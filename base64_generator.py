import pyperclip
import hashlib
import base64


def basic_auth(input_string):
    # Encode the string as bytes (UTF-8 encoding)
    input_bytes = input_string.encode('utf-8')
    # Calculate the SHA-256 hash
    sha256_hash = hashlib.sha256(input_bytes).hexdigest().upper()
    #print(sha256_hash)
    # Convert the hash to a Base64-encoded string
    #base64_encoded = base64.b64encode(sha256_hash).decode('utf-8')
    return sha256_hash

def Base64XMLFile(xmlfile):

    # Define the path to the input XML file
    input_xml_file = xmlfile  # Replace with your file path

    # Define the path to the output Base64 file (or None to store in a variable)
    output_base64_file = 'output_base64.txt'  # Replace with your desired output file path or set to None

    # Read the contents of the XML file
    with open(input_xml_file, 'rb') as xml_file:
        xml_contents = xml_file.read()

    # Encode the XML contents as Base64
    base64_encoded = base64.b64encode(xml_contents).decode('utf-8')

    # Print or save the Base64-encoded data
    if output_base64_file:
        with open(output_base64_file, 'w') as base64_file:
            base64_file.write(base64_encoded)
        pyperclip.copy(base64_encoded)
        #print("Base64-encoded XML:")
        #print(base64_encoded)
        return base64_encoded
    else:
        pass
        print("Base64-encoded XML:")
        print(base64_encoded)


#print(basic_auth('sandboxws*'))
