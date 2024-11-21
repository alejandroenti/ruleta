#!/usr/bin/env python3

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
SALMON = (227, 70, 104)

# Definir la finestra
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window Title')

jugadores = [
    {"nom": "Taronja", "005": 2, "010": 2, "020": 2, "050": 2, "100": 2},
    {"nom": "Lila", "005": 2, "010": 2, "020": 2, "050": 2, "100": 2},
    {"nom": "Blau", "005": 2, "010": 2, "020": 2, "050": 2, "100": 2}
]

def printJugadores(screen, coords, height=500, width=200):
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