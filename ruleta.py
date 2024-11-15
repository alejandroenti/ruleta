#!/usr/bin/env python3

import pygame
import sys

# Definim les constants
POSICIONS = 37
FILES = 3
CENTER = (450, 450)
RADI = 350

GREEN = (52, 220, 22)
RED = (220, 22, 22)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definim les variables globals
numeros_vermells = [1, 3, 5, 6, 7, 12, 14, 16, 18, 19, 21, 22, 23, 25, 27, 30, 32, 34, 36]
ruleta_distribucio = []

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Alejandro López - Exercici Paint')

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

    pygame.draw.circle(screen, BLACK, CENTER, RADI, 5)



# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

def app_events():
    pass

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