#!/usr/bin/env python3

import pygame

# Definimos las constantes
POINTS_ARROW = [(425, 390), (450, 405), (450, 375)]
PIVOT = (437, 408)
YELLOW = (240, 229, 48)

# Definimos las variables
angle = 0
down_speed = 0
arrow_movement = 0

def draw_arrow(screen):
    '''Dibujamos la flecha en la posición indicada del color azul.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Rotamos los puntos según el ángulo en el que nos encontramos y dibujos la flecha
    rotated_points = rotate_points()
    pygame.draw.polygon(screen, YELLOW, rotated_points)

def rotate_points():
    '''Rotamos todos los puntos inciales según el ángulo que vamos sumando en la variable 'angle'

    Retorna: list'''

    # Función recogida de https://stackoverflow.com/questions/75116101/how-to-make-rotate-polygon-on-key-in-pygame
    # Recoge un Vector2 de un pivote y va realizando la rotación de cada uno de los puntos de una lista
    vector2_position = pygame.math.Vector2(PIVOT)
    rotated_points = [
        (pygame.math.Vector2(x, y) - vector2_position).rotate(angle) + vector2_position for x, y in POINTS_ARROW]
    return rotated_points

def control_rotation(delta_time, ruleta_speed, angle_step):
    '''Controlamos la rotación que debe de tener la flecha en función de la posción en la casilla que tenga la punta y si ha de rotar hacia la izquierda o la derecha.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.
        -ruleta_speed(float): Velocidad actual en la que se encuentra girando la ruleta.
        -angle_step(float): Ángulo que tendremos en cuenta a la hora de rotar la flecha en una dirección u otra.

    Retorna: None'''

    global arrow_movement, angle

    # !Nota: Arrow_movement:
    #   0 -> Rotación hacia la izquierda
    #   1 -> Rotación hacia la derecha
    #
    # Miramos hacia que lado estamos rotando y aplicamos la rotación
    # Tendremos en cuenta que no queremos que el ángulo de rotación se nos escape de -angle_step y de 0, ya que sino la velocidad no dejará que se mueva correctamente por falta de fuerza.
    # Al llegar a estos límites, cambiamos el sentido del giro.
    if arrow_movement == 0:
        angle = max(angle - ruleta_speed * delta_time, -angle_step)
    else:
        angle = min(angle + ruleta_speed * delta_time, 0)
    
    if angle == -angle_step or angle == 0:
            arrow_movement = (arrow_movement + 1) % 2        

def reset_arrow_rotation():
    '''Reseteamos el giro y el movimiento de la flecha para que cuando deba volver a girar lo haga de manera correcta.

    Retorna: None'''

    global arrow_movement, angle

    arrow_movement = 0
    angle = 0