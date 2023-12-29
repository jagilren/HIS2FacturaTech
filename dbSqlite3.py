import sqlite3
import os
from datetime import datetime

# Check if the database file exists



global conn1, cursor1
def connectDB():
    if not os.path.exists('mydatabase'):
        conn1 = sqlite3.connect("mydatabase")
        cursor1 = conn1.cursor()
        cursor1.execute("""
            CREATE TABLE INVOICES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoiceNumber TEXT,
                invoiceprefix TEXT,
                transactionid TEXT,
                documenttype TEXT,
                invoiceamount REAL,
                retriesfee SMALLINT,
                fecha  DATETIME
            )
        """)
    else:
        conn1 = sqlite3.connect("mydatabase")
        cursor1 = conn1.cursor()
    return conn1,cursor1
        #raise FileNotFoundError("The SQLite database file 'your_database.db' does not exist.")

def insertUploadInvoiceRecord(facturaNumero, invoicePrefix,  transactionID,documentType, totalFactura, reintentos):

        try:
            conn1,cursor1=connectDB()
            database='sqlite3'
        except Exception as e:
            #print(e)
            database = None
        else:
            pass
        finally:
            pass

        try:
            invoice_data = (f"{facturaNumero}", f"{invoicePrefix}",f"{transactionID}",f'{documentType}', f'{totalFactura}', reintentos, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            cursor1.execute("INSERT INTO INVOICES (invoicenumber, invoiceprefix, transactionid,documenttype, invoiceamount, retriesfee, fecha) VALUES (?, ?, ?, ?, ?, ?, ?)", invoice_data)
            conn1.commit()
            #results = cursor1.fetchall()
        except:
            pass
        else:
            cursor1.close()
            conn1.close()
        finally:
            pass

def queryFacturaRetries(facturaNumero):
        try:
            conn1,cursor1=connectDB()
            database='msaccess'
        except Exception as e:
            #print(e)
            database = None
        finally:
            pass

        try:
            if cursor1 is not None:
                cursor1.execute(f"SELECT retriesfee FROM INVOICES WHERE invoicenumber = '{facturaNumero}'")
                conn1.commit()
                results = cursor1.fetchall()

            if not results:
                results = None
        except:
            results = None
        else:
            cursor1.close()
            conn1.close()
        finally:
            return results


def sqliteUpdateFacturaRetries(facturaNumero):
    try:
        conn1, cursor1 = connectDB()
        cursor1.execute(f'UPDATE  INVOICES SET retriesfee=retriesfee+1  WHERE invoicenumber = {facturaNumero}')
        conn1.commit()


    except:
        return False
    else:
        cursor1.close()
        conn1.close()
        return True
    finally:
        pass

def sqliteUpdateExhaustRetriesFT(facturaNumero):
    try:
        conn1, cursor1 = connectDB()
        cursor1.execute(f'UPDATE  INVOICES SET exhaustedRetriesFT=-1  WHERE invoicenumber = {facturaNumero}')
        conn1.commit()
    except:
        return False
    else:
        cursor1.close()
        conn1.close()
        return True
    finally:
        pass
