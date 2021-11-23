#Cifrador Cesar
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Quieres encriptar, desencriptar o forzar un mensaje?')
        mode = input().lower()
        if mode in ['encriptar', 'e', 'desencriptar', 'd', 'bruta', 'b']:
            return mode
        else:
            print('Ingresa "encriptar" o "e", "desencriptar" o "d", o "bruta" o "b".')

def getMessage():
    print('Ingresa tu mensaje: ')
    return input()

def getKey():
    key = 0
    while True:
        print('Ingresa el numero de la llave (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1: #Not found in SYMBOLS.
            #Add this symbols without change
            translated += symbol
        else:
            # Encrypt or Decrypt
            symbolIndex += key

            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]
    return translated

mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()
print('Tu texto traducido es: ')
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))


