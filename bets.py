#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from ruleta import numeros_vermells, ruleta_distribucio
from jugadores import jugadores, printJugadores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (50, 50, 50)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
SALMON = (227, 70, 104)
RED = (235, 0, 0)
GREEN = (51, 158, 63)
WALNUT = (115, 61, 27)
BLUE = (30, 30, 230)

pygame.init()
clock = pygame.time.Clock()

mouse = {"x": -1, "y": -1, "pressed": False}

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
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_focused():
                mouse['x'] = event.pos[0]
                mouse['y'] = event.pos[1]
            else:
                mouse['x'] = -1
                mouse['y'] = -1

        
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    drawBetTable((250, 100))
    printJugadores((200, 510))
    drawPlayerChips((180, 350))
    pygame.display.update()

def makeBet(player, posicio):
    pass

def drawBetTable(coords):
    global nums
    """Las coordenadas son donde quieres que esté la esquina superior izquierda de la casilla '3' de la tabla"""

    colorCeldaOutline = BLACK
    colorCeldaNotNumber = GREEN
    colorTable = GREEN

    #LOS NUMS DE LAS FILAS DE UNA RULETA REAL
    nums = [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36], 
            [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35], 
            [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]
    
    fuenteNum = pygame.font.SysFont('Arial', 16, True)

    #Dibujar la "mesa"
    pygame.draw.rect(screen, colorTable, ((coords[0] - 100, coords[1] - 40), (100 + 35 * 12 + 100, 50 + 35 * 3 + 100)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] - 100, coords[1] - 40), (100 + 35 * 12 + 100, 50 + 35 * 3 + 100)), 10)

    #Dibuja lo que está alrededor del tablero que no son las casillas con números
    txt0 = fuenteNum.render('0', True, BLACK)
    pointsLines1 = [(coords[0], coords[1]), (coords[0] - 25, coords[1]), (coords[0] - 50, coords[1] + 25), (coords[0] - 25, coords[1] + 50), (coords[0], coords[1] + 50)]
    pygame.draw.polygon(screen, colorCeldaNotNumber, pointsLines1)
    pygame.draw.lines(screen, colorCeldaOutline, False, pointsLines1, 2)
    screen.blit(txt0, (coords[0] - 20, coords[1] + 17))

    txt00 = fuenteNum.render('00', True, BLACK)
    pointsLines2 = [(coords[0], coords[1] + 50), (coords[0] - 25, coords[1] + 50), (coords[0] - 50, coords[1] + 75), (coords[0] - 25, coords[1] + 100), (coords[0], coords[1] + 100)]
    pygame.draw.polygon(screen, colorCeldaNotNumber, pointsLines2)
    pygame.draw.lines(screen, colorCeldaOutline, False, pointsLines2, 2)
    screen.blit(txt00, (coords[0] - 25, coords[1] + 67))

    #Dibuja los tres rectangulos de debajo
    txtColumna1 = fuenteNum.render('Columna 1', True, BLACK)
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0], coords[1] + 100), (140, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0], coords[1] + 100), (140, 40)), 3)
    screen.blit(txtColumna1, (27 + coords[0], 12 + coords[1] + 100))

    txtColumna2 = fuenteNum.render('Columna 2', True, BLACK)
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 140, coords[1] + 100), (140, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 140, coords[1] + 100), (140, 40)), 3)
    screen.blit(txtColumna2, (27 + coords[0] + 140, 12 + coords[1] + 100))
    
    txtColumna3 = fuenteNum.render('Columna 3', True, BLACK)
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 280, coords[1] + 100), (140, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 280, coords[1] + 100), (140, 40)), 3)
    screen.blit(txtColumna3, (27 + coords[0] + 280, 12 + coords[1] + 100))

    #Dibuja los tres cuadrados a la derecha de las casillas
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 35 * 12, coords[1]), (35, 35)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 35 * 12, coords[1]), (35, 35)), 3)

    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 35 * 12, coords[1] + 35), (35, 35)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 35 * 12, coords[1] + 35), (35, 35)), 3)

    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 35 * 12, coords[1] + 70), (35, 35)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 35 * 12, coords[1] + 70), (35, 35)), 3)

    #Dibuja los seis rectangulos de debajo de los tres rectangulos
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0], coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0], coords[1] + 138), (70, 40)), 3)

    txtPares = fuenteNum.render("Pares", True, BLACK)
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 70, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 70, coords[1] + 138), (70, 40)), 3)
    screen.blit(txtPares, (12 + coords[0] + 70, 10 + coords[1] + 138))

    pygame.draw.rect(screen, RED, ((coords[0] + 140, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 140, coords[1] + 138), (70, 40)), 3)

    pygame.draw.rect(screen, DARKGRAY, ((coords[0] + 210, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 210, coords[1] + 138), (70, 40)), 3)

    txtImpares = fuenteNum.render("Impares", True, BLACK)
    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 280, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 280, coords[1] + 138), (70, 40)), 3)
    screen.blit(txtImpares, (4 + coords[0] + 280, 10 + coords[1] + 138))

    pygame.draw.rect(screen, colorCeldaNotNumber, ((coords[0] + 350, coords[1] + 138), (70, 40)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + 350, coords[1] + 138), (70, 40)), 3)

    #Dibuja las casillas con números
    colorOffset = 20
    for row in range(3):
        for cell in range(12):
            colorCelda = RED if nums[row][cell] in numeros_vermells else DARKGRAY
            
            #Esto se puede borrar, lo que hace es que si el mouse está encima de una celda en específico, esa celda se "ilumina"
            #Posiblemente esto sea algo que se borre, a menos que esta función se llame en cada frame, si no es así esto es bastante inutil.
            if utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coords[0], "y": coords[1], "width": 35 * 12, "height": 35 * 3}):
                if utils.is_point_in_rect({"x": mouse['x'], "y": mouse['y']}, {"x": coords[0] + 35 * cell, "y": coords[1] + 35 * row, "width": 35, "height": 35}):
                    listColorcelda = list(colorCelda)
                    listColorcelda[0] += colorOffset
                    listColorcelda[1] += colorOffset
                    listColorcelda[2] += colorOffset

                    colorCelda = tuple(listColorcelda)

            pygame.draw.rect(screen, colorCelda, ((coords[0] + (35 * cell), coords[1] + (35 * row)), (35, 35)))
            pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] + (35 * cell), coords[1] + (35 * row)), (35, 35)), 3)

            txtNum = fuenteNum.render(str(nums[row][cell]), True, WHITE if colorCelda != RED and colorCelda != (RED[0] + colorOffset, RED[1] + colorOffset, RED[2] + colorOffset) else BLACK)

            screen.blit(txtNum, ((8 + coords[0] + (35 * cell), 8 + coords[1] + (35 * row))))

            if cell * row in ruleta_distribucio:#["bets"]:
                pass #Aquí habría que hacer que los números que tengan bets se le pongan las fichas que se han apostado encima de los números.

            
