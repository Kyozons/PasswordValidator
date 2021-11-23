import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

route = '/mnt/imp' # Ruta carpeta principal
app = '/home/soporteti/printerStatus/mundo/monitoreo/static/monitoreo/images'

for i in range(32):
    today_instance = datetime.now() - timedelta(i + 1)
    today_loop = today_instance.strftime('%Y-%m-%d_1634')

    yesterday_instance = datetime.now() - timedelta(i + 2)
    yesterday_loop = yesterday_instance.strftime('%Y-%m-%d_1634')
    just_date = today_instance.strftime('%d_%b_%Y')

    # CREACION DE LOS SET DE DATOS
    device_list_today = pd.read_csv(route+'/DevicesList_'+today_loop+'.csv')# Lista del día actual de dispositivos
    device_list_yesterday = pd.read_csv(route+'/DevicesList_'+yesterday_loop+'.csv') # Lista del día anterior de dispositivos

    used_pages = device_list_today[["Location", "Model Name"]] # Nuevo set de datos conteniendo locacion de las Impresoras
    used_pages["Paginas Usadas Hoy"] = device_list_today["Total Page Count"] - device_list_yesterday["Total Page Count"] # Agregar la diferencia de las páginas usadas para obtener el total del día

    plot = used_pages.dropna() # Crear nuevo set de datos eliminando todos los NaN del set anterior

    name = 'PagesPerDay_'+just_date+'.csv'
    plot.to_csv(route+'/'+name)

