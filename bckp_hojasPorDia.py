import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

route = '/mnt/imp' # Ruta carpeta principal
app = '/home/soporteti/printerStatus/mundo/monitoreo/static/monitoreo/images'


# CREAR VARIABLES PARA FECHA FORMATEADEA DE AYER Y HOY
f = datetime.now() 
date = f.strftime("%Y-%m-%d_1634")
just_date = f.strftime('%d_%b_%Y')
fa = datetime.now() - timedelta(1)
yesterday = fa.strftime("%Y-%m-%d_1630")

# CREACION DE LOS SET DE DATOS
device_list_today = pd.read_csv(route+'/DevicesList_2021-11-14_1634.csv')# Lista del día actual de dispositivos
device_list_yesterday = pd.read_csv(route+'/DevicesList_2021-11-13_1634.csv') # Lista del día anterior de dispositivos


used_pages = device_list_today[["Model Name", "IP Address", "Location"]] # Nuevo set de datos conteniendo Modelos, IP y locacion de las Impresoras

used_pages["Today Pages"] = device_list_today["Total Page Count"] # Agregar total de páginas del día actual

used_pages["Yesterday Pages"] = device_list_yesterday["Total Page Count"] # Agregar total de páginas del día anterior

used_pages["Used Pages"] = used_pages["Today Pages"] - used_pages["Yesterday Pages"] # Agregar la diferencia de las páginas usadas para obtener el total del día

plot = used_pages.dropna() # Crear nuevo set de datos eliminando todos los NaN del set anterior

# CREACION DEL GRÁFICO
x = plot["Location"]
y = plot["Used Pages"]

name = 'PagesPerDay_14_Nov_2021.csv'
plot.to_csv(route+'/'+name)

hbar = plt.barh(x, y, height = 0.5) # Gráfico de barras horizontales:
plt.bar_label(hbar) # Mostrar valor en cada barra
plt.title('Cantidad de impresiones del día 14_Nov_2021')
fig = plt.gcf() # Get current Figure
fig.set_size_inches((14, 7)) # Ajustar el tamaño de la figura (ancho, alto)

# GUARDAR EL GRAFICO
fig.savefig(route+'/graph_14_Nov_2021', dpi=97.2)
fig.savefig(app+'/graph_14_Nov_2021', dpi=97.2)
