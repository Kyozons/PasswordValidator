import pygame, sys, os, random
from pygame.locals import *
clock = pygame.time.Clock()

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.set_num_channels(64)


# Constants
SCREEN_SIZE = (600, 400)

screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
pygame.display.set_caption('Learning Pygame')

display = pygame.Surface((300, 200))

# Map
CHUNK_SIZE = 8
def generate_chunks(x,y):
    chunk_data = []
    for y_pos in range(CHUNK_SIZE):
        for x_pos in range(CHUNK_SIZE):
            target_x = x * CHUNK_SIZE + x_pos
            target_y = y * CHUNK_SIZE + y_pos
            tile_type = 0 # Air / Nothing
            if target_y > 10:
                tile_type = 2 # Dirt
            elif target_y == 10:
                tile_type = 1 # Grass
            elif target_y == 9:
                if random.randint(1,5) == 1:
                    tile_type = 3 # Plant
            if tile_type != 0:
                chunk_data.append([[target_x,target_y],tile_type])
    return chunk_data

game_map = {}

# Sounds
jump_sound = pygame.mixer.Sound('platformer_project_3/jump.wav')
jump_sound.set_volume(0.2)
grass_sounds = [pygame.mixer.Sound('platformer_project_3/grass_0.wav'),pygame.mixer.Sound('platformer_project_3/grass_1.wav')] 
grass_sounds[0].set_volume(0.2)
grass_sounds[1].set_volume(0.2)
# Music
pygame.mixer.music.load('platformer_project_3/music.wav')
pygame.mixer.music.play(-1)

# Animations

global animation_frames
animation_frames = {}

def load_animations(path, frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame
animation_database = {}

animation_database['run'] = load_animations('player_animations/run',[7,7])
animation_database['idle']= load_animations('player_animations/idle',[7,7,40])
animation_database['jump'] = load_animations('player_animations/jump', [2,5,8,2])

player_action = 'idle'
player_frame = 0
player_flip = False

grass_sounds_timer = 0



# Load images
dirt_image = pygame.image.load('platformer_project_3/dirt.png')
grass_image = pygame.image.load('platformer_project_3/grass.png')
plant_image = pygame.image.load('platformer_project_3/plant.png').convert()
plant_image.set_colorkey((255,255,255))

tile_index = {1:grass_image, 
              2:dirt_image,
              3:plant_image,
              }
background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

TILE_SIZE = grass_image.get_width()

# Colliders
player_rect = pygame.Rect(100,100,5,13)

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
jumps_remaining = 2
wall_jumps = 0

# Scrolling
true_scroll = [0,0]



while True:
    display.fill((146,244,255))
    
    if grass_sounds_timer > 0:
        grass_sounds_timer -= 1

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
    # Tile rendering
    for y in range (3):
        for x in range(4):
            target_x = x - 1 + int(round(scroll[0]/(CHUNK_SIZE*16)))
            target_y = y - 1 + int(round(scroll[1]/(CHUNK_SIZE*16)))
            target_chunk = str(target_x) + ';' + str(target_y)
            if target_chunk not in game_map:
                game_map[target_chunk] = generate_chunks(target_x, target_y)
            for tile in game_map[target_chunk]:
                display.blit(tile_index[tile[1]], (tile[0][0]*16-scroll[0],tile[0][1]*16-scroll[1]))
                if tile[1] in [1,2]:
                    tile_rects.append(pygame.Rect(tile[0][0]*16,tile [0][1]*16,16,16))
                
    
    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0
    player_img_id = animation_database[player_action][player_frame]
    player_img = animation_frames[player_img_id]
    
    display.blit(pygame.transform.flip(player_img, player_flip, False), (player_rect.x-scroll[0], player_rect.y-scroll[1]))
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
        
    if player_movement[0] > 0:
        player_action, player_frame = change_action(player_action, player_frame, 'run')
        player_flip = False
    if player_movement[0] == 0:
        player_action, player_frame = change_action(player_action, player_frame, 'idle')
    if player_movement[0] < 0:
        player_action, player_frame = change_action(player_action, player_frame, 'run')
        player_flip = True  

         
        
    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    display.blit(player_img, (player_rect.x, player_rect.y))

    if collisions['bottom']:
        player_y_momentum = 0
        air_time = 0
        jumps_remaining = 2
        wall_jumps = 0
        if player_movement[0] != 0:
            if grass_sounds_timer == 0:
                grass_sounds_timer = 30
                random.choice(grass_sounds).play()
    else:
        air_time += 1
    if collisions['top']:
        player_y_momentum = 0
    if collisions['left'] or collisions['right']:
        if wall_jumps < 2:
            jumps_remaining += 1
        elif wall_jumps > 2:
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
            if event.key == K_w:
                pygame.mixer.music.fadeout(1000)
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                if collisions['left'] and jumps_remaining > 0:
                    player_y_momentum = -3
                    wall_jumps += 1
                    jump_sound.play()
                if collisions['right'] and jumps_remaining > 0:
                    player_y_momentum = -3
                    wall_jumps += 1
                    jump_sound.play()
                if air_time < 7:
                    player_y_momentum = -3
                    jump_sound.play()
                if jumps_remaining > 0:
                    player_y_momentum = -3
                    jumps_remaining -= 1
                    jump_sound.play()
                
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False



    pygame.display.update()
    clock.tick(60)
