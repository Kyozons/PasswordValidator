import pygame, math, os, sys, random

def load_map(path):
    '''Takes a string with the name of the map to load.
    returns a list of lists with the map info to render
    the tiles.'''
    with open(path + '.txt', 'r') as f:

        data = f.read()
        data = data.split('\n')
        game_map = []
        for row in data:
            game_map.append(list(row))
        return game_map


def collision_test(rect, tiles):
    '''Test the given collider(Rect object) against the 
    tiles and return a list for every tile that hits.'''
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list


def move(rect, movement, tiles):
    '''Takes the collider(Rect object) that want to move, 
    the movement that you want to apply and the tiles 
    list of your game.Then returns the collider with the 
    new coordinates to move and the type of collision that
    it makes with that movement.'''
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


def load_image(path,filename,x,y):
    """Takes the path and filename of the image to load 
    and return the image object and image rect.
    The x and y arguments are for setting the initial
    position of the image."""
    fullname = os.path.join(path, filename)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
        image_rect = image.get_rect()
        image_rect.x = x
        image_rect.y = y
    except pygame.error as message:
        print('No se pudo cargar la imagen ', fullname)
        raise SystemExit(message)
    return image, image_rect
    
    

   