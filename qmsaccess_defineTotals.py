import pyodbc
from decimal import Decimal

facturaNumero= 1299.0
outlaw=0

def RetrieveTotals(facturaNumero):
    try:
        # Create a cursor
        conn1 = pyodbc.connect('DSN=access2003DSN;')
        cursor1 = conn1.cursor()

        # Execute a SQL query
        queryGroups = f"""SELECT [llser co], [Total],[ValIVA]   FROM [CONSUMO]   
                WHERE  [CONSUMO].[NUMERO FACTURA]= {facturaNumero} AND  [CONSUMO].[ISFE]=-1"""
        cursor1.execute(queryGroups)
        rows=cursor1.fetchall()
        #Crea Lista todos los Grupos de Articulos de HIS para luego construir los Diccionarios
        listGroups= [x[0].split(" ")[0] for x in rows]
        setUniqueGroups=set(listGroups)
        listUniqueGroups=list(setUniqueGroups)

        # Create Dict  with root   keys of groups of  Items
        dictTotals= {'base':Decimal(0), 'impuestos':Decimal(0)}
        dictGroups= {'IVA19': {}, 'IC08':{}}
        #Let's go calculate Tax for Item Groups

        for group in listUniqueGroups:
            if group == 'RESTAURANTE':
                if group not in dictGroups['IC08']:
                    dictGroups['IC08'][group] = {'base': Decimal('0'),'impuesto': Decimal('0')}
            else:
                if group not in dictGroups['IVA19']:
                    dictGroups['IVA19'][group] = {'base': Decimal('0'), 'impuesto': Decimal('0')}

        #Recorremos cada fila fetchAll recuperado y ubicamos sus valores en el respectivo Diccionario
        for row in rows:
            if row[0].split(' ')[0] in  dictGroups['IVA19']:
                group=row[0].split(' ')[0]
                #print('ROW====', row)
                dictGroups['IVA19'][group]['base'] = dictGroups['IVA19'][group]['base'] + row[1]
                dictGroups['IVA19'][group]['impuesto']=dictGroups['IVA19'][group]['impuesto']+ row[2]
            elif  row[0].split(' ')[0] in dictGroups['IC08']:
                group=row[0].split(' ')[0]
                dictGroups[ 'IC08' ][group][ 'base' ] = dictGroups[ 'IC08' ][ group ][ 'base' ] + row[ 1 ]
                dictGroups[ 'IC08' ][ group ][ 'impuesto' ] = dictGroups[ 'IC08' ][ group ][ 'impuesto' ] + row[ 2 ]
            else:
                pass
            dictTotals['base']=dictTotals['base'] + row[1]
            dictTotals['impuestos']+= row[2]

        totalFactura = round(dictTotals['base'] + dictTotals['impuestos'], 0)
        dictTotals['base']=round(dictTotals['base'],2)
        dictTotals['impuestos']=round(totalFactura - dictTotals['base'], 2)
        #print(dictTotals)

        for dictKeys, dictValues in dictGroups.items():
            pass
            #print('Valores',dictKeys, dictValues)
    except:
        dictGroups = None
        dictTotals = None
        totalFactura = None
    else:
        cursor1.close()
        conn1.close()
    return dictGroups, dictTotals, totalFactura

dict1, dict2, totalFactura=RetrieveTotals(facturaNumero)
#print('Diccionario1 keys', list(dict1.keys()))
#print('Diccionario1 pairs', dict1.items())
#print('Diccionario2',dict2)
#print('totalFactura',totalFactura)