import pyodbc
import txtlogs

conn = pyodbc.connect('DSN=access2003DSN;')
# Create a cursor
cursor1 = conn.cursor()
boolfacturaTeched = -1


def updateTotalesFacturaTeched(facturaNumero):
    try:

        # Execute a SQL query
        query = f'''UPDATE  [TOTALES]  set [TOTALES].[FacturaTeched]={boolfacturaTeched} 
                WHERE  [TOTALES].[Numero factura]={facturaNumero} AND [TOTALES].[isFE]=-1'''
        cursor1.execute(query)
        cursor1.commit()
    except Exception as e:
        txtlogs.writeLog(facturaNumero, f'q_updateTotalesFacturaTech-{str(e)}')
        return False
    else:
        cursor1.close()
        conn.close()
        return True
        # Close the cursor and connection
    finally:
        pass

def updateTotalesExhaustRetriesFT(facturaNumero):
    try:
        # Execute a SQL query
        boolExhaustRetriesFT = -1
        query = f'''UPDATE  [TOTALES]  set [TOTALES].[exhaustedRetriesFT]={boolExhaustRetriesFT} 
                WHERE  [TOTALES].[Numero factura]={facturaNumero} AND [TOTALES].[isFE]=-1'''
        cursor1.execute(query)
        cursor1.commit()
    except Exception as e:
        txtlogs.writeLog(facturaNumero, f'updateTotalesExhaustRetriesFT-{str(e)}')
        return False
    else:
        cursor1.close()
        conn.close()
        return True
        # Close the cursor and connection
    finally:
        pass
