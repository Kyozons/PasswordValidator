import pygame, sys, os
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

# Constants
SCREEN_SIZE = (600, 400)

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
pygame.display.set_caption('Title')

display = pygame.Surface((300, 200))

# Map
def load_map(path):
    with open(path + '.txt', 'r') as f:

        data = f.read()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map
game_map = load_map('map')
# Load images
player_image = pygame.image.load(os.path.join('player.png'))
player_image.set_colorkey(( 255,255,255 ))  # Make white transparent
dirt_image = pygame.image.load(os.path.join('dirt.png'))
grass_image = pygame.image.load(os.path.join('grass.png'))


background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

TILE_SIZE = grass_image.get_width()

# Colliders
player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())

# Collisions
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_type = {'right': False, 'left': False, 'top': False, 'bottom': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_type['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collision_type['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_type['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collision_type['top'] = True
    return rect, collision_type
# Movement
moving_right = False
moving_left = False
player_y_momentum = 0
air_time = 0
jump_count = 0

# Scrolling
true_scroll = [0,0]



while True:
    display.fill((146,244,255))

    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    pygame.draw.rect(display, (7,80,75), pygame.Rect(0,120,300,80))
    for background_object in background_objects:
        obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0], background_object[1][1]-scroll[1]*background_object[0], background_object[1][2], background_object[1][3])
        if background_object[0] == 0.5:
            pygame.draw.rect(display, (14,222,150), obj_rect)
        else:
            pygame.draw.rect(display, (9,91,85), obj_rect)


    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE-scroll[0], y * TILE_SIZE-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
    

    display.blit(player_image, (player_rect.x-scroll[0], player_rect.y-scroll[1]))
    surface = pygame.transform.scale(display, SCREEN_SIZE)
    screen.blit(surface, (0, 0))
    player_movement = [0, 0]
    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3

    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    display.blit(player_image, (player_rect.x, player_rect.y))

    if collisions['bottom']:
        player_y_momentum = 0
        air_time = 0
        jump_count = 0
    else:
        air_time += 1
    if collisions['top']:
        player_y_momentum = 0
    if collisions['left'] or collisions['right']:
        air_time = 0



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
                if air_time < 7 and jump_count < 2:
                    player_y_momentum = -3
                    jump_count += 1
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_UP:
                wall_jump = 1



    pygame.display.update()
    clock.tick(60)
