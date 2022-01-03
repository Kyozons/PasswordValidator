# Setup:
import pygame, sys
# Setup pygame/screen:
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('Learning Physics')
screen = pygame.display.set_mode((500, 500), 0, 32)

player = pygame.Rect(100, 100, 80, 40)

tiles = [pygame.Rect(200,350,50,50),pygame.Rect(260,450,50,50)]

def collision_test(rect, tiles):
    '''Function that test collisions with rect 
    (collider you are testing) against the tiles you want
    to see if its colliding with.

    It takes the tiles and append to a list the ones that 
    collides with the given rect and return that list.'''

    collisions = []
    for tile in tiles:
        if rect.colliderect(tile):
            collisions.append(tile)
    return collisions

def move(rect, movement, tiles):
    '''Function that takes the rect you want to move,
    the movement you want it to make as a list [x, y]
    and the tiles that it collides with.

    Test the collisions on X axis first and sets
    the right side of the rect to de left side of
    the tile that is colliding with if moving to
    the right, vice versa if moving to the left.

    Then Test for the Y axis and set the bottom
    of the rect to the top of the tile that collides
    with if hitting from above, vice versa if hitting
    from below.
    
    This is to set the possition correctly for the rect that we are moving.

    Return the rect. '''


    rect.x += movement[0]
    collisions = collision_test(rect, tiles)
    collisions_dict = {'right': False, 'left': False, 'bottom': False, 'top': False}
    for tile in collisions:
        if movement[0] > 0:
            rect.right = tile.left
            collisions_dict['right'] = True
        if movement[0] < 0:
            rect.left = tile.right
            collisions_dict['left'] = True
    rect.y += movement[1]
    collisions = collision_test(rect, tiles)
    for tile in collisions:
        if movement[1] > 0:
            rect.bottom = tile.top
            collisions_dict['bottom'] = True
        if movement[1] < 0:
            rect.top = tile.bottom
            collisions_dict['top'] = True
    return rect, collisions_dict

moving_left = False
moving_right = False
moving_up = False
moving_down = False
   



# Game Loop:
while True:

    # Clear Display
    screen.fill((0,0,0))

    movement = [0, 0]
    if moving_right:
        movement[0] += 5
    if moving_left:
        movement[0] -= 5
    if moving_up:
        movement[1] -= 5
    if moving_down:
        movement[1] += 5

    player, collisions_dict= move(player, movement, tiles)

    pygame.draw.rect(screen, (255,255,255), player)

    for tile in tiles:
        pygame.draw.rect(screen,(255,0,0),tile)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_DOWN:
                moving_down = True
            if event.key == K_UP:
                moving_up = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_DOWN:
                moving_down = False
            if event.key == K_UP:
                moving_up = False

    # Update display
    pygame.display.update()
    mainClock.tick(60)
