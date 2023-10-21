import xml.etree.ElementTree as ET
import requests
#Define Variables Globales
userNameDemo='GAMA070223'
passwordDemo='502d77c7c1d5fa0f4495d104b29ad80cda2510238fb66ba7f107303317d49bc5'

# Define the URL of the SOAP web service
url = 'https://ws.facturatech.co/v2/demo/index.php?wsdl'

# Define the headers for the POST request
def postRequest(transactionID):
    headers = {

        'SOAPAction': 'urn:https://ws.facturatech.co/v2/demo/#FtechAction.documentStatusFile',
        'Content-Type': 'text/xml; charset=utf-8'
    }


    # Define the SOAP request payload as a string
    soap_request = f'''
    <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
        <Body>
            <FtechAction.documentStatusFile xmlns="urn:https://ws.facturatech.co/v2/demo/">
                <username>{userNameDemo}</username>
                <password>{passwordDemo}</password>
                <transaccionID>{transactionID}</transaccionID>
            </FtechAction.documentStatusFile>
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

        result_code = root.find(".//code")
        result_sucess = root.find(".//sucess")
        result_status = root.find(".//status")
        result_error = root.find(".//error")

        result_code_text = result_code.text
        #result_sucess_text = result_sucess.text
        result_status_text = result_status.text
        result_error_text = result_error.text

        #print("Value of <code>:", result_code_text)
        #print("Value of <sucess>:", result_sucess_text)
        #print("Value of <status>:", result_status_text)
        #print("Value of <error>:", result_error_text)


    else:
        pass
        #print(f"Request failed with status code {response.status_code}.")

    return result_code_text, result_status_text,result_error_text