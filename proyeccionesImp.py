import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# DATE FORMATING
today = datetime.now().strftime('%d_%b_%Y')
unformated_yesterday = datetime.now() - timedelta(1)
yesterday = unformated_yesterday.strftime('%d_%b_%Y')

# CONSTANTS
ROUTE = '/mnt/imp'


template = pd.read_csv(ROUTE+'/PagesPerDay_'+yesterday+'.csv')

dict_csv = {}

for i in range(32):
    # fecha | sucursal | modelo | hojas impresas
    today_instance = datetime.now() - timedelta(i + 5)
    today_loop = today_instance.strftime('%d_%b_%Y')
    yesterday_instance = datetime.now() - timedelta(i + 6)
    yesterday_loop = yesterday_instance.strftime('%d_%b_%Y')
    just_date = today_instance.strftime('%d_%b_%Y')
    loop_date = today_instance.strftime('%d-%m-%Y')

    temp = pd.read_csv(ROUTE+'/PagesPerDay_'+today_loop+'.csv')
    list_csv = []
    model_list = []
    dict_loop = {
        loop_date : {
            'Locación' :temp["Location"], 
            'Modelo' : temp["Model Name"],
            'Paginas Usadas' : temp["Paginas Usadas Hoy"],
        }
    }
    dict_csv.update(dict_loop)


name = 'Proyecciones_IMP_'+today+'.csv'
required_csv = pd.DataFrame(dict_csv)
required_csv = required_csv.transpose()
required_csv.to_csv(ROUTE+'/'+name)


