import random
import pyodbc
from decimal import Decimal

def traeFactura():
    global cursor, conn
    try:
        conn = pyodbc.connect('DSN=access2003DSN;')
        # Create a cursor
        cursor = conn.cursor()

        outlaw = -1

        # Execute a SQL query
        query = "SELECT  [NUMERO FACTURA]  FROM [TOTALES] WHERE [TOTALES].[ISFE]= -1 ORDER BY [TOTALES].[NUMERO FACTURA] ASC"
        cursor.execute(query)
        rows = cursor.fetchall()
        facturaNumero: Decimal = Decimal(random.choice(rows)[ 0 ])
        #print(facturaNumero)

    except:
        facturaNumero=None
    else:
        cursor.close()
        conn.close()
    finally:
        pass
    return facturaNumero

# Execute a SQL query for get Names of columns on Table
'''
query= "SELECT  [NUMERO FACTURA], [HORA CON]  FROM [CONSUMO] WHERE [CONSUMO].[HORA CON]= ?"
cursor.execute(query, (consumo_dateIni))

#cursor.execute('SELECT * FROM [TOTALES] WHERE [TOTALES].[NUMERO FACTURA]>= 100000 AND [Fecha de pago] >= ? AND [Fecha de pago] <= ? ')
rows = cursor.fetchone()
print(type(cursor.description))
print('Primera Columna de cursos.description', cursor.description[0])
print('Segunda Columna de cursos.description', cursor.description[1])
column_names = [columna[0] for columna in cursor.description]

# Print column names as a header
print(", ".join(column_names))

# Display the fetched data

if rows is not  None:
    print('Numero Factura', rows[0],rows[1])

if rows is not  None:
    for row in rows:
        pass
        print(rows[0])
'''


# Close the cursor and connection


def getNumberAttemps():
    global cursor, conn
    try:
        conn = pyodbc.connect('DSN=access2003DSN;')
        # Create a cursor
        cursor = conn.cursor()

        # Execute a SQL query
        query = "SELECT  [NUMERO FACTURA]  FROM [TOTALES] WHERE [TOTALES].[ISFE]= -1 ORDER BY [TOTALES].[NUMERO FACTURA] ASC"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
    except:
        pass
    else:
        cursor.close()
        conn.close()
    finally:
        pass
