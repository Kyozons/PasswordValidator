#!/usr/bin/python3 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, sys, time, ezsheets
import pandas as pd

full_path = '/home/pedro.bustos.l/PythonProyects/RPA/' 

# Descargar tabla como csv para procesar
ss = ezsheets.Spreadsheet('1gz3rHN_xXxHh9Pkzuaqwi_RrAyjogYvEhHLn2iPQVcs')
ss.refresh()
ss.downloadAsCSV(f'{full_path}insumos/insumos_ti.csv')

with open(f'{full_path}creds', 'r') as creds:
    data = creds.read()
user = data[:41]
passwd = data[42:]

file = f'{full_path}insumos/insumos_ti.csv'

# Tomar el archivo de insumos TI desde la ruta indicada para procesar   
insumos_ti = pd.read_csv(file)

# Quitar todas las filas que tengan más de 19 valores Nulos, lo que significa que estan vacías.
insumos_nan = insumos_ti[insumos_ti.isnull().sum(axis=1) < 19]
insumos_nan = insumos_nan[insumos_nan["Request #"].isnull()]  # Seleccionar sólo las filas que tengan la columna Request # vacia
insumos_ti = insumos_nan[insumos_nan["Estado"].isnull()]  # Seleccionar sólo las filas que también tengan la columna Estado vacia

# Guardar las variables de cada columna relevante en listas.
correo = insumos_ti["Dirección de correo electrónico"].to_list()  # Lista de correos
nombre = insumos_ti["Nombres"] + ' ' + insumos_ti["Apellido Paterno"] + ' ' + insumos_ti["Apellido Materno"]  # Concatenar nombres y apellidos
nombre = nombre.to_list()  # Lista de nombres completos
codigo_mp = insumos_ti["Código MP Asignado a su Equipo"].to_list()  # Lista de Códigos MP
so = insumos_ti["Sistema Operativo"].to_list()  # Lista de Sistemas Operativos
telefono = insumos_ti["Contacto Telefonico (+56911112222)"].to_list()  # Lista de telefonos
departamento = insumos_ti["Seleccione su Departamento"].to_list()  # Lista de áreas
correo_jefatura = insumos_ti["Correo Jefatura Directa (nombre.apellido@mundopacifico.cl)"].to_list()  # Lista de correos de jefatura
ciudad = insumos_ti["Ciudad puesto de trabajo"].to_list()  # Lista de ciudad donde trabaja
insumo = insumos_ti["Seleccione el insumo requerido"].to_list()  # Lista de insumos solicitados
cantidad_req = insumos_ti["Indique la Cantidad requerida"].to_list()  # Cantidad requerida del insumo
observacion = insumos_ti["Observacion"].to_list()  
segundo_insumo = insumos_ti["Necesita que agreguemos otro insumo TI - Observaciones (Opcional)"].to_list()


# print(f' Nombre: {nombre[0]} \n Correo: {correo[0]} \n Codigo MP: {codigo_mp[0]} \n Sistema Operativo: {so[0]} \n Telefono: {telefono[0]} \n Departamento: {departamento[0]} \n Correo Jefatura: {correo_jefatura[0]}')

br = webdriver.Chrome()
br.get('https://gmail.com')

# Login google
user_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(user, Keys.ENTER)
pwd_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(passwd)


# Inicio loop de envio correos
for i in range(len(correo)):
    msg_button = WebDriverWait(br, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'z0'))).click()  # Click en redactar
    to = 'ticket@mundotelecomunicaciones.cl'
    to_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'to')))
    to_box.send_keys(to, Keys.TAB)

    subject = f'Solicitud insumos {nombre[i]}'
    subject_box = WebDriverWait(br, 10).until(EC.visibility_of_element_located((By.NAME, 'subjectbox')))
    message = f' Nombre: {nombre[i]} \n Correo: {correo[i]} \n Codigo MP: {codigo_mp[i]} \n Sistema Operativo: {so[i]} \n Telefono: {telefono[i]} \n Departamento: {departamento[i]} \n Correo Jefatura: {correo_jefatura[i]} \n Ciudad: {ciudad[i]} \n Insumo solicitado: {insumo[i]} \n Cantidad: {cantidad_req[i]} \n Observación: {observacion[i]} \n Otros insumos: {segundo_insumo[i]}'
    subject_box.send_keys(subject, Keys.TAB, message, Keys.TAB, Keys.ENTER)
    print(f'Enviando correo {i+1}/{len(correo)}')
    time.sleep(5)







