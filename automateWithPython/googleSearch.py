#!/usr/bin/python3
# Script para buscar y abrir resultados de google automaticamente

import sys, bs4, requests, webbrowser

res = requests.get('https://google.com/search?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.l')
print(soup)

num_open = min(3, len(link_elems))
for i in range(num_open):
    url_to_open = 'https://google.com' + link_elems[i].get('href')
    print('Abriendo', url_to_open)
    webbrowser.open(url_to_open)