def drawPlayerChips(coords):
    txtPlayerName = pygame.font.SysFont('Arial', 18, True)
    for jugador in jugadores:
        txtName = txtPlayerName.render(jugador["nom"], True, BLACK)
        screen.blit(txtName, (coords[0] + 250 * jugadores.index(jugador), coords[1]))


        for dato in jugador.items():
            if dato[0] != "nom":
                if dato[1] != 0: #Esto comprueba que el número de fichas no sea 0
                    for ficha in range(dato[1]):
                        coordsChip = (coords[0] + 250 * jugadores.index(jugador) - 40, coords[1] + 50 + (ficha * 10))
                        if dato[0] == "005":
                            pygame.draw.circle(screen, RED, coordsChip, 15)
                            pygame.draw.circle(screen, BLACK, coordsChip, 15, 3)
                        elif dato[0] == "010":
                            pygame.draw.circle(screen, BLUE, (coordsChip[0] + 35, coordsChip[1]), 15)
                            pygame.draw.circle(screen, BLACK,(coordsChip[0] + 35, coordsChip[1]), 15, 3)
                        elif dato[0] == "020":
                            pygame.draw.circle(screen, GREEN, (coordsChip[0] + 35 * 2, coordsChip[1]), 15)
                            pygame.draw.circle(screen, BLACK,(coordsChip[0] + 35 * 2, coordsChip[1]), 15, 3)
                        elif dato[0] == "050":
                            pygame.draw.circle(screen, WALNUT, (coordsChip[0] + 35 * 3, coordsChip[1]), 15)
                            pygame.draw.circle(screen, BLACK,(coordsChip[0] + 35 * 3, coordsChip[1]), 15, 3)
                        elif dato[0] == "100":
                            pygame.draw.circle(screen, DARKGRAY, (coordsChip[0] + 35 * 4, coordsChip[1]), 15)
                            pygame.draw.circle(screen, BLACK,(coordsChip[0] + 35 * 4, coordsChip[1]), 15, 3)
                            
if __name__ == "__main__":
    main()