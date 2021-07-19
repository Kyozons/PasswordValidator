import random
def check_password(usr_password):
    lower_case = 'abcdefghijklmnopqrstuvwxyz'
    upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers    = '123456789'
    symbols    = '!#$%&.-_'
    sum = 0 ; a = 0 ; b = 0 ; c = 0 ; d = 0

    while sum != 4:
        while len(usr_password) <=5:
               usr_password = input('\nLa contraseña debe ser de minimo 6 caracteres, ingrese nuevamente: ')

        for x in range(len(usr_password)):
            if usr_password[x] in lower_case:
                a = 1 
            if usr_password[x] in upper_case:
                b = 1 
            if usr_password[x] in numbers:
                c = 1 
            if usr_password[x] in symbols:
                d = 1
        sum=a+b+c+d
        if sum != 4:
            chara = random.choice(lower_case)+random.choice(upper_case)+random.choice(numbers)+random.choice(symbols)+random.choice(upper_case)+random.choice(numbers)
            print('La contraseña no cumple los requisitos de seguridad')
            print('\nSugerencia de contraseña:', chara)
            chara  = ''
            usr_password = input('\ningrese nuevamente: ')
        else:
            print('La contraseña cumple los requisitos de seguridad')


usr_password = input('\nIngrese su contraseña: ')
check_password(usr_password)
