import pandas as pd

file = 'insumos/insumos_ti.csv'

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


for i in range(len(correo)):
    print(f' Nombre: {nombre[i]} \n Correo: {correo[i]} \n Codigo MP: {codigo_mp[i]} \n Sistema Operativo: {so[i]} \n Telefono: {telefono[i]} \n Departamento: {departamento[i]} \n Correo Jefatura: {correo_jefatura[i]}')
