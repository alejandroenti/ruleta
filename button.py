#!/usr/bin/env python3

import pygame
import utils

# Definimos las constantes
BUTTON_EXTERIOR = (500, 100, 150, 75)
BUTTON_INTERIOR = (510, 110, 130, 55)
PADDING = 2

TEXT_POSITION = (575, 140)

BUTTON_TEXT = "SPIN"

BUTTON_BLINK_SPEED = 0.3

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
    pygame.draw.rect(screen, color, BUTTON_EXTERIOR, border_radius=32)
    pygame.draw.rect(screen, BLACK, BUTTON_EXTERIOR, button_line_width, 32)

    # Añadimos el texto al botón
    string_surface = font_ruleta.render(BUTTON_TEXT, True, WHITE)
    string_rect = string_surface.get_rect()

    # Centramos el texto
    string_rect.center = TEXT_POSITION

    screen.blit(string_surface, string_rect)

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

    # Si la ruleta se encuentra girando, deberemos controlar el color del fondo del botón.
    # En caso contrario:
    #   Si lo estamos presionando, tendrá un color rojo oscuro.
    #   Si estamos sólo sobre él, tendrá un rojo más claro.
    #   En el resto de casos, tendrá un color rojo normal.
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

    # Aumentamos el contador de la animación. En cuanto se pase, cambiaremos el color que deberá tomar el botón y reiniciamos el contador
    animation_timer += delta_time
    if animation_timer >= BUTTON_BLINK_SPEED:
        animation_timer = 0
        animation_color = (animation_color + 1) % 2

def check_states(mouse):
    '''Cambiamos los estados del botón, siempre que el mouse esté dentro del botón.

    Input:
        -mouse(dict): Diccionario con la toda información del mouse.

    Retorna: None'''
    global is_pressed, is_hover

    if mouse["pressed"]:
        is_pressed = True
        is_hover = False
    elif mouse["released"]:
        is_pressed = False
        is_hover = False
    else:
        is_hover = True
        is_pressed = False