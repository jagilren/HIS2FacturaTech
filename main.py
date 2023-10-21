import logging
import time
import threading
import os
import pyodbc
from decimal import Decimal
import inisettings, qmsaccess_defineTotals, XMLBuilder, base64_generator, postUploadInvoice,postDocumentStatusFile, qmsaccess_RetrievingQuery,txtlogs
from sendMail import sendEmail
import dbSqlite3

def mainUploadInvoiceRoutine():

    try:
        xmlfile = 'outputxml1.xml'
        #Query next Invoice for upload to Electronic Operator FacturaTech
        facturaNumero=qmsaccess_RetrievingQuery.traeFactura()

        #Query retries for upload  Invoice forto Electronic Operator FacturaTech
        facturaRetries= dbSqlite3.queryFacturaRetries(facturaNumero) if  dbSqlite3.queryFacturaRetries(facturaNumero) != None else 0
        #Get value of retries parameters from CONFIG.INI file
        retriesFE, retriesNC = inisettings.configRead()
        #Verifies that factura exist and retries is in aceptable boundaries
        if (facturaNumero is not None) and (facturaRetries is None or facturaRetries < retriesFE):
            dictGroups, dictTotals, totalFactura = qmsaccess_defineTotals.RetrieveTotals(facturaNumero)
            if (dictGroups and dictTotals and totalFactura):
                totalItems=str(len(dictGroups['IVA19'])+ len(dictGroups['IC08']))
                facturaNumero='26136' #Solo para efectos de poder subir la información al DEMO de FacturaTech
                XMLBuilder.generateXML(xmlfile, facturaNumero,str(totalFactura),str(totalItems),  dictGroups, dictTotals)
                base64Invoice = base64_generator.Base64XMLFile(xmlfile)
                postStatusCode, transactionID = postUploadInvoice.postRequest(base64Invoice)
                if postStatusCode == 200:
                    code_response,signed_status,error_status= postDocumentStatusFile.postRequest(transactionID)
                    if code_response == str(201):
                        txtlogs.writeLog(facturaNumero)
                reintentos = 1 if facturaRetries ==  None else facturaRetries + 1
                dbSqlite3.insertUploadInvoiceRecord(facturaNumero,'FEFA', transactionID,'FE',totalFactura, reintentos)
                respuestaEnvio = sendEmail(facturaNumero, transactionID,postStatusCode)
        else:
            txtlogs.writeLog("Error to query facturaNumero")
    except Exception as e:
        logging.error(f"An unexpected error occurred in FacturaTech Service: {str(e)}")
        facturaNumero = facturaNumero if fac
        txtlogs.writeLog

    else:
        pass
        #If over a complete day, not has transmisión to FacturaTech mark Invoice to failed in msaccess Database
        #If retries is Not None
    finally:
        print('Termina Ciclo de subida de Documento')


if __name__ == "__main__":
    # Create a daemon thread
    while True:
        try:
            fe_upload_thread = threading.Thread(target=mainUploadInvoiceRoutine)
            fe_upload_thread.daemon = True  # Set it as a daemon thread
            fe_upload_thread.start()
            time.sleep(20000)
        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            print('Termina Routine')

