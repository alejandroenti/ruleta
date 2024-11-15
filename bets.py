#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from ruleta import numeros_vermells
from jugadores import jugadores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
SALMON = (227, 70, 104)
RED = (255, 0, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window Title')

surface = pygame.Surface((WIDTH, HEIGHT))

# Bucle de l'aplicació
def main():
    is_looping = True

    surface.fill(WHITE)

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Botó tancar finestra
            return False
        
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    drawBetTable((50, 50))
    
    pygame.display.update()

def makeBet(player, posicio):
    pass

def drawBetTable(coords):
    #LOS NUMS DE LAS FILAS DE UNA RULETA REAL
    nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, ]
    for row in range(3):
        for cell in range(12):
            colorFicha = RED if cell * row in numeros_vermells else BLACK
            pygame.draw.rect(screen, GRAY, ((coords[0] + (35 * cell), coords[1] + (35 * row)), (35, 35)))
            pygame.draw.rect(screen, BLACK, ((coords[0] + (35 * cell), coords[1] + (35 * row)), (35, 35)), 3)
            
            pygame.draw.circle(screen, colorFicha, ((16 + coords[0] + (35 * cell), 16 + coords[1] + (35 * row))), 10)

if __name__ == "__main__":
    main()