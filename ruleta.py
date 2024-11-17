#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

# Definim les constants
POSICIONS = 37
FILES = 3
CENTER = { "x": 250, "y": 250 }
RADI_RULETA = 225
RADI_EXTERIOR = 185
RADI_INTERIOR = 50
RADI_TEXT = 155
RADI_DECORACIO_1 = 30
RADI_DECORACIO_2 = 10

POINTS_ARROW = [(425, 250), (500, 200), (500, 300)]

ANGLE_STEP = 360 / POSICIONS

RULETA_ACCELERATION = -2.5
RULETA_SPIN_REV = 3

GREEN = (52, 220, 22)
RED = (220, 22, 22)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (128, 60, 34)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)
BLUE = (91, 182, 237)

# Definim les variables globals
numeros_vermells = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ruleta_distribucio = []

winner_number = None
winner_angle = 0

ruleta_init_spin_angle = 0
ruleta_actual_spin_angle = 0
ruleta_actual_speed = 0

is_spinning = False

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Alejandro López - Exercici Paint')

font_ruleta = pygame.font.SysFont("Arial", 12)

def init_ruleta():
    '''Inicializamos todas las casillas de la ruleta. Esta estructura también puede ser usada para las apuestas, ya que indica en que fila se encuentra, si es par o impar y color.

    Retorna: None'''

    global ruleta_distribucio

    fila = 0

    for num in range(POSICIONS):
        # Definimos el color de la casilla a la ruleta
        if num in numeros_vermells:
            color = RED
        elif num == 0:
            color = GREEN
        else:
            color = BLACK

        posicio = {
            "number": num,                                  # Indica el propio número
            "row": 0 if num == 0 else fila,                 # Indica la fila an la que es encuentra para apostar, si el número es 0, la fila tambén será 0
            "parity": "even" if num % 2 == 0 else "odd",    # Indica si el número es par o impar
            "color": color,                                 # Indica el color del que se ha de pintar la casilla
            "bets": {},                                     # Indica las apuestas que hay en esta casilla, puede ser una diccionario similar { "player": Blau, "bet": {"010": 3, "050": 1} }
            "angles": [ANGLE_STEP * num - 90, ANGLE_STEP * num + ANGLE_STEP - 90]   # Indicamos los ángulos de inicio y de final del polígono que dibujaremos en la ruleta
        }

        # Añadimos el diccionario a la ruleta
        ruleta_distribucio.append(posicio)

        fila = 1 if fila == 3 else fila + 1

def draw_ruleta():
    '''Dibujamos la ruleta completa, desde la base con sus elementos de decoración junto con cada una de las casillas.

    Retorna: None'''

    global ruleta_distribucio

    draw_base_ruleta()
    for num_object in ruleta_distribucio:
        draw_rect(num_object)

def draw_rect(object):
    '''Dibujamos el polígono que genera cada una de las casillas de la ruleta. 

    Input:
        -obj(dict): Diccionario con todas las propiedades de cada una de las casillas a representar.

    Retorna: None'''

    # Conseguimos los puntos del polígono
    points = get_draw_points(object)

    # Dibujamos el polígono del color que nos viene indicado en la propiedad 'color' y los marcamos con un borde blanco
    pygame.draw.polygon(screen, object["color"], points)
    pygame.draw.polygon(screen, WHITE, points, 2)

    # Elegimos el color de la fuente para representar el número
    color = BLACK if object["color"] == RED else WHITE

    # Generamos la string que deberás ser representada:
    #   1. Renderizamos el número con la fuente indicada
    #   2. Calculamos el ángulo de rotación necesario para que los números siempre estén mirando hacia el centro de la ruleta
    #   3. Rotamos el texto en el ángulo calcula previamente
    #   4. Calculamos el rectángulo que genera para trabahar sobre él
    #   5. Calculamos la posición en la que se debería posicionar el texto
    #   6. Centramos el texto en la posición calculada anteriormente

    string_surface = font_ruleta.render(f"{object["number"]}", True, color)
    surface_rotation = -90 - object["angles"][0] - ANGLE_STEP / 2
    string_surface = pygame.transform.rotozoom(string_surface, surface_rotation, 1.0)
    string_rect = string_surface.get_rect()

    pos = tuple(utils.point_on_circle(CENTER, RADI_TEXT, object["angles"][0] + ANGLE_STEP / 2).values())
    string_rect.centerx = pos[0]
    string_rect.centery = pos[1]

    screen.blit(string_surface, string_rect)

