#!/usr/bin/env python3

import pygame

# Definimos las constantes
BLACK = (0, 0, 0)
RED = (220, 22, 22)
GREEN = (52, 220, 22)
WHITE = (255, 255, 255)
YELLOW = (240, 229, 48)
BROWN = (128, 60, 34)

RECT_HISTORIC_EXTERNAL = {
     "x": 680,
     "y": 430,
     "width": 560,
     "heigth": 120
}

RECT_HISTORIC_INNER = {
     "x": 696,
     "y": 446,
     "width": 528,
     "heigth": 84
}

CELL_Y_POSITIONS = {
    BLACK: 450,
    GREEN: 470,
    RED: 490
}

CELL_X_START = 1180

CELL_SIZE = 40
CELL_HALF_SIZE = 20

LINE_WIDTH = 4

LIST_MAX_SIZE = 13

TITLE_TEXT = "HISTORIC"
TITLE_TEXT_POSITION = (960, 400)

BORDER_RADIUS = 8

ANIMATION_SPEED = 0.2

# Definimos las variables
numbers_played = []

font_historic = pygame.font.SysFont("Arial", 16)
font_historic_title = pygame.font.SysFont("Arial", 48)

animation_accent_color = YELLOW
animation_current_color = 0
animation_timer = 0

def draw_historic(screen):
    '''Dibujamos la zona del histórico por completo.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    draw_title(screen)
    draw_rect(screen)
    draw_numbers(screen)

def draw_rect(screen):
    '''Dibujamos la base sobre la que se dibujará el histórico.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Generamos la tupla a partir del valor del diccionario
    rect_tuple = tuple(RECT_HISTORIC_EXTERNAL.values())
    # Seleccionamos el color que debemos pintar de fondo del rectángulo exterior según la animación
    color = WHITE if animation_current_color == 0 else animation_accent_color

    # Dibujamos el rectángulo exterior con su borde
    pygame.draw.rect(screen, color, rect_tuple, border_radius=BORDER_RADIUS)
    pygame.draw.rect(screen, BLACK, rect_tuple, LINE_WIDTH, BORDER_RADIUS)

    # Generamos la tupla a partir del valor del diccionario
    rect_tuple = tuple(RECT_HISTORIC_INNER.values())
    
    # Dibujamos el rectángulo interior con su borde
    pygame.draw.rect(screen, BROWN, rect_tuple)
    pygame.draw.rect(screen, BLACK, rect_tuple, LINE_WIDTH)

def draw_numbers(screen):
    '''Dibujamos las diferentes casillas con los números que han salido en la ruleta.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Seteamos la posición inicial de las casillas en X
    pos_x = CELL_X_START
    for number in numbers_played:
        # Seteamos la posición en Y de la casilla según su color
        pos_y = CELL_Y_POSITIONS[number["color"]]

        # Dibujamos el fondo de la casilla del color que ha salido en la ruleta
        rect_tuple = (pos_x, pos_y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, number["color"], rect_tuple)

        # Seleccionamos el color que debe tener el borde y lo dibujamos
        border_color = WHITE if number["color"] == BLACK else BLACK
        pygame.draw.rect(screen, border_color, rect_tuple, LINE_WIDTH)

        # Seleccionamos el color del texto que deberá tener la casillas
        color = BLACK if number["color"] == RED else WHITE
        string_surface = font_historic.render(f"{number["number"]}", True, color)
        string_rect = string_surface.get_rect()

        # Calculamos el centro de la casilla y centramos el texto
        center = (pos_x + CELL_HALF_SIZE, pos_y + CELL_HALF_SIZE)
        string_rect.centerx = center[0]
        string_rect.centery = center[1]

        # Dibujamos el pantalla el texto
        screen.blit(string_surface, string_rect)

        # Disminuimos la posición de la casilla en su tamaño
        pos_x -= CELL_SIZE

def draw_title(screen):
    '''Dibujamos el título del histórico de la ruleta.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Generamos el texto y definimos su tamaño
    string_surface = font_historic_title.render(f"{TITLE_TEXT}", True, BLACK)
    string_rect = string_surface.get_rect()

    # Centramos el texto en la posición de la variable TITLE_TEXT_POSITION
    center = TITLE_TEXT_POSITION
    string_rect.centerx = center[0]
    string_rect.centery = center[1]

    # Dibujamos el texto por pantalla
    screen.blit(string_surface, string_rect)

def add_played_number(number):
    '''Añadimos en la primera posición de la lista de números jugados el número que ha salido en la ruleta.

    Input:
        -number(dict): Diccionario con toda la información del número que tenemos almacenada en la variable 'ruleta_distribucio' en ruleta.py.

    Retorna: None'''
    global numbers_played, animation_accent_color

    # Insertamos al inicio del array el diccionario que nos ha llegado como parámetro
    numbers_played.insert(0, number)

    # Gestionamos el tamaño de la lista, para que sólo salgan X cantidad de números como mucho
    if len(numbers_played) > LIST_MAX_SIZE:
        numbers_played = numbers_played[:LIST_MAX_SIZE]

    # Cambiamos el color al que deberá cambiar en la animación de parpadeo
    animation_accent_color = number["color"]

def define_current_color():
    '''Definimos el color que debe mostrar según lo que llevamos de animación

    Retorna: None'''

    global animation_timer, animation_current_color

    # Revisamos si la animación ha pasado el límite de tiempo.
    #   En caso que así sea, seteamos el temporizador a 0 y cambiamos el color
    if animation_timer >= ANIMATION_SPEED:
        animation_timer = 0
        animation_current_color = (animation_current_color + 1) % 2

def control_blink_animation(delta_time):
    '''Controlamos la animación del parpadeo del marco exterior del histórico.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.

    Retorna: None'''
    global animation_timer

    # Añadimos el tiempo a la animación y gestionamos el cambio de color
    animation_timer += delta_time
    define_current_color()