#! python3
# comicDwnld.py Descarga todos los comics de XKCD

import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # Descargar la página
    print('Descargando página %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Encuentra y descarga la imagen del comic
    comic_elem = soup.select('#comic img')
    if comic_elem == []:
        print('No se encontraron imágenes de cómic.')
    else:
        comic_url = 'https:' + comic_elem[0].get('src')
        print('Descargando la imagen %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # Guardar la imagen en ./xkcd
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # Buscar la url del boton "anterior"
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print('Terminado.')
