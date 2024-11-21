#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from ruleta import numeros_vermells, ruleta_distribucio, init_ruleta, winner_number
from jugadores import jugadores, printJugadores

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGRAY = (50, 50, 50)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 70)
SALMON = (227, 70, 104)
RED = (235, 0, 0)
GREEN = (51, 158, 63)
LIGHTGREEN = (10, 170, 10)
WALNUT = (115, 61, 27)
BLUE = (30, 30, 230)

affectedChip = "0"
bettingPlayer = "none"

pygame.init()
clock = pygame.time.Clock()

mouse = {"x": -1, "y": -1, "pressed": False, "dragging": False, "released": False}

#LOS NUMS DE LAS FILAS DE UNA RULETA REAL
nums = [[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36], 
        [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35], 
        [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]]
    

coordsBetTable = (250, 100)
coordsPrintJugadores = (200, 510)
coordsDrawPlayerChips = (180, 350)

# Definir la finestra
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Window Title')

chipSubsurface = pygame.Surface((WIDTH, HEIGHT))
surface = pygame.Surface((WIDTH, HEIGHT))

# Bucle de l'aplicació
def main():
    is_looping = True
    init_ruleta()
    surface.fill(WHITE)

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()
        comprobarResultados(winner_number)

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["pressed"] = True
            mouse["released"] = False

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False
            mouse["dragging"] = False
            mouse["released"] = True

        
    return True

# Fer càlculs

def app_run():
    isMouseClickOnChip()
    releaseChipOnCell()

def releaseChipOnCell():
    global affectedChip
    if affectedChip != "0" and mouse["released"]:
        #Si está soltando la ficha en el "0"
        if utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] - 50, "y": coordsBetTable[1], "width": 50, "height": 50}):
            if affectedChip not in ruleta_distribucio[0]["bets"][bettingPlayer].keys():
                ruleta_distribucio[0]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[0]["bets"][bettingPlayer][affectedChip] += 1



        #Si está soltando en uno de los cuadros de "Columnas"
        #Columna 1
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0], "y": coordsBetTable[1] + 35 * 3, "width": 140, "height": 40}):
            if affectedChip not in ruleta_distribucio[37]["bets"][bettingPlayer].keys():
                ruleta_distribucio[37]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[37]["bets"][bettingPlayer][affectedChip] += 1


        #Columna2
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] + 140, "y": coordsBetTable[1] + 35 * 3, "width": 140, "height": 40}):
            if affectedChip not in ruleta_distribucio[38]["bets"][bettingPlayer].keys():
                ruleta_distribucio[38]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[38]["bets"][bettingPlayer][affectedChip] += 1


        #Columna 3
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] + 280, "y": coordsBetTable[1] + 35 * 3, "width": 140, "height": 40}):
            if affectedChip not in ruleta_distribucio[39]["bets"][bettingPlayer].keys():
                ruleta_distribucio[39]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[39]["bets"][bettingPlayer][affectedChip] += 1


        #Si está soltando en Par, Impar o Colores
        #Pares
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] + 70, "y": coordsBetTable[1] + 35 * 4, "width": 70, "height": 40}):
            if affectedChip not in ruleta_distribucio[40]["bets"][bettingPlayer].keys():
                ruleta_distribucio[40]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[40]["bets"][bettingPlayer][affectedChip] += 1


        #Color Rojo
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] + 140, "y": coordsBetTable[1] + 35 * 4, "width": 70, "height": 40}):
            if affectedChip not in ruleta_distribucio[41]["bets"][bettingPlayer].keys():
                ruleta_distribucio[41]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[41]["bets"][bettingPlayer][affectedChip] += 1


        #Color Negro
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] + 210, "y": coordsBetTable[1] + 35 * 4, "width": 70, "height": 40}):
            if affectedChip not in ruleta_distribucio[42]["bets"][bettingPlayer].keys():
                ruleta_distribucio[42]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[42]["bets"][bettingPlayer][affectedChip] += 1


        #Impar
        elif utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsBetTable[0] + 280, "y": coordsBetTable[1] + 35 * 4, "width": 70, "height": 40}):
            if affectedChip not in ruleta_distribucio[43]["bets"][bettingPlayer].keys():
                ruleta_distribucio[43]["bets"][bettingPlayer][affectedChip] = 1
            else:
                ruleta_distribucio[43]["bets"][bettingPlayer][affectedChip] += 1


        #Si está soltando la ficha en un número de la tabla
        else:
            for row in range(3):
                for col in range(12):
                    if utils.is_point_in_rect({"x": mouse['x'], "y": mouse['y']}, {"x": coordsBetTable[0] + 35 * col, "y": coordsBetTable[1] + 35 * row, "width": 35, "height": 35}):

                        if affectedChip not in ruleta_distribucio[nums[row][col]]["bets"][bettingPlayer].keys():
                            ruleta_distribucio[nums[row][col]]["bets"][bettingPlayer][affectedChip] = 1
                        else:
                            ruleta_distribucio[nums[row][col]]["bets"][bettingPlayer][affectedChip] += 1

                        #print(ruleta_distribucio[nums[row][col]])

        #Que reste la ficha
        for jugador in jugadores:
            dicJugador = jugador
            if dicJugador["nom"] == bettingPlayer:
                jugador[affectedChip] -= 1
                    
        affectedChip = "0"


