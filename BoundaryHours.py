from datetime import datetime, timedelta
from decimal import Decimal

def ConsigueHoras():
    hours_ini = 7
    minutes_ini = 0
    seconds_ini = 0

    hours_fin = 6
    minutes_fin = 59
    seconds_fin = 59

    formatted_time_ini = "{:02d}:{:02d}:{:02d}".format(hours_ini, minutes_ini, seconds_ini)
    formatted_time_fin = "{:02d}:{:02d}:{:02d}".format(hours_fin, minutes_fin, seconds_fin)
    formatted_date_ini = (datetime.now().date()-timedelta(days=1)).strftime("%m/%d/%Y")
    formatted_date_fin = (datetime.now().date()-timedelta(days=0)).strftime("%m/%d/%Y")
    #formatted_datetime = datetime.now().date().strftime("%m/%d/%Y %H:%M:%S")
    formatted_datetime_ini = formatted_date_ini + " " + formatted_time_ini
    formatted_datetime_fin = formatted_date_fin + " " + formatted_time_fin
    print(formatted_datetime_ini, formatted_datetime_fin)
    return formatted_datetime_ini, formatted_datetime_fin