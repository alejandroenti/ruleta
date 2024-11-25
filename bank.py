#!/usr/bin/env python3

import pygame

# Definimos las constantes
RECT_BANK = {
     "x": 1260,
     "y": 705,
     "width": 200,
     "heigth": 120
}

BORDER_RADIUS = 8
LINE_WIDTH = 4

TITLE_TEXT = "BANK"
TITLE_TEXT_POSITION = (1360, 675)

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Definimos las variables
font_bank = pygame.font.SysFont("Arial", 48)

def draw_bank(screen):
    '''Dibujamos la zona de la banca por completo.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    draw_title(screen)
    draw_rect(screen)

def draw_rect(screen):
    '''Dibujamos el quadrado que representa la banca.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Generamos la tupla a partir del valor del diccionario
    rect_tuple = tuple(RECT_BANK.values())

    # Dibujamos el rectángulo exterior con su borde
    pygame.draw.rect(screen, GRAY, rect_tuple, border_radius=BORDER_RADIUS)
    pygame.draw.rect(screen, BLACK, rect_tuple, LINE_WIDTH, BORDER_RADIUS)

def draw_title(screen):
    '''Dibujamos el título de la banca de la ruleta.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Generamos el texto y definimos su tamaño
    string_surface = font_bank.render(f"{TITLE_TEXT}", True, BLACK)
    string_rect = string_surface.get_rect()

    # Centramos el texto en la posición de la variable TITLE_TEXT_POSITION
    center = TITLE_TEXT_POSITION
    string_rect.centerx = center[0]
    string_rect.centery = center[1]

    screen.blit(string_surface, string_rect)