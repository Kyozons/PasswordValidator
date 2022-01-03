import pygame, sys
from pygame.locals import *

pygame.init()

# Set up the framerate.
clock = pygame.time.Clock()

SCREEN_SIZE = (400, 400)

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
pygame.display.set_caption('Learning Pygame!')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up font.
base_font = pygame.font.SysFont('Corbel', 35)

# Set up text.
text = base_font.render('Wena wena!!', True, BLACK, GREEN)
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery

# Create "player"
player_location = [40, 40]
player_image = pygame.image.load('player.png')

# Coliders
player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100, 100, 100, 50)
second_test_rect = pygame.Rect(120, 250, 50, 100)

# Movement
moving_right = False
moving_left = False
jumping = False

player_y_momentum = 0

while True:
    screen.fill(( 146, 144, 255) )

    screen.blit(player_image, player_location)

    player_y_momentum += 0.2

    if moving_right:
        player_location[0] += 4
    if moving_left:
        player_location[0] -= 4
    player_location[1] += player_y_momentum


    # Update player collider with player position:
    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    # Check for collitions:

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
                jumping == True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_UP:
                jumping == False


    pygame.display.update()
    clock.tick(60)  # Maintain 60 fps
