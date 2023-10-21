from datetime import datetime
# Log the operation in a text file

def writeLog(facturaNumero):
    try:
        log_file = "sqllogs.txt"  # Replace with your log file name
        log_message = f"Factura: {facturaNumero}  written in FacturaTech plattform at  {datetime.now()}\n"

        with open(log_file, "a") as file:
            file.write(log_message)
            file.close()
    except:
        pass
    else:
        pass
    finally:
        pass