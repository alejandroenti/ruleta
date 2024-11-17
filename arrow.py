#!/usr/bin/env python3

import pygame

# Definimos las constantes
POINTS_ARROW = [(425, 250), (500, 200), (500, 300)]

BLUE = (91, 182, 237)

def draw_arrow(screen):
    '''Dibujamos la flecha en la posición indicada del color azul.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    pygame.draw.polygon(screen, BLUE, POINTS_ARROW)