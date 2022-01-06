import pygame, sys, os, math, random
from pygame.locals import *
clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Title')

WINDOW_SIZE = (400,400)

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)  # Initiate screen

# Scale for pixel art
display = pygame.Surface((200,200))  # Must be half of (x,y) of WINDOW_SIZE

while True:  # Game loop
    
    for event in pygame.event.get():  # Event handler
        if event.tye == QUIT:
            pygame.quit()
            sys.exti()

    pygame.display.update()  # Show the updated display
    clock.tick(60)  # Maintain 60 fps

