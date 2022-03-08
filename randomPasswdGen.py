import random
lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers    = '123456789'
symbols    = '!#$%&.-_'

characters = {
    'lower_case' : 'abcdefghijklmnopqrstuvwxyz',
    'upper_case' : 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'numbers'    : '123456789',
    'symbols'    :'!#$%&.-_',
}

new_passwd = []
for i in range(2):
    for chara in characters:
        new_passwd += characters[chara][random.randint(0,len(characters[chara])-1)]
        
random.shuffle(new_passwd)

print(''.join(new_passwd))
