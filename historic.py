#!/usr/bin/env python3

import pygame

# Definimos las constantes
BLACK = (0, 0, 0)
RED = (220, 22, 22)
GREEN = (52, 220, 22)
WHITE = (255, 255, 255)
YELLOW = (240, 229, 48)

RECT_HISTORIC_EXTERNAL = {
     "x": 680,
     "y": 430,
     "width": 560,
     "heigth": 120
}

RECT_HISTORIC_INNER = {
     "x": 696,
     "y": 446,
     "width": 524,
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

# Definimos las variables
numbers_played = []

font_historic = pygame.font.SysFont("Arial", 16)
font_historic_title = pygame.font.SysFont("Arial", 48)

color

def draw_historic(screen):
    '''Dibujamos la zona del histórico por completo.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    draw_title(screen)
    draw_numbers(screen)
    draw_rect(screen)

def draw_rect(screen):
    '''Dibujamos la base sobre la que se dibujará el histórico.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Rotamos los puntos según el ángulo en el que nos encontramos y dibujos la flecha
    rect_tuple = tuple(RECT_HISTORIC_INNER.values())
    pygame.draw.rect(screen, BLACK, rect_tuple, LINE_WIDTH)

    rect_tuple = tuple(RECT_HISTORIC_EXTERNAL.values())
    pygame.draw.rect(screen, BLACK, rect_tuple, LINE_WIDTH)

def draw_numbers(screen):
    '''Dibujamos las diferentes casillas con los números que han salido en la ruleta.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''
    pos_x = CELL_X_START
    for number in numbers_played:
        pos_y = CELL_Y_POSITIONS[number["color"]]

        rect_tuple = (pos_x, pos_y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, number["color"], rect_tuple)

        border_color = WHITE if number["color"] == BLACK else BLACK
        pygame.draw.rect(screen, border_color, rect_tuple, LINE_WIDTH)

        color = BLACK if number["color"] == RED else WHITE
        string_surface = font_historic.render(f"{number["number"]}", True, color)
        string_rect = string_surface.get_rect()

        center = (pos_x + CELL_HALF_SIZE, pos_y + CELL_HALF_SIZE)
        string_rect.centerx = center[0]
        string_rect.centery = center[1]

        screen.blit(string_surface, string_rect)

        pos_x -= CELL_SIZE

def draw_title(screen):
    '''Dibujamos el título del histórico de la ruleta.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    string_surface = font_historic_title.render(f"{TITLE_TEXT}", True, BLACK)
    string_rect = string_surface.get_rect()

    center = TITLE_TEXT_POSITION
    string_rect.centerx = center[0]
    string_rect.centery = center[1]

    screen.blit(string_surface, string_rect)


def add_played_number(number):
    '''Añadimos en la primera posición de la lista de números jugados el número que ha salido en la ruleta.

    Input:
        -number(dict): Diccionario con toda la información del número que tenemos almacenada en la variable 'ruleta_distribucio' en ruleta.py.

    Retorna: None'''
    global numbers_played

    numbers_played.insert(0, number)

    if len(numbers_played) > LIST_MAX_SIZE:
        numbers_played = numbers_played[:LIST_MAX_SIZE]