def get_draw_points(object):
    '''Dado un objeto que nos dice todas las propiedades de una casilla, calculamos los puntos en los que se encuentra para dibujarla dentro de la ruleta.

    Input:
        -obj(dict): Diccionario con todas las propiedades de cada una de las casillas a representar.

    Retorna: list'''

    return [
        tuple(utils.point_on_circle(CENTER, RADI_INTERIOR, object["angles"][0]).values()),
        tuple(utils.point_on_circle(CENTER, RADI_EXTERIOR, object["angles"][0]).values()),
        tuple(utils.point_on_circle(CENTER, RADI_EXTERIOR, object["angles"][1]).values()),
        tuple(utils.point_on_circle(CENTER, RADI_INTERIOR, object["angles"][1]).values()),
    ]

def draw_base_ruleta():
    '''Dibujamos la base de la ruleta. La base total de color marrón con un marcado grande de color negro, y la decoración, simulando una ruleta de casino en el mundo real.

    Retorna: None'''

    # Calculamos el centro de la ruleta
    center = (CENTER["x"], CENTER["y"])

    # Dibujamos la base de la ruleta con su borde negro
    pygame.draw.circle(screen, BROWN, center, RADI_RULETA)
    pygame.draw.circle(screen, BLACK, center, RADI_RULETA, 10)

    # Dibujamos la parte decorativa de la ruleta, se separa en dos colores para que se diferencien un poco. Ambos tienen un borde negro para resaltarlos un poco más
    pygame.draw.circle(screen, SILVER, center, RADI_DECORACIO_1)
    pygame.draw.circle(screen, BLACK, center, RADI_DECORACIO_1, 2)
    pygame.draw.circle(screen, GOLD, center, RADI_DECORACIO_2)
    pygame.draw.circle(screen, BLACK, center, RADI_DECORACIO_2, 2)

def draw_arrow():
    pygame.draw.polygon(screen, BLUE, POINTS_ARROW)

def init_spin():
    '''Configuramos las variables necesarias para que el giro de la ruleta de pueda realizar de manera correcta.

    Retorna: None'''

    global is_spinning, winner_number, winner_angle, ruleta_init_spin_angle, ruleta_actual_spin_angle, ruleta_actual_speed, ruleta_init_spin_angle

    # Cambiamos la varibles is_spinning a True para que en el app_run() se ejecute la función spin()
    is_spinning = True

    # Calculamos el número que será el ganador y el ángulo en el que se encuentra si texto
    winner_number = random.randint(0, POSICIONS - 1)
    winner_angle = ruleta_distribucio[winner_number]["angles"][0] + ANGLE_STEP / 2

    # Calculamos el giro que deberá hacer la ruleta.
    # !NOTA: si se encuentra retrasada, debemos sumar el ángulo en términos absolutos, ya que deberá dar más giro)
    ruleta_init_spin_angle = (RULETA_SPIN_REV * 360) + abs(winner_angle) if winner_angle < 0 else (RULETA_SPIN_REV * 360) - winner_angle
    ruleta_actual_spin_angle = ruleta_init_spin_angle

    # Calculamos la velcidad incial necesaria para que dado un ángulo a recorrer y una aceleración, la velocidad llegue a 0 de manera continuada
    ruleta_actual_speed = math.sqrt(-2 * RULETA_ACCELERATION * ruleta_actual_spin_angle)

def spin(delta_time):
    '''Calculamos el giro que debe estar dando la ruleta en este preciso momento. También gestionamos el final del giro de esta.

    Retorna: None'''

    global winner_number, winner_angle, ruleta_actual_spin_angle, ruleta_actual_speed, is_spinning, ruleta_distribucio

    # Por cada casilla, vamos aumentando el ángulo de incio y de final
    for obj in ruleta_distribucio:
            obj["angles"][0] = (obj["angles"][0] + ruleta_actual_speed * delta_time) % 360
            obj["angles"][1] = (obj["angles"][1] + ruleta_actual_speed * delta_time) % 360

    # Restamos el ángulo actual en el que nos encontramos según la velocidad
    ruleta_actual_spin_angle -= ruleta_actual_speed * delta_time

    # Disminuimos la velocidad en respecto a la aceleración
    # !NOTA: Disminuimos la velocidad por una aceleración negativa
    ruleta_actual_speed += RULETA_ACCELERATION * delta_time

    # Gestionamos la llegada de la ruleta a la posición indicada
    if ruleta_actual_spin_angle <= 0:
        is_spinning = False

# Bucle de l'aplicació
def main():
    is_looping = True

    init_ruleta()

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            init_spin()
    
    return True

def app_run():
    global is_spinning

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    if is_spinning:
        spin(delta_time)

def app_draw():
    global points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(WHITE)

    draw_ruleta()
    draw_arrow()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

main()