import pygame,sys
from pygame.locals import *

pygame.init()


clock = pygame.time.Clock()
FPS = 60

# App window

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Budget calculator')
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
# Fonts
FONT = pygame.font.SysFont('Arial', 24)

class Input_box():
    """To create a input box is necessary to just input 
    the x and y value for where you want to put the box.
    This class handles the draw, update and events to use
    the box."""
    def __init__(self,x,y,text=''):
        self.rect = pygame.Rect(x,y,75,35)
        self.color = COLOR_INACTIVE
        self.active = False
        self.text = text
        self.FONT = FONT
        self.txt_surface = FONT.render(text,True,self.color)
        
    def handle_event(self, event):
        """Takes the events found in pygame.event.get()
        and handles the mouse click to toogle the active
        state and detect the unicode of the keys pressed
        to write it on the box."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text,True,self.color)

    def update(self):
        """Makes sure that the width of the box fits the
        lenght of the input."""
        width = max(200,self.txt_surface.get_width()+10)
        self.rect.w = width


    def draw(self,screen):
        """Draw the box itself and the text of it on the 
        given srceen"""
        self.txt_surface = FONT.render(self.text,True,self.color)
        screen.blit(self.txt_surface,(self.rect.x+5,self.rect.y+5))
        pygame.draw.rect(screen,self.color,self.rect, 2)

class Button():
    """The button class takes the x and y position of the
    topleft corner for the button and the image to render
    for the button. It also has function to draw itself 
    and to detect if it has been clicked."""
    def __init__(self, x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        """Blit itself into the screen. For this to work
        your display variable has to be named screen."""
        # Draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self):
        """Detects if the mouse position is the same as
        the buttons Rect and returns True or False
        depending if the mouse button 1 has been pressed
        or released. Use this to control what your buttons
        do once they are clicked."""

        action = False

        # Get mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        
        return action

