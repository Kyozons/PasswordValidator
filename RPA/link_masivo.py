#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os, sys, time, ezsheets
import pandas as pd

full_path = '/home/pedrobustosl/PythonProyects/RPA/'

# Credenciales
with open(f'{full_path}vici_creds', 'r') as creds:
    data = creds.read()
user = data[:7]
passwd = data[8:]

# Pequeña muestra de usuarios para enviar correo de vici
user_db = [
    19344852,
    17454307,
    116819945,
    20021999,
    13508697,
    123,
    27202248,
    16600953,
    18405407,
    17573018,
    268138463,
    13859021,
    26610158,
    26154534,
    26002817,
    14210090,
    12920515,
    26269789,
    26319502,
    19657194,
    122,
    26571412,
    558,
    26506291,
    12554196,
    17746192,
    16394416,
    "pneira",
    9174182,
    16620688,
    13380228,
    17570340,
    15186845,
    16218215,
    17046020,
    175746145,
    143537803,
    26306542,
    26903120,
    16533976,
    194384858,
    14549557,
    19815030,
    13807687,
]

# Inicializar el webdriver de Chrome
service = Service('/home/pedrobustosl/chromedriver')
service.start()
br = webdriver.Remote(service.service_url)
# Iniciar sesion en la pagina de admin para evitar prompts
br.get(f'https://cc.mundopacifico.cl/vicidial/admin.php')
time.sleep(4)

# Ingresar al link de envio de correo por cada usuario en la lista de usuarios
for vici_user in user_db:
    br.get(f'https://cc.mundopacifico.cl/vicidial/email_agent_login_link.php?preview=0&agent_id={vici_user}')
br.quit()