def isMouseClickOnChip():
    global affectedChip, bettingPlayer
    #Logica para el arrastre de las fichas


    if mouse["pressed"]:
        if not mouse["dragging"]:
            for jugador in jugadores:
                namePlayer = jugador["nom"]
                dicPlayer = jugador

                for dato in jugador.items():
                    if dato[0] != "nom":
                        coordsChips005 = (coordsDrawPlayerChips[0] + 250 * jugadores.index(jugador) - 50, coordsDrawPlayerChips[1] + 40)
                        coordsChips010 = (coordsDrawPlayerChips[0] + 250 * jugadores.index(jugador) - 50 + 35, coordsDrawPlayerChips[1] + 40)
                        coordsChips020 = (coordsDrawPlayerChips[0] + 250 * jugadores.index(jugador) - 50 + 35 * 2, coordsDrawPlayerChips[1] + 40)
                        coordsChips050 = (coordsDrawPlayerChips[0] + 250 * jugadores.index(jugador) - 50 + 35 * 3, coordsDrawPlayerChips[1] + 40)
                        coordsChips100 = (coordsDrawPlayerChips[0] + 250 * jugadores.index(jugador) - 50 + 35 * 4, coordsDrawPlayerChips[1] + 40)
                        
                        coordsChips005RectY = dicPlayer["005"] * 10 + 10
                        coordsChips010RectY = dicPlayer["010"] * 10 + 10
                        coordsChips020RectY = dicPlayer["020"] * 10 + 10
                        coordsChips050RectY = dicPlayer["050"] * 10 + 10
                        coordsChips100RectY = dicPlayer["100"] * 10 + 10
                            
                        if (utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsChips005[0], "y": coordsChips005[1], "width": 20, "height": coordsChips005RectY})
                            and dicPlayer["005"] != 0 and not mouse["dragging"]):
                            mouse["dragging"] = True
                            affectedChip = "005"
                            bettingPlayer = dicPlayer["nom"]

                        elif (utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsChips010[0], "y": coordsChips005[1], "width": 20, "height": coordsChips010RectY})
                            and dicPlayer["010"] != 0 and not mouse["dragging"]):
                            mouse["dragging"] = True
                            affectedChip = "010"
                            bettingPlayer = dicPlayer["nom"]

                        elif (utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsChips020[0], "y": coordsChips005[1], "width": 20, "height": coordsChips020RectY})
                            and dicPlayer["020"] != 0 and not mouse["dragging"]):
                            mouse["dragging"] = True
                            affectedChip = "020"
                            bettingPlayer = dicPlayer["nom"]

                        elif (utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsChips050[0], "y": coordsChips005[1], "width": 20, "height": coordsChips050RectY})
                            and dicPlayer["050"] != 0 and not mouse["dragging"]):
                            mouse["dragging"] = True
                            affectedChip = "050"
                            bettingPlayer = dicPlayer["nom"]

                        elif (utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coordsChips100[0], "y": coordsChips005[1], "width": 20, "height": coordsChips100RectY})
                            and dicPlayer["100"] != 0 and not mouse["dragging"]):
                            mouse["dragging"] = True
                            affectedChip = "100"
                            bettingPlayer = dicPlayer["nom"]

                        

        else:
            if affectedChip:
                drawChipOnCursor(affectedChip)

def drawChipOnCursor(chip):
    if chip == "005":
        pygame.draw.circle(screen, RED, (mouse["x"], mouse["y"]), 20)
    elif chip == "010":
        pygame.draw.circle(screen, BLUE, (mouse["x"], mouse["y"]), 20)
    elif chip == "020":
        pygame.draw.circle(screen, GREEN, (mouse["x"], mouse["y"]), 20)
    elif chip == "050":
        pygame.draw.circle(screen, WALNUT, (mouse["x"], mouse["y"]), 20)
    elif chip == "100":
        pygame.draw.circle(screen, DARKGRAY, (mouse["x"], mouse["y"]), 20)

    pygame.draw.circle(screen, BLACK, (mouse["x"], mouse["y"]), 20, 4)
    

    pygame.display.update()



