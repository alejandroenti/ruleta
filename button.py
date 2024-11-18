#!/usr/bin/env python3

import pygame
import utils

# Definimos las constantes
BUTTON_EXTERIOR = (500, 100, 150, 75)
BUTTON_INTERIOR = (510, 110, 130, 55)
PADDING = 2

TEXT_POSITION = (575, 140)

BUTTON_TEXT = "SPIN"

BUTTON_BLINK_SPEED = 0.5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (221, 34, 34)
RED_DARK = (175, 20, 20)
RED_LIGHT = (248, 64, 64)

# Definimos las variables
is_hover = False
is_pressed = False

button_names = ["x", "y", "width", "height"]
button_dict = dict(zip(button_names, BUTTON_EXTERIOR))
button_lines_width = [5, 8]

animation_timer = 0
animation_color = 0

font_ruleta = pygame.font.SysFont("Arial", 48)

def draw_button(screen, is_spining):
    '''Dibujamos el botón para hacer girar la ruleta

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Seleccionamos el color con el que vamos a pintar el botón
    color = select_color_button(is_spining)

    # Dibujamos la base del botón
    button_line_width = select_line_width_button()
    draw_base_button(screen, color, button_line_width)

    # Añadimos el texto al botón
    string_surface = font_ruleta.render(BUTTON_TEXT, True, WHITE)
    string_rect = string_surface.get_rect()

    string_rect.center = TEXT_POSITION

    screen.blit(string_surface, string_rect)

def draw_base_button(screen, color, line_width):
    if is_pressed:
        pygame.draw.rect(screen, color, BUTTON_EXTERIOR, border_radius=32)
        pygame.draw.rect(screen, BLACK, BUTTON_EXTERIOR, line_width, 32)
    else:
        pygame.draw.rect(screen, color, BUTTON_EXTERIOR, border_radius=32)
        pygame.draw.rect(screen, BLACK, BUTTON_EXTERIOR, line_width, 32)


def is_hover_button(mouse_pos): 
    '''Detectamos si el ratón se encuentra sobre el botón.

    Input:
        -mouse_pos(dict): Diccionario con toda la información del mouse

    Retorna: bool'''
    global button_dict

    return utils.is_point_in_rect(mouse_pos, button_dict)

def select_color_button(is_spining):
    '''Seleccionamos el color con el que vamos a pintar el fondo del botón en función de la interacción que tenemos con él.

    Input:
        -is_spinning(bool): Booleano que nos indica si la ruleta se encuentra ahora mismo girando o no.

    Retorna: color'''

    if is_spining:    
        return RED if animation_color == 0 else RED_LIGHT
    else:
        if is_pressed:
            return RED_DARK
        elif is_hover:
            return RED_LIGHT
        else:
            return RED

def select_line_width_button():
    '''Seleccionamos el ancho de la línia del botón para simular la pulsación.

    Retorna: int'''

    return button_lines_width[1] if is_pressed else button_lines_width[0]

def control_blink_animation(delta_time):
    '''Controlamos la animación de parpadeo del botón mientras la ruleta se encuentra girando. Si pasa de la velocidad del blink cambiamos también el color del fondo del botón.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.

    Retorna: None'''

    global animation_timer, animation_color

    animation_timer += delta_time
    if animation_timer >= BUTTON_BLINK_SPEED:
        animation_timer = 0
        animation_color = (animation_color + 1) % 2