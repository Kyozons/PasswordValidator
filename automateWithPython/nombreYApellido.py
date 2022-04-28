import re, pyperclip

nombres = re.compile(r'''(
[a-zA-Z]+           # Primer Nombre
(\s)                # Espacio
[a-zA-Z]+           # Segundo Nombre
(\s)                # Espacio
)''', re.VERBOSE)

current_clipboard = str(pyperclip.paste())

names_matches = []
last_name_matches = []

for groups in nombres.findall(current_clipboard):
    names_matches.append(groups[0])

for groups in nombres.findall(current_clipboard):
    last_name_matches.append(groups[2])
if len(names_matches) > 0:
    pyperclip.copy('\n'.join(names_matches))
    print('Se copió al portapapeles: \n')
    print('\n'.join(names_matches))
    print('\n'.join(last_name_matches))
    print('')
else:
    print('No se encuentran coincidencias')
