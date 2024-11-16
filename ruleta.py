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
RADI_RULETA = 200
RADI_EXTERIOR = 185
RADI_INTERIOR = 50
RADI_TEXT = 155

GREEN = (52, 220, 22)
RED = (220, 22, 22)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (128, 60, 34)

# Definim les variables globals
numeros_vermells = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
ruleta_distribucio = []


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
            "bets": {}                                      # Indica les apostes que n'hi han en aquesta casella, pot ser un diccionari similar { "player": Blau, "aposta": {"010": 3} }
        }

        # Afegim el diccionari a la ruleta
        ruleta_distribucio.append(posicio)

        fila = 1 if fila == 3 else fila + 1

def draw_ruleta():
    global ruleta_distribucio

    center = (CENTER["x"], CENTER["y"])
    pygame.draw.circle(screen, BROWN, center, RADI_RULETA)

    angle = -90
    step = 360 / POSICIONS

    for num_object in ruleta_distribucio:
        draw_rect(num_object, angle, step)
        angle = (angle + step) % 360

def draw_rect(object, angle, step):
    points = [
        tuple(utils.point_on_circle(CENTER, RADI_INTERIOR, angle).values()),
        tuple(utils.point_on_circle(CENTER, RADI_EXTERIOR, angle).values()),
        tuple(utils.point_on_circle(CENTER, RADI_EXTERIOR, angle + step).values()),
        tuple(utils.point_on_circle(CENTER, RADI_INTERIOR, angle + step).values()),
    ]

    pygame.draw.polygon(screen, object["color"], points)
    pygame.draw.polygon(screen, WHITE, points, 2)

    color = BLACK if object["color"] == RED else WHITE

    string_surface = font_ruleta.render(f"{object["number"]}", True, color)
    surface_rotation = -90 - angle - step / 2
    string_surface = pygame.transform.rotozoom(string_surface, surface_rotation, 1.0)
    string_rect = string_surface.get_rect()

    pos = tuple(utils.point_on_circle(CENTER, RADI_TEXT, angle + step / 2).values())
    string_rect.centerx = pos[0]
    string_rect.centery = pos[1]

    screen.blit(string_surface, string_rect)

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
    
    return True

def app_run():
    pass

def app_draw():
    global points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(WHITE)

    draw_ruleta()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

main()