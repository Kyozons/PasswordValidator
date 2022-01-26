import pygame, sys
from pygame.locals import *
from data import objects as o

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# App window

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Calculadora Presupuesto')
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
# Fonts
FONT = pygame.font.SysFont('Arial', 24)

# Game variables
savings= six_months_safe= months_to_save_for= spents = 0

# Output text
def draw_text(text,FONT,text_color,x,y):
    inpt_text = FONT.render(text,True,text_color)
    screen.blit(inpt_text,(x,y))



def calc_bugdet(income,spents):
    income_value = 0
    spents_value = 0
    income_value = int(income.text)
    spents_value = spents
    
    savings = income_value - spents_value

    six_months_safe = spents_value * 6

    months_to_save_for = int(six_months_safe / savings)

    return savings, six_months_safe, months_to_save_for



# Images
clear_btn_image = pygame.image.load('data/clear_btn.png').convert()
sum_btn_image = pygame.image.load('data/suma_btn.png').convert()
# Init buttons
sum_btn = o.Button(screen.get_rect().right-90,450,sum_btn_image)
clear_btn = o.Button(screen.get_rect().right-180,450,clear_btn_image)

# Init text boxes
income_box = o.Input_box(140,32)
income_box.rect.centerx = screen.get_rect().centerx
food_amount_box = o.Input_box(screen.get_rect().right-210,200)
transport_amount_box = o.Input_box(screen.get_rect().right-210,245)
bills_amount_box = o.Input_box(screen.get_rect().right-210,290)
entretainment_amount_box = o.Input_box(screen.get_rect().right-210,335)
emergency_amount_box = o.Input_box(screen.get_rect().right-210,380)
input_boxes = [income_box,food_amount_box,transport_amount_box,bills_amount_box,entretainment_amount_box,emergency_amount_box]


while True:
    clock.tick(FPS)

    # Draw background
    screen.fill((30,30,30))

    # Draw Buttons
    sum_btn.draw()
    clear_btn.draw()

    # Draw boxes and text 
    draw_text('Ingreso: ',FONT,(255,255,255),income_box.rect.left-100,income_box.rect.centery-10)
    draw_text('Categoria',FONT,(255,255,255),screen.get_rect().left+100,food_amount_box.rect.top-40)
    draw_text('Monto',FONT,(255,255,255),food_amount_box.rect.centerx-40,food_amount_box.rect.top-40)
    draw_text('Comida',FONT,COLOR_INACTIVE,screen.get_rect().left+10,food_amount_box.rect.centery-10)
    draw_text('Transporte',FONT,COLOR_INACTIVE,screen.get_rect().left+10,transport_amount_box.rect.centery-10)
    draw_text('Cuentas',FONT,COLOR_INACTIVE,screen.get_rect().left+10,bills_amount_box.rect.centery-10)
    draw_text('Entretenimiento',FONT,COLOR_INACTIVE,screen.get_rect().left+10,entretainment_amount_box.rect.centery-10)
    draw_text('Emergencia',FONT,COLOR_INACTIVE,screen.get_rect().left+10,emergency_amount_box.rect.centery-10)
    draw_text(f'Con tus ingresos de ${income_box.text}',FONT,(255,255,255),screen.get_rect().left+10,500)

    for box in input_boxes:
        box.update()
        box.draw(screen)
   # Buttons control
    if clear_btn.is_clicked():
        for box in input_boxes:
            box.text = ''
    if sum_btn.is_clicked():
        def spents(input_boxes):
            spents = 0
            for box in input_boxes[1:]:
                spents += int(box.text)
            return spents
        spents = spents(input_boxes)
        savings, six_months_safe, months_to_save_for = calc_bugdet(income_box,spents)

    draw_text(f'Estas gastando ${spents} al mes',FONT,(255,255,255),screen.get_rect().left+10,530)
    draw_text(f'Lo que significa que debes ahorrar ${six_months_safe}',FONT,(255,255,255),screen.get_rect().left+10,570)
    draw_text(f'para vivir seis meses sin preocupaciones',FONT,(255,255,255),screen.get_rect().left+10,590)
    draw_text(f'Si ahorras los ${savings} restantes',FONT,(255,255,255),screen.get_rect().left+10,630)
    draw_text(f'Puedes alcanzar ese monto en {months_to_save_for} Meses',FONT,(255,255,255),screen.get_rect().left+10,650)

    # Event handler
    for event in pygame.event.get():
        # Quit App
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for box in input_boxes:
            box.handle_event(event)
 

    pygame.display.update()


