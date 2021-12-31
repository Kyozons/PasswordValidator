import random

def guess_the_number():

    secret_number = random.randint(1, 20)
    print('Estoy pensando en un numero entre 1 y 20.')

    # 6 intentos para adivinar
    for guessesTaken in range(1, 7):
        print('Intenta adivinar:')
        guess = int(input())

        if guess < secret_number:
            print('Prueba un número más grande')

        elif guess > secret_number:
            print('Prueba un número más pequeño')

        else:
            break # Esta condición significa que adivinó

    if guess == secret_number:
        print('Adivinaste! Y te tomó {} intentos.'.format(guessesTaken))
    else:
        print('No adivinaste, el número era {}.'.format(secret_number))





if __name__ == '__main__':
    guess_the_number()

