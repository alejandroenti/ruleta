import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import bets
import ruleta
import arrow
import button
import historic
import jugadores
import utils

ALMOSTWHITE = (200, 200, 200)

def drawButton(screen, coords):
    width = 100
    height = 50

    fuente = pygame.font.SysFont('Arial', 16, True)

    pygame.draw.rect(screen, bets.WHITE, ((coords[0], coords[1]), (width, height)))
    pygame.draw.rect(screen, bets.BLACK, ((coords[0], coords[1]), (width, height)), 7)

    txtHistorial = fuente.render("Historial", True, bets.BLACK)

    screen.blit(txtHistorial, (coords[0] + 17, coords[1] + 17))

def isClickOnButton(screen, mouse, coords):
    if utils.is_point_in_rect({"x": mouse["x"], "y": mouse["y"]}, {"x": coords[0], "y": coords[1], "width": 100, "height": 50}):
        return True
    else:
        return False
    
def drawPopUp(screen):
    width = screen.get_width()
    height = screen.get_height()
    
    fuenteTxt = pygame.font.SysFont('Arial', 20, True)

    pygame.draw.rect(screen, ALMOSTWHITE, ((50, 50), (width - 100, height - 100)))
    pygame.draw.rect(screen, bets.BLACK, ((50, 50), (width - 100, height - 100)), 20)

    displacement = 0
    for linea in bets.historialBets:
        if linea[0] == ">":
            displacement += 1

        txtLinea = fuenteTxt.render(linea, True, bets.BLACK)

        screen.blit(txtLinea, (100 ,70 + displacement * 30))
        displacement += 1


        

