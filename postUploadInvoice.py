import xml.etree.ElementTree as ET
import requests
import q_updateTotalesFacturaTeched
from inisettings import ReadEndPointProData, ReadEndPointDemoData


'''#url, userPro, passPro  = ReadEndPointDemoData()
#Define Variables Globales
#url = url
#userEndPoint= userPro
#passwordEndPoint= passPro
# Define the URL of the SOAP web service'''


# Define the headers for the POST request
def postRequest(base64Invoice,facturaNumero,url, userPro, passPro):
    headers = {
        'SOAPAction': f'urn:{url}#FtechAction.uploadInvoiceFile',
        'Content-Type': 'text/xml; charset=utf-8'
    }


    # Define the SOAP request payload as a string
    soap_request = f'''
    <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
        <Body>
            <FtechAction.uploadInvoiceFile xmlns="urn:{url}">
                <username>{userPro}</username>
                <password>{passPro}</password>
                <xmlBase64>{base64Invoice}</xmlBase64>
            </FtechAction.uploadInvoiceFile>
        </Body>
    </Envelope>
    '''

    # Send the POST request with headers and SOAP request payload
    response = requests.post(url, headers=headers, data=soap_request)
    #print(response)

    # Check the response status and content
    if response.status_code == 200:
        #print(response.text)
        #print(response.status_code)
        #print("Request succeeded. Response content:")
        root = ET.fromstring(response.text)
        result_element = root.find(".//transaccionID")
        result_value_transaction = result_element.text
        # print("Value of <transaccionID>:", result_value_transaction)
        if result_value_transaction:
            #Code for Update Field FacturaTeched in Table Totales DSNAccess2003
            q_updateTotalesFacturaTeched.updateTotalesFacturaTeched(facturaNumero)

    else:
        pass
        #print(f"Request failed with status code {response.status_code}.")

    #print('POST method UploadInvoice reached with sucessfull')
    return response.status_code, result_value_transaction