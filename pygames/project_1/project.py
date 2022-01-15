import pygame, math, os, sys, random
import data.myEngine as e 
from pygame.locals import *
def main():
    clock = pygame.time.Clock()
    
    pygame.init()
    
    # Constant
    SCREEN_SIZE = (600, 400)
    # screen = pygame.display.set_mode((SCREEN_SIZE), 0, 32)
    
    bits = 0
    modes = pygame.display.list_modes(bits)
    if not modes:
        print(f'{bits}-bit not supported')
    else:
        screen = pygame.display.set_mode((SCREEN_SIZE), 0, bits)
    pygame.display.set_caption('Primo Project')
    
    display = pygame.Surface((300,200))
    
    # Map
    game_map = e.load_map('map')
    
    # Load images
    player_image = pygame.image.load('data/images/entities/player/player.png').convert()  # Use convert when need to set transparency to a color
    player_image.set_colorkey((255,255,255))  # Make white transparent
    dirt_image = pygame.image.load('data/images/dirt.png')
    grass_image = pygame.image.load('data/images/grass.png')
    coin_image = pygame.image.load('data/images/coin.png').convert()
    coin_image.set_colorkey((255,255,255))
    layer1_image = pygame.image.load('data/images/background/layer1.png').convert()
    layer1_image.set_colorkey((255,255,255))
    layer2_image = pygame.image.load('data/images/background/layer2.png').convert()
    layer2_image.set_colorkey((255,255,255))
    layer3_image = pygame.image.load('data/images/background/layer3.png').convert()
    layer3_image.set_colorkey((255,255,255))
    
    player_flip = False
    # Text
    bottom_font = pygame.font.SysFont('Corbel', 15)
    win_font = pygame.font.SysFont('Corbel', 35)
    win_text = win_font.render('Ganaste!', True, (0,0,0))
    win_text_rect = win_text.get_rect()
    
    bottom_text = bottom_font.render('Presiona R para jugar nuevamente ESC para salir', True, (0,0,0))
    bottom_text_rect = bottom_text.get_rect()    
    
    score_font = pygame.font.SysFont('Corbel', 15)
    # Coins
    coins_to_win = 5
    coins_collected = 0
    # Colliders
    player_rect = pygame.Rect(30,323,player_image.get_width(), player_image.get_height())
    layer1_rect = pygame.Rect(0,0,layer1_image.get_width(), layer1_image.get_height())
    # Movement variables
    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_time = 0
    jumps_remaining = 2
    wall_jumps = 0
    
    # Scrolling
    true_scroll = [0,0]
    
    # Background Objects
    background_objects = [[0.25,[250,120,50,150]],[0.25,[100,150,120,150]],[0.5,[10,200,100,200]],[0.5,[50,90,150,50]]]
    
    
    coin_rects = []
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '3':
                coin_rects.append(pygame.Rect(x * 16, y * 16, 5, 4))
            x += 1
        y += 1
    while True:  # Game Loop
        display.fill((146,244,255))
        
        jumps_remaining = 2
        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])
        
      
        # pygame.draw.rect(display,(30,90,50),pygame.Rect(0-scroll[0]*0.25,130-scroll[1]*0.25,300,70))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
            if background_object[0] == 0.5:
                pass
                # pygame.draw.rect(display,(50,10,222),obj_rect)
            else:
                pass
                # pygame.draw.rect(display,(30,40,90),obj_rect)
        
        
        
        # print(player_rect) 
    
    
        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    display.blit(dirt_image, (x * 16 - scroll[0], y *16 - scroll[1]))
                if tile == '2':
                    display.blit(grass_image, (x * 16 - scroll[0], y *16 - scroll[1]))
                if tile != '0' and tile != '3':
                    tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
                x += 1
            y += 1
        
        
    
        for coin in coin_rects[:]:
            if player_rect.colliderect(coin):
                coin_rects.remove(coin)
                coins_collected += 1
                
        score_text = score_font.render(f'Puntaje: {coins_collected}', True, (0,0,0))
        score_text_rect = score_text.get_rect()
        score_text_rect.topleft = display.get_rect().topleft
        display.blit(score_text, score_text_rect)
        for coin in coin_rects:
            display.blit(coin_image, (coin.x - scroll[0], coin.y - scroll[1]))
            
        win_text_rect.centerx = display.get_rect().centerx
        win_text_rect.centery = display.get_rect().centery
        bottom_text_rect.centerx = win_text_rect.centerx
        bottom_text_rect.centery = win_text_rect.bottom

        if 763 >= player_rect.x >= 755 and 355 >= player_rect.y >= 352 and coins_collected == coins_to_win:
            moving_left = False
            moving_right = False
            jumps_remaining = 0
            vertical_momentum = 0
            display.blit(win_text, win_text_rect)
            display.blit(bottom_text, bottom_text_rect)
            
        display.blit(pygame.transform.flip(player_image, player_flip, False), (player_rect.x-scroll[0], player_rect.y-scroll[1]))
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
        
        
        if player_movement[0] > 0:
            player_flip = False
        if player_movement[0] < 0:
            player_flip = True

        
        player_rect, collisions = e.move(player_rect, player_movement, tile_rects)
        
        
            
            
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
                if event.key == K_r:
                    main()
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = True
                if event.key == K_UP or event.key == K_w:
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
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = False
            if event.type == MOUSEBUTTONUP:
                player_rect.x = 752
                player_rect.y = 352
                    
                    
        pygame.display.update()
        clock.tick(60)
main()
    
