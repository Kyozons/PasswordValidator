def add(number):
    return lambda a : a + number

def subs(number):
    return lambda a : a - number

def mult(number):
    return lambda a : a * number

def div(number):
    return lambda a : a / number
def select_operation():

    print('Select operation: ')
    print('''
            1. Add
            2. Substract
            3. Multiply
            4. Divide''')
    return input()

while True:
    operation = select_operation()
    if operation == '1' or operation == 'Add':
        print('First Number: ')
        fnumber = int(input())
        print('Second Nmuber: ')
        snumber = int(input())
        lnumber = add(snumber) 
        print('Result: ')
        res = lnumber(fnumber)
        print('%s + %s = %s' %(fnumber,snumber, res))
        print('Volver a calcular? ')
        if not input().lower().startswith('s'):
            break

    elif operation == '2' or operation == 'Substract':
        print('First Number: ')
        fnumber = int(input())
        print('Second Nmuber: ')
        snumber = int(input())
        print('Result: ')
        lnumber = subs(snumber) 
        res = lnumber(fnumber)
        print('%s - %s = %s' %(fnumber,snumber, res))
        print('Volver a calcular? ')
        if not input().lower().startswith('s'):
            break

    elif operation == '3' or operation == 'Multiply':
        print('First Number: ')
        fnumber = int(input())
        lnumber = mult(fnumber) 
        print('Second Nmuber: ')
        snumber = int(input())
        print('Result: ')
        res = lnumber(snumber)
        print('%s * %s = %s' %(fnumber,snumber, res))
        print('Volver a calcular? ')
        if not input().lower().startswith('s'):
            break

    elif operation == '4' or operation == 'Divide':
        print('First Number: ')
        fnumber = int(input())
        print('Second Nmuber: ')
        snumber = int(input())
        print('Result: ')
        lnumber = div(snumber) 
        res = lnumber(fnumber)
        print('%s / %s = %s' %(fnumber,snumber, res))
        print('Volver a calcular? ')
        if not input().lower().startswith('s'):
            break
    

        

