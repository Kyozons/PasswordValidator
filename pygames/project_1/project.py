import pygame, math, os, sys, random
import data.myEngine as e 
from pygame.locals import *
clock = pygame.time.Clock()

pygame.init()

# Constant
SCREEN_SIZE = (600, 400)

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
pygame.display.set_caption('Primo Project')

display = pygame.Surface((300,200))

# Map
game_map = e.load_map('map')

# Load images
player_image = pygame.image.load('data/images/entities/player/player.png').convert()  # Use convert when need to set transparency to a color
player_image.set_colorkey((255,255,255))  # Make white transparent
dirt_image = pygame.image.load('data/images/dirt.png')
grass_image = pygame.image.load('data/images/grass.png')

# Colliders
player_rect = pygame.Rect(50,163,player_image.get_width(), player_image.get_height())

# Movement variables
moving_right = False
moving_left = False
vertical_momentum = 0
air_time = 0
jumps_remaining = 2
wall_jumps = 0

# Scrolling
true_scroll = [0,0]

while True:  # Game Loop
    display.fill((146,244,255))

    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])


    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x * 16 - scroll[0], y *16 - scroll[1]))
            if tile == '2':
                display.blit(grass_image, (x * 16 - scroll[0], y *16 - scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
            x += 1
        y += 1

    display.blit(player_image, (player_rect.x - scroll[0], player_rect.y - scroll[1]))
    surface = pygame.transform.scale(display, SCREEN_SIZE)
    screen.blit(surface,(0,0))
    
    player_movement = [0 ,0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3

    player_rect, collisions = e.move(player_rect, player_movement, tile_rects)
    display.blit(player_image, (player_rect.x, player_rect.y))

    if collisions['bottom']:
        vertical_momentum = 0
        air_time = 0
        jumps_remaining = 2
        wall_jumps = 0
    else:
        air_time += 1
    if collisions['top']:
        vertical_momentum = 0
    if collisions['left'] or collisions['right']:
        if wall_jumps < 2:
            jumps_remaining += 1
        elif wall_jumps < 2:
            wall_jumps = 2
            jumps_remaining = 0

    if jumps_remaining < 0:
        jumps_remaining = 0
    if jumps_remaining > 2:
        jumps_remaining = 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if collisions['left'] and jumps_remaining > 0:
                    vertical_momentum = -3
                    wall_jumps += 1
                if collisions['right'] and jumps_remaining > 0:
                    vertical_momentum = -3
                    wall_jumps += 1
                if air_time < 7:
                    vertical_momentum = -3
                if jumps_remaining > 0:
                    vertical_momentum = -3
                    jumps_remaining -= 1
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False


    pygame.display.update()
    clock.tick(60)



