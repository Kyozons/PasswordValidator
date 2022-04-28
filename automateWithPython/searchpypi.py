#! python3
# searchpypi.py - Abre varios resultados de busqueda

import requests, sys, webbrowser, bs4

print('Buscando...') # Muestra texto mientras realiza la busqueda
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Obtener los primeros resultados
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Abrir una pestaña de navegador por cada resultado
linkElems = soup.select('.package-snippet')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Abriendo', urlToOpen)
    webbrowser.open(urlToOpen)
