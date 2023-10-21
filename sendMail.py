import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

'''imap.google.com
Port: 465
account  pythonforsendmail@gmail.com
pass:  bmaqjqoxdyhkogyc
Encrypt Mode: SSL
'''
def sendEmail(facturaNumero, transactionID, postStatusCode):
    global smtp_server
    sender_email = "pythonforsendmail@gmail.com"
    sender_password = "bmaqjqoxdyhkogyc"

    # Create a message object
    message = MIMEMultipart()

    # Set the email subject
    if postStatusCode==200:
        message["Subject"] = "Factura"  + " " + facturaNumero + " " + "Subida a FacturaTech"
        body = "succesfull operation  method uploadInvoiceFile at::" + f'{datetime.datetime.now()}'
    else:
        message["Subject"] = "Fallo en envío Factura"  + " " + facturaNumero     # Set the sender's email address
    message["From"] = "jagilren@gmail.com"
    # Set the recipient's email address
    message["To"] = "sistemas@inversionesler.co"
    #print(message["To"])
    # Add the email body
    message.attach(MIMEText(body, "plain"))

    # Establish a connection to the SMTP server
    #smtp_server = smtplib.SMTP("imap.google.com", 465) Deprecated
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()  # For secure communication

        # Log in to your email account
        smtp_server.login(sender_email, sender_password)
        # Send the email
        smtp_server.sendmail(sender_email, message["To"], message.as_string())

    except:
        return "email no enviado"
    finally:
        # Close the SMTP server connection
        smtp_server.quit()

#sendEmail()