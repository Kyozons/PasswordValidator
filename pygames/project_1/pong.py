try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from data import myEngine as e
    from socket import *
    from pygame.locals import *
except ImportError as err:
    print(f'No se pudo importar {err}')
    sys.exit(2)
    
pygame.init()

SCREEN_SIZE = (600,400)

screen = pygame.display.set_mode((SCREEN_SIZE), 0,32)

display = pygame.Surface((300,200))

coin_image, coin_rect = e.load_image('data/images', 'coin.png', 0,0)
coin_image.set_colorkey((255,255,255))

player_image, player_rect = e.load_image('data/images/entities/player', 'player.png',50,50)
player_image.set_colorkey((255,255,255))


vertical_momentum = 0
while True:
    
    display.fill((146,244,255))
    vertical_momentum += 0.2
    
    display.blit(coin_image, coin_rect)
    
    display.blit(player_image, player_rect)
    
    surface = pygame.transform.scale(display, SCREEN_SIZE)
    screen.blit(surface,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
    