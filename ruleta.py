#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

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

ANGLE_STEP = 360 / POSICIONS

GREEN = (52, 220, 22)
RED = (220, 22, 22)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (128, 60, 34)
GOLD = (255, 215, 0)
SILVER = (192, 192, 192)

# Definim les variables globals
numeros_vermells = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ruleta_distribucio = []

is_spinning = False

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Alejandro López - Exercici Paint')

font_ruleta = pygame.font.SysFont("Arial", 12)

def init_ruleta():
    global ruleta_distribucio

    fila = 0

    for num in range(POSICIONS):
        # Definim el color de la casella a la ruleta
        if num in numeros_vermells:
            color = RED
        elif num == 0:
            color = GREEN
        else:
            color = BLACK

        posicio = {
            "number": num,                                  # Indica el propi número
            "row": 0 if num == 0 else fila,                 # Indica la fila a la que es troba per apostar, si el número es 0, la fila també serà 0
            "parity": "even" if num % 2 == 0 else "odd",    # Indica si el número es par o impar
            "color": color,                                 # Indica el color del que s'ha de pintar la casella
            "bets": {},                                     # Indica les apostes que n'hi han en aquesta casella, pot ser un diccionari similar { "player": Blau, "aposta": {"010": 3} }
            "angles": [ANGLE_STEP * num - 90, ANGLE_STEP * num + ANGLE_STEP - 90]   # Indicamos los ángulos de inicio y de final del polígono que dibujaremos en la ruleta
        }

        # Afegim el diccionari a la ruleta
        ruleta_distribucio.append(posicio)

        fila = 1 if fila == 3 else fila + 1

def draw_ruleta():
    global ruleta_distribucio

    draw_base_ruleta()
    for num_object in ruleta_distribucio:
        draw_rect(num_object)

def draw_rect(object):
    points = get_draw_points(object)

    pygame.draw.polygon(screen, object["color"], points)
    pygame.draw.polygon(screen, WHITE, points, 2)

    color = BLACK if object["color"] == RED else WHITE

    string_surface = font_ruleta.render(f"{object["number"]}", True, color)
    surface_rotation = -90 - object["angles"][0] - ANGLE_STEP / 2
    string_surface = pygame.transform.rotozoom(string_surface, surface_rotation, 1.0)
    string_rect = string_surface.get_rect()

    pos = tuple(utils.point_on_circle(CENTER, RADI_TEXT, object["angles"][0] + ANGLE_STEP / 2).values())
    string_rect.centerx = pos[0]
    string_rect.centery = pos[1]

    screen.blit(string_surface, string_rect)

def get_draw_points(object):
    return [
        tuple(utils.point_on_circle(CENTER, RADI_INTERIOR, object["angles"][0]).values()),
        tuple(utils.point_on_circle(CENTER, RADI_EXTERIOR, object["angles"][0]).values()),
        tuple(utils.point_on_circle(CENTER, RADI_EXTERIOR, object["angles"][1]).values()),
        tuple(utils.point_on_circle(CENTER, RADI_INTERIOR, object["angles"][1]).values()),
    ]

def draw_base_ruleta():
    center = (CENTER["x"], CENTER["y"])
    pygame.draw.circle(screen, BROWN, center, RADI_RULETA)
    pygame.draw.circle(screen, BLACK, center, RADI_RULETA, 10)
    pygame.draw.circle(screen, SILVER, center, RADI_DECORACIO_1)
    pygame.draw.circle(screen, BLACK, center, RADI_DECORACIO_1, 2)
    pygame.draw.circle(screen, GOLD, center, RADI_DECORACIO_2)
    pygame.draw.circle(screen, BLACK, center, RADI_DECORACIO_2, 2)

def spin_ruleta():
    global is_spinning

    is_spinning = True

# Bucle de l'aplicació
def main():
    is_looping = True

    init_ruleta()
    spin_ruleta()

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
    
    return True

def app_run():
    global is_spinning, ruleta_distribucio

    delta_time = clock.get_time() / 1000.0  # Convertir a segons
    speed = 50

    if is_spinning:
        for obj in ruleta_distribucio:
            obj["angles"][0] =  (obj["angles"][0] + speed * delta_time) % 360
            obj["angles"][1] =  (obj["angles"][1] + speed * delta_time) % 360


def app_draw():
    global points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(WHITE)

    draw_ruleta()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

main()