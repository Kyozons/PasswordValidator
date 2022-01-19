import pygame
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Game Window
TILE_SIZE = 16
COLS = 38
ROWS = 25
MARGIN = 100
SCREEN_WIDTH = TILE_SIZE * COLS
SCREEN_HEIGHT = (TILE_SIZE * ROWS) + MARGIN

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Level Editor')


# Load Images
dirt_img = pygame.image.load('img/dirt.png').convert()
grass_img = pygame.image.load('img/grass.png').convert()
coin_img = pygame.image.load('img/coin.png').convert()
coin_img.set_colorkey((255,255,255))
save_img = pygame.image.load('img/save_btn.png').convert()
load_img = pygame.image.load('img/load_btn.png').convert()
bg1_img = pygame.image.load('img/layer1.png').convert()
bg1_img = pygame.transform.scale(bg1_img,(SCREEN_WIDTH, SCREEN_HEIGHT))
bg2_img = pygame.image.load('img/layer2.png').convert()
bg2_img = pygame.transform.scale(bg2_img,(SCREEN_WIDTH, SCREEN_HEIGHT))
bg2_img.set_colorkey((255,255,255))
clear_img = pygame.image.load('img/clear_btn.png').convert()



# Game variables
clicked = False
level = 1
TOTAL_TILES_IMG = 3
tile_type = 0

# Colours
WHITE = (255,255,255)
GREEN = (144,201,120)

# Fonts
font = pygame.font.SysFont('Futura',24)

# Create empty tile list
world_data = []
def empty_world_data():
    for row in range(ROWS):
        r = [0] * COLS
        world_data.append(r)
    # Screen borders
    for tile in range(0,COLS):
        world_data[ROWS-1][tile] = 2
        world_data[0][tile] = 1
    for row in range(0,ROWS):
        world_data[row][0] = 1
        world_data[row][COLS-1] = 1
empty_world_data()

# Clear screen
def clear_screen():
    world_data.clear()
    empty_world_data()

# output text
def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))


def draw_grid():
    for c in range(COLS+1):
        # vertical lines:
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE, 0), (c * TILE_SIZE, SCREEN_HEIGHT - MARGIN))
    for r in range(ROWS+1):
        # horizontal lines:
        pygame.draw.line(screen, WHITE, (0, r * TILE_SIZE), (SCREEN_WIDTH, r * TILE_SIZE))


def draw_world():
    for row in range(ROWS):
        for col in range(COLS):
            if world_data[row][col] == 1:
                # dirt blocks
                img = pygame.transform.scale(dirt_img, (TILE_SIZE, TILE_SIZE))
                screen.blit(img, (col * TILE_SIZE, row * TILE_SIZE))
            if world_data[row][col] == 2:
                # grass blocks
                img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))
                screen.blit(img, (col * TILE_SIZE, row * TILE_SIZE))
            if world_data[row][col] == 3:
                # coins
                img = pygame.transform.scale(coin_img, (TILE_SIZE, TILE_SIZE))
                screen.blit(img, (col * TILE_SIZE, row * TILE_SIZE))

class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        # Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self):
        action = False

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Ceck mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        
        return action




# Create load and save buttons
save_button = Button(SCREEN_WIDTH // 2 + 220, SCREEN_HEIGHT - 100, save_img)
load_button = Button(SCREEN_WIDTH // 2 + 220, SCREEN_HEIGHT - 57, load_img)
clear_button = Button(SCREEN_WIDTH // 2 + 139, SCREEN_HEIGHT - 57, clear_img)
dirt_button = Button(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 80, pygame.transform.scale(dirt_img,(TILE_SIZE * 2, TILE_SIZE * 2)))
grass_button = Button(SCREEN_WIDTH // 2 - 18, SCREEN_HEIGHT - 80, pygame.transform.scale(grass_img,(TILE_SIZE * 2, TILE_SIZE * 2)))
coin_button = Button(SCREEN_WIDTH // 2 + 14, SCREEN_HEIGHT - 80, pygame.transform.scale(coin_img,(TILE_SIZE * 2, TILE_SIZE * 2)))

# Main game loop
while True:
    clock.tick(FPS)

    # Draw background
    
    screen.blit(bg1_img,(0,0))
    screen.blit(bg2_img, (0,100))
    pygame.draw.rect(screen,GREEN,(0,SCREEN_HEIGHT - 100,SCREEN_WIDTH,SCREEN_HEIGHT-MARGIN))
    save_button.draw()
    load_button.draw()
    clear_button.draw()
    dirt_button.draw()
    grass_button.draw()
    coin_button.draw()

    # Buttons control
    if dirt_button.is_clicked():  # Paint a dirt tile
        tile_type = 1
    if grass_button.is_clicked():  # Paint a grass tile
        tile_type = 2
    if coin_button.is_clicked():  # Paint a coin tile
        tile_type = 3
    # Clear lvl
    if clear_button.is_clicked():  # Set all the tiles to 0
        clear_screen()

    # load and save lvl
    if save_button.is_clicked():
        # save level data:
        pickle_out = open(f'level{level}_data','wb')
        pickle.dump(world_data,pickle_out)
        pickle_out.close()
    if load_button.is_clicked():
        # load in level data
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)

    # Show the grid and the level tiles
    draw_grid()
    draw_world()
    
    # Text showing current level
    draw_text(f'Level: {level}',font, WHITE, TILE_SIZE, SCREEN_HEIGHT - 60 )

    # Event handler
    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
        
        # Mouse Click to change tiles:
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
            pos = pygame.mouse.get_pos()
            x = pos[0] // TILE_SIZE
            y = pos[1] // TILE_SIZE
            # Check that the coordinates are within the tile area
            if x < COLS and y < ROWS:
                # Left click draw tile on place
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] = tile_type
                # Right click "delete" tile
                if pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] = 0
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
        # Hold click to keep "painting" with tiles
        if event.type == pygame.MOUSEMOTION and clicked == True:
            pos = pygame.mouse.get_pos()
            x = pos[0] // TILE_SIZE
            y = pos[1] // TILE_SIZE
            # Check that the coordinates are within the tile area
            if x < COLS and y < ROWS:
                if pygame.mouse.get_pressed()[0] == 1:
                    world_data[y][x] = tile_type
                if pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] = 0

            # Up and down keys to change level number
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tile_type = 0
            if event.key == pygame.K_c:
                clear_screen()
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN and level > 1:
                level -= 1

    pygame.display.update()