# Dibuixar 
def app_draw():
    screen.fill(WHITE)
    utils.draw_grid(pygame, screen, 50)
    drawBetTable((250, 100))
    printJugadores((200, 510))
    drawPlayerChips((180, 350))
    drawBets((800, 100))
    #screen.blit(chipSubsurface, (0, 0))
    if affectedChip != "0":
        drawChipOnCursor(affectedChip)
    pygame.display.update()


def drawBets(coords): #Dibuja el historial de apuestas en la ronda
    colorNum = BLACK
    fuenteTxt = pygame.font.SysFont('Arial', 16, True)
    displacement = 0
    for numero in ruleta_distribucio:
        #Comprobar si el número tiene alguna apuesta.
        check = 0
        for dato in list(numero["bets"].values()): #Esto comprueba si los 3 valores de la apuesta de un número están vacíos
            if dato == {}:
                check += 1

        if check != 3: #En caso de que al menos uno no esté vacío, esto se ejecuta
            #Dibuja el número
            txt = f"Apuesta en {str(numero["number"])}:"
            txtNumero = fuenteTxt.render(txt, True, colorNum)
            screen.blit(txtNumero, (coords[0], coords[1] + displacement * 70))

            #Dibuja las apuestas
            for bet in numero["bets"].items():
                if bet[1] != {}: #Esto comprueba que el 2do item (El diccionario de apuestas) no esté vacío.
                    #txtNombre = fuenteTxt.render(f"{bet[0]}:", True, colorNum)
                    #txtApuestas = fuenteTxt.render("\n".join(list(bet[1])), True, colorNum)

                    suma = 0
                    for item in bet[1].items():
                        ficha = item[0]
                        cantidad = item[1]
                        #print(type(ficha))
                        #print(type(cantidad))
                        ficha = int(ficha)
                        

                        suma += ficha * cantidad
                    txtNombre = fuenteTxt.render(f"{bet[0]}: {suma}", True, colorNum)
                    #txtApuestas = fuenteTxt.render("\n".join(list(bet[1])), True, colorNum)
                    
                    screen.blit(txtNombre, (coords[0], 20 + coords[1] + displacement * 70))
                    #screen.blit(txtApuestas, (coords[0] + 60, 20 + coords[1] + displacement * 50))
                    

            displacement += 1

        
def drawBetTable(coords):
    global nums
    """Las coordenadas son donde quieres que esté la esquina superior izquierda de la casilla '3' de la tabla"""

    colorCeldaOutline = BLACK
    colorCeldaNotNumber = GREEN
    colorTable = GREEN

    
    fuenteNum = pygame.font.SysFont('Arial', 16, True)

    #Dibujar la "mesa"
    pygame.draw.rect(screen, colorTable, ((coords[0] - 100, coords[1] - 40), (100 + 35 * 12 + 100, 50 + 35 * 3 + 100)))
    pygame.draw.rect(screen, colorCeldaOutline, ((coords[0] - 100, coords[1] - 40), (100 + 35 * 12 + 100, 50 + 35 * 3 + 100)), 10)

    #Dibuja lo que está alrededor del tablero que no son las casillas con números
    txt0 = fuenteNum.render('0', True, BLACK)
    pointsLines1 = [(coords[0], coords[1]), (coords[0] - 25, coords[1]), (coords[0] - 50, coords[1] + 25), (coords[0] - 25, coords[1] + 50), (coords[0], coords[1] + 50)]
    pygame.draw.polygon(screen, LIGHTGREEN, pointsLines1)
    pygame.draw.lines(screen, colorCeldaOutline, False, pointsLines1, 2)
    screen.blit(txt0, (coords[0] - 20, coords[1] + 17))


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
    
    #Dibujando la "mesa"
    colorTable = GREEN
    #pygame.draw.rect(screen, colorTable, ((coords[0] - 100, coords[1] - 50), (770, 220)))
    #pygame.draw.rect(screen, BLACK, ((coords[0] - 100, coords[1] - 50), (770, 220)), 10)

    #Todo lo demás
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

def comprobarResultados(winnerNumber):
    

    #winnerNumber es un dict
    if winner_number != None:
        colorGanador = winner_number["color"]
        parityGanadora = winner_number["parity"]

    for numero in ruleta_distribucio:
        apuestasNumero = numero["bets"].items()

        #Comprobar que el número tiene apuestas
        check = 0
        for dato in apuestasNumero:
            if dato[1] != {}:
                check += 1
        
        #Si check es mayor a 0 tiene apuestas
        if check > 0:
            #Comprueba si es el mismo color
            if numero["number"] == "a":
                pass
            if numero["color"] == winner_number["color"]:
                print("color ganador")

            #Comprueba si la paridad es la misma
            if numero["parity"] == winner_number["parity"]:
                print("paridad ganadora")

            #Esto comprueba si el número es el mismo que en el que está la apuesta
            if winner_number["number"] == numero["number"]:
                print("mismo numero")

            #Comprueba si la apuesta 


if __name__ == "__main__":
    main()