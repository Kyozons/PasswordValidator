import pygame, sys
from pygame.locals import *

pygame.init()

# Set up the framerate.
clock = pygame.time.Clock()

SCREEN_SIZE = (600, 400)

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
pygame.display.set_caption('Learning Pygame!')

display = pygame.Surface((300, 200))

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# MAP
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','1','1'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

# Collisions
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:  # Is moving right
            rect.right = tile.left  # Player's right side alongside tile leftside
            collision_types['right'] = True
        elif movement[0] < 0:  # Is moving left
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:  # Is falling
            rect.bottom = tile.top
            collision_types['bottom'] = True
        if movement[1] < 0:  # Is jumping
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

# Set up font.
base_font = pygame.font.SysFont('Corbel', 35)

# Set up text.
text = base_font.render('Wena wena!!', True, BLACK, GREEN)
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery

# Images
player_image = pygame.image.load('player.png')
player_image.set_colorkey((255, 255, 255))
grass_image = pygame.image.load('grass.png')
TILE_SIZE = grass_image.get_width()
dirt_image = pygame.image.load('dirt.png')

# Coliders
player_rect = pygame.Rect(50, 50, player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)
second_test_rect = pygame.Rect(120, 250, 50, 100)

# Movement
moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0
jump_count = 0
wall_jump = 0

while True:
    display.fill(( 146, 244, 255) )

    tile_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                display.blit(grass_image, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

            x += 1
        y += 1
        
    display.blit(player_image, (player_rect.x, player_rect.y))
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

    player_rect, collisions= move(player_rect, player_movement, tile_rects)
    display.blit(player_image, (player_rect.x, player_rect.y))

    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
        jump_count = 0
    else:
        air_timer += 1
    if collisions['top']:
        player_y_momentum = 0
    if collisions['left'] or collisions['right']:
        air_timer = 0
        wall_jump += 1
    

    # Event Handling
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
                if air_timer < 7:
                    player_y_momentum = -3
                if jump_count < 2:
                    player_y_momentum = -3
                    jump_count += 1
                if wall_jump < 2:
                    player_y_momentum = -3
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False


    pygame.display.update()
    clock.tick(60)  # Maintain 60 fps
