import re, pyperclip

email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+           # Usuario
@                           # Símbolo @
[a-zA-Z0-9._]+              # Dominio correo
(\.[a-zA-Z]{2,4})           # .com .net .co etc 
)''', re.VERBOSE)


current_clipboard = str(pyperclip.paste()) 

matches = []

# Agregar a la lista "matches" todo el texto que corresponda a los criterios de emali_regex
for groups in email_regex.findall(current_clipboard):
    matches.append(groups[0])

# Copiar resultados al portapapeles

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Se copió al portapapeles: ')
    print('\n'.join(matches))
else:
    print('No se encontro texto que concuerde con dirección de correo')
    

