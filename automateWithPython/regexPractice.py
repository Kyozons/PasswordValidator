import re

phone_num_regex = re.compile(r'(\+56)?(9)(\d{8})')

user_phone_num = input('Ingrese su numero telefonico ( EJ: 912345678): ')

mo = phone_num_regex.search(user_phone_num)

if mo == None:
    print(r'Teléfono es inválido.')
else:
    print('Número de teléfono encontrado: ' + mo.group())


