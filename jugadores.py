#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
SALMON = (227, 70, 104)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window Title')

jugadores = [
    {"nom": "Taronja", "005": 7, "010": 2, "020": 1, "050": 1, "100": 3},
    {"nom": "Lila", "005": 1, "010": 2, "020": 1, "050": 1, "100": 0},
    {"nom": "Blau", "005": 2, "010": 5, "020": 3, "050": 0, "100": 4}
]

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
    
    printJugadores((300, 250), 500, 200)
    pygame.display.update()

def printJugadores(coords, height=500, width=200):
    """coords: tuple con las coordenadas donde quieras la esquina superior izquierda del cuadro, 
    height: (int) altura del cuadro, width: (int) anchura del cuadro"""
    
    pygame.draw.rect(screen, SALMON, ((coords), (height, width)))
    pygame.draw.rect(screen, BLACK, ((coords), (height, width)), 10)
    fuenteNom = pygame.font.SysFont('Arial', 18, True)
    fuenteTxt = pygame.font.SysFont('Arial', 18)
    
    for jugador in jugadores:
        txtNom = fuenteNom.render(jugador["nom"] + f": {jugador['005'] * 5 + jugador['010']  * 10 + jugador['020'] * 20 + jugador['050'] * 50 + jugador['100'] * 100}", True, BLACK)
        txt = "005: " + str(jugador["005"]).ljust(10) +"010: " + str(jugador["010"]).ljust(10) +"020: " + str(jugador["020"]).ljust(10) +"050: "+ str(jugador["050"]).ljust(10) + "100: "+ str(jugador["100"])
        txtFicha = fuenteTxt.render(txt, True, BLACK)
        screen.blit(txtNom, (10 + coords[0] + 20 , coords[1] + 40 + 40 * jugadores.index(jugador)))
        screen.blit(txtFicha, (10 + coords[0] + 20, coords[1] + 60 + 40 * jugadores.index(jugador)))

if __name__ == "__main__":
    main()