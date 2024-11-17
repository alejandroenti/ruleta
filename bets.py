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
    drawBetTable((100, 100))
    
    pygame.display.update()

def makeBet(player, posicio):
    pass

def drawBetTable(coords):
    #LOS NUMS DE LAS FILAS DE UNA RULETA REAL
    nums = [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35], [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]
    fuenteNum = pygame.font.SysFont('Arial', 16, True)

    #Dibuja lo que está alrededor del tablero que no son las casillas con números
    txt0 = fuenteNum.render('0', True, BLACK)
    pointsLines1 = [(coords[0], coords[1]), (coords[0] - 25, coords[1]), (coords[0] - 50, coords[1] + 25), (coords[0] - 25, coords[1] + 50), (coords[0], coords[1] + 50)]
    pygame.draw.polygon(screen, GRAY, pointsLines1)
    pygame.draw.lines(screen, BLACK, False, pointsLines1, 2)
    screen.blit(txt0, (coords[0] - 20, coords[1] + 17))

    txt00 = fuenteNum.render('00', True, BLACK)
    pointsLines2 = [(coords[0], coords[1] + 50), (coords[0] - 25, coords[1] + 50), (coords[0] - 50, coords[1] + 75), (coords[0] - 25, coords[1] + 100), (coords[0], coords[1] + 100)]
    pygame.draw.polygon(screen, GRAY, pointsLines2)
    pygame.draw.lines(screen, BLACK, False, pointsLines2, 2)
    screen.blit(txt00, (coords[0] - 25, coords[1] + 67))

    #Dibuja los tres rectangulos de debajo
    txtColumna1 = fuenteNum.render('Columna 1', True, BLACK)
    pygame.draw.rect(screen, GRAY, ((coords[0], coords[1] + 100), (140, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0], coords[1] + 100), (140, 40)), 3)
    screen.blit(txtColumna1, (27 + coords[0], 12 + coords[1] + 100))

    txtColumna2 = fuenteNum.render('Columna 2', True, BLACK)
    pygame.draw.rect(screen, GRAY, ((coords[0] + 140, coords[1] + 100), (140, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 140, coords[1] + 100), (140, 40)), 3)
    screen.blit(txtColumna2, (27 + coords[0] + 140, 12 + coords[1] + 100))
    
    txtColumna3 = fuenteNum.render('Columna 3', True, BLACK)
    pygame.draw.rect(screen, GRAY, ((coords[0] + 280, coords[1] + 100), (140, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 280, coords[1] + 100), (140, 40)), 3)
    screen.blit(txtColumna3, (27 + coords[0] + 280, 12 + coords[1] + 100))

    #Dibuja los tres cuadrados a la derecha de las casillas
    pygame.draw.rect(screen, GRAY, ((coords[0] + 35 * 12, coords[1]), (35, 35)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 35 * 12, coords[1]), (35, 35)), 3)

    pygame.draw.rect(screen, GRAY, ((coords[0] + 35 * 12, coords[1] + 35), (35, 35)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 35 * 12, coords[1] + 35), (35, 35)), 3)

    pygame.draw.rect(screen, GRAY, ((coords[0] + 35 * 12, coords[1] + 70), (35, 35)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 35 * 12, coords[1] + 70), (35, 35)), 3)

    #Dibuja los seis rectangulos de debajo de los tres rectangulos
    pygame.draw.rect(screen, GRAY, ((coords[0], coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0], coords[1] + 138), (70, 40)), 3)

    txtPares = fuenteNum.render("Pares", True, BLACK)
    pygame.draw.rect(screen, GRAY, ((coords[0] + 70, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 70, coords[1] + 138), (70, 40)), 3)
    screen.blit(txtPares, (12 + coords[0] + 70, 10 + coords[1] + 138))

    pygame.draw.rect(screen, RED, ((coords[0] + 140, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 140, coords[1] + 138), (70, 40)), 3)

    pygame.draw.rect(screen, BLACK, ((coords[0] + 210, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 210, coords[1] + 138), (70, 40)), 3)

    txtImpares = fuenteNum.render("Impares", True, BLACK)
    pygame.draw.rect(screen, GRAY, ((coords[0] + 280, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 280, coords[1] + 138), (70, 40)), 3)
    screen.blit(txtImpares, (4 + coords[0] + 280, 10 + coords[1] + 138))

    pygame.draw.rect(screen, GRAY, ((coords[0] + 350, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, BLACK, ((coords[0] + 350, coords[1] + 138), (70, 40)), 3)

    #Dibuja las casillas con números
    for row in range(3):
        for cell in range(12):
            colorCelda = RED if nums[row][cell] in numeros_vermells else GRAY
            pygame.draw.rect(screen, colorCelda, ((coords[0] + (35 * cell), coords[1] + (35 * row)), (35, 35)))
            pygame.draw.rect(screen, BLACK, ((coords[0] + (35 * cell), coords[1] + (35 * row)), (35, 35)), 3)
            txtNum = fuenteNum.render(str(nums[row][cell]), True, BLACK)

            screen.blit(txtNum, ((8 + coords[0] + (35 * cell), 8 + coords[1] + (35 * row))))
            #pygame.draw.circle(screen, colorFicha, ((16 + coords[0] + (35 * cell), 16 + coords[1] + (35 * row))), 10)
    

if __name__ == "__main__":
    main()