import pyodbc
conn = pyodbc.connect('DSN=access2003DSN;')

# Create a cursor
cursor1 = conn.cursor()

outlaw=-1
consumo_dateIni = '2023-09-24 13:28:00'
consumo_dateFin = '2023-09-24 13:29:09'
facturaNumero = 1245895.0

# Execute a SQL query
query = f"""UPDATE  [CONSUMO]  set [CONSUMO].[OUTLAW]='{outlaw}' 
        WHERE  [CONSUMO].[NUMERO FACTURA]= {facturaNumero}"""
cursor1.execute(query)
cursor1.commit()

# Close the cursor and connection
cursor1.close()
conn.close()