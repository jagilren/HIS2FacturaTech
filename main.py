#Commited to origin in GitHub Public Repository HIS2FacturaTech
import logging
import time
import threading
import argparse
import os
import pyodbc
from decimal import Decimal
import inisettings, qmsaccess_defineTotals, XMLBuilder, base64_generator, postUploadInvoice,postDocumentStatusFile, qmsaccess_RetrievingQuery,txtlogs
import q_updateTotalesFacturaTeched
from sendMail import sendEmailTruePositivo
import dbSqlite3

def getfacturaNumero():
    # Query next Invoice for upload to Electronic Operator FacturaTech
    facturaNumero = qmsaccess_RetrievingQuery.traeFactura()
    return facturaNumero


def getDocumentRetries(facturaNumero):
    try:
        # Query retries for upload  Invoice to Electronic Operator. FacturaTech
        #facturaRetries = dbSqlite3.queryFacturaRetries(facturaNumero) if dbSqlite3.queryFacturaRetries(facturaNumero) != None else 0
        # Get value of retries parameters from CONFIG.INI file
        retriesFE, retriesNC = inisettings.configRead()
        return retriesFE, retriesNC
    except:
        retriesFE = retriesNC =None
        return retriesFE, retriesNC

def getReintentosUploaadFactura(facturaNumero):
    try:
        results = dbSqlite3.queryFacturaRetries(facturaNumero)
    except:
        return None
    else:
        return results

def mainUploadInvoiceRoutine(url, userPro, passPro):

    try:
        xmlfile = 'outputxml1.xml'
        facturaNumero = getfacturaNumero()
        if facturaNumero is None:
            raise ValueError("The value of numeroFactura is None. Please provide a valid value.")
        retriesFE, retriesNC = getDocumentRetries(facturaNumero)
        reintentos = getReintentosUploaadFactura(facturaNumero)
        reintentos = -1 if reintentos is None else reintentos
        #Verifythat factura exist and retries is in aceptable boundaries
        if (facturaNumero is not None) and (reintentos is None or reintentos < retriesFE):
            dictGroups, dictTotals, totalFactura = qmsaccess_defineTotals.RetrieveTotals(facturaNumero)
            if (dictGroups and dictTotals and totalFactura):
                totalItems=str(len(dictGroups['IVA19'])+ len(dictGroups['IC08']))
                #Pendiente comentar line
                #facturaNumero='26155' #Solo para efectos de poder subir la información al DEMO de FacturaTech
                XMLBuilder.generateXML(xmlfile, facturaNumero,str(totalFactura),str(totalItems),  dictGroups, dictTotals)
                base64Invoice = base64_generator.Base64XMLFile(xmlfile)
                postStatusCode, transactionID = postUploadInvoice.postRequest(base64Invoice,facturaNumero,url, userPro, passPro)
                if postStatusCode == 200 and transactionID:
                    code_response,signed_status,error_status= postDocumentStatusFile.postRequest(transactionID,url, userPro, passPro)
                    if code_response == str(201):
                        respuestaTruePositivo = sendEmailTruePositivo(facturaNumero, transactionID, postStatusCode)
                        txtlogs.writeLog(facturaNumero, f'Factura subida correctamente a plataforma Proveedor de Facturación Electrónica')
                else:
                    respuestaFalsePositivo = sendEmailTruePositivo(facturaNumero, transactionID, postStatusCode)
                    txtlogs.writeLog(facturaNumero,
                                     f'Factura No pudo ser Cargada a plataforma Proveedor de Facturación Electrónica')
                #Revisa cuantas veces se ha reintentado subir la factura a Plataforma de FacturaTech
                if reintentos < 0:
                    #"Pendiente de revisión"
                    dbSqlite3.insertUploadInvoiceRecord(facturaNumero,'FEIF', transactionID,'FE',totalFactura, reintentos)
                else:
                    dbSqlite3.sqliteUpdateFacturaRetries(facturaNumero)
                    if reintentos >= int(retriesFE):
                        #Establece en True campo exhaustRetries en Tabla totales de Access para que on siga intentando con esta factura
                        q_updateTotalesFacturaTeched.updateTotalesExhaustRetriesFT(facturaNumero)
                        dbSqlite3.sqliteUpdateExhaustRetriesFT(facturaNumero)

        elif reintentos >= retriesFE:
            txtlogs.writeLog(facturaNumero, f'Se alcanzó el número de reintentos máximo de la factura Target: {facturaNumero}')
        else:
            txtlogs.writeLog(facturaNumero, "qmsaccess_RetrievingQuery.py not get Factura")
    except ValueError as ve:
        logging.error(f"Warning.  No left facturas for uploadInvoiceFile: {str(ve)}")
        txtlogs.writeLog(facturaNumero,f'''numerofactura is None  {str(ve)}
                threading continues''' )
    except Exception as e:
        logging.error(f"An unexpected error occurred in FacturaTech Service: {str(e)}")
        facturaNumero = facturaNumero
        txtlogs.writeLog(facturaNumero,f'''Error main.mainUploadInvoiceRoutine {str(e)}
                Error Conecting to web service resource''' )
    else:
        print('Termina Ciclo de subida de Documento.  todo correcto pasa por ELSE')
        #If over a complete day, not has transmisión to FacturaTech mark Invoice to failed in msaccess Database
        #If retries is Not None
    finally:
        pass
        #print('Termina Ciclo de subida de Documento.  todo correcto pasa por Finally')


if __name__ == "__main__":

    url, userPro, passPro = inisettings.ReadEndPointProData()
    #url, userPro, passPro = inisettings.ReadEndPointDemoData()
    while True:
        mainUploadInvoiceRoutine(url, userPro, passPro)
        time.sleep(3)
        #print('Comienza conteo de Veinte mil segundos')
        #time.sleep(20000)
        #No necessary use of threads
        '''try:
            fe_upload_thread = threading.Thread(target=mainUploadInvoiceRoutine, args=(url, userPro, passPro),name='fe_upload_thread')
            fe_upload_thread.daemon = True  # Set it as a daemon thread
            fe_upload_thread.start()
            time.sleep(20000)
        except KeyboardInterrupt:
            print("Exiting...")
        finally:
            print('Termina Routine', ' ', 'Continue Infinite Loop')'''
