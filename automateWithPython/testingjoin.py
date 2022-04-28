import sys, webbrowser, requests, bs4

print('Buscando...')
url_to_open = 'https://amazon.com/s?k=' + '+'.join(sys.argv[1:]) + '&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=305LTI8V4J0OZ&sprefix=asus%2Caps%2C256&ref=nb_sb_noss_1'



webbrowser.open(url_to_open)
sys.exit()
