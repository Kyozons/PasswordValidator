import pygame, os, sys
from data import myEngine as e
from pygame.locals import *

def main():
    pygame.init()

    screen_width = 600
    screen_height = 400

    tile_size = 16
    display = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Platformer')

    # display = pygame.Surface((600,400))
    # Load Images
    bg_img = pygame.image.load('data/images/background/layer1.png').convert()
    bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))

    midg_img = pygame.image.load('data/images/background/layer2.png').convert()
    midg_img = pygame.transform.scale(midg_img,(screen_width,screen_height))
    midg_img.set_colorkey((255,255,255))




    #Game map
    game_map = e.load_map('map')
    

   
    world = e.World(game_map,tile_size,display)


    while True:
        
        display.blit(bg_img,(0,0))
        display.blit(midg_img,(0,100))
        world.draw()


        # surface = pygame.transform.scale(display, (screen_width,screen_height))

        # screen.blit(surface,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main()
