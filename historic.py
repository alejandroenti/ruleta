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
     "y": 530,
     "width": 560,
     "heigth": 120
}

RECT_HISTORIC_INNER = {
     "x": 696,
     "y": 546,
     "width": 528,
     "heigth": 84
}

CELL_Y_POSITIONS = {
    BLACK: 450,
    GREEN: 470,
    RED: 490
}

CELL_X_COMPLETE_START = 1180
CELL_X_START = 1220
CELL_X_END = 696

CELL_SIZE = 40
CELL_HALF_SIZE = 20

LINE_WIDTH = 4

LIST_MAX_SIZE = 13

TITLE_TEXT = "HISTORIC"
TITLE_TEXT_POSITION = (960, 500)

BORDER_RADIUS = 8

ANIMATION_BLINK_SPEED = 0.2
ANIMATION_ENTER_SPEED = 50

# Definimos las variables
numbers_played = []

font_historic = pygame.font.SysFont("Arial", 16)
font_historic_title = pygame.font.SysFont("Arial", 48)

animation_blink_accent_color = YELLOW
animation_blink_current_color = 0
animation_blink_timer = 0

animation_enter = False

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
    color = WHITE if animation_blink_current_color == 0 else animation_blink_accent_color

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

    for number in numbers_played:
        # Dibujamos el fondo de la casilla del color que ha salido en la ruleta
        rect_tuple = (number["x"], number["y"], number["width"] , CELL_SIZE)
        pygame.draw.rect(screen, number["color"], rect_tuple)

        # Seleccionamos el color que debe tener el borde y lo dibujamos
        pygame.draw.rect(screen, number["border_color"], rect_tuple, LINE_WIDTH)

        # !NOTA: Sólo calculamos el texto si supera la mitad el ancho de la casilla
        if number["width"] >= CELL_HALF_SIZE:
            # Seleccionamos el color del texto que deberá tener la casillas
            color = BLACK if number["color"] == RED else WHITE
            string_surface = font_historic.render(f"{number['number']}", True, color)
            string_rect = string_surface.get_rect()

            # Calculamos el centro de la casilla y centramos el texto
            center = (number["x"] + number["width"]  / 2, number["y"] + CELL_HALF_SIZE)
            string_rect.centerx = center[0]
            string_rect.centery = center[1]

            # Dibujamos el pantalla el texto
            screen.blit(string_surface, string_rect)

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
    global numbers_played, animation_blink_accent_color, animation_enter

    # Insertamos al inicio del array el diccionario con las propiedades necesarias para dibujar posteriormente la casilla
    number_dict = {
        "x": CELL_X_START,
        "y": CELL_Y_POSITIONS[number["color"]],
        "width": 0,
        "number": number["number"],
        "color": number["color"],
        "border_color": WHITE if number["color"] == BLACK else BLACK
    }
    numbers_played.insert(0, number_dict)

    # Cambiamos el color al que deberá cambiar en la animación de parpadeo
    animation_blink_accent_color = number["color"]

    # Iniciamos la animación de entrada de la nueva casilla
    animation_enter = True

def define_current_color():
    '''Definimos el color que debe mostrar según lo que llevamos de animación

    Retorna: None'''

    global animation_blink_timer, animation_blink_current_color

    # Revisamos si la animación ha pasado el límite de tiempo.
    #   En caso que así sea, seteamos el temporizador a 0 y cambiamos el color
    if animation_blink_timer >= ANIMATION_BLINK_SPEED:
        animation_blink_timer = 0
        animation_blink_current_color = (animation_blink_current_color + 1) % 2

def control_animations(delta_time):
    '''Controlamos las dos animaciones que tenemos en el histórico: parpadeo del marco y la entrada de la nueva casilla cuando acaba de girar la ruleta.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.

    Retorna: None'''

    control_blink_animation(delta_time)
    
    if animation_enter:
        control_enter_animation(delta_time)

def control_blink_animation(delta_time):
    '''Controlamos la animación del parpadeo del marco exterior del histórico.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.

    Retorna: None'''

    global animation_blink_timer

    # Añadimos el tiempo a la animación y gestionamos el cambio de color
    animation_blink_timer += delta_time
    define_current_color()

def control_enter_animation(delta_time):
    '''Controlamos la animación de entrada de una nueva casilla y la salida de la más antogua.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.

    Retorna: None'''

    global animation_enter, numbers_played

    # Recorremos todas las casillas que tenemos almacenadas en numbers_played
    for index, number in enumerate(numbers_played):
        # En caso de que no sea la última casilla, incrementamos su valor de X
        if index != LIST_MAX_SIZE:
            number["x"] = max(number["x"] - ANIMATION_ENTER_SPEED * delta_time, CELL_X_COMPLETE_START - (CELL_SIZE * index))
            # Además, si nos encontramos con la primera casilla, incrementaremos también su anchura
            if index == 0:
                number["width"] += ANIMATION_ENTER_SPEED * delta_time
        # En caso de ser la última, iremos descendiendo su anchura
        else:
            number["width"] -= ANIMATION_ENTER_SPEED * delta_time
    
    # Cuando la primera casilla haya llegado a un punto indicado, pararemos la animación y recortaremos la lista de numbers_played a LIST_MAX_SIZE
    if numbers_played[0]["x"] == CELL_X_COMPLETE_START:
        animation_enter = False
        numbers_played = numbers_played[:LIST_MAX_SIZE]