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

def getPopUpReady(historyBets_surface, screen):
    historyBets_surface.fill(bets.WHITE)
    #pygame.draw.rect(historyBets_surface, bets.BLACK, ((0, 0), (screen.get_width() - 100, screen.get_height() - 100)), 10)
    fuenteTitulo = pygame.font.SysFont('Arial', 62, True)
    historyBets_surface.blit(fuenteTitulo.render('Historial', True, bets.BLACK), (550, 50))

def drawPopUp(screen, historyBets_surface):

    fuenteTxt = pygame.font.SysFont('Arial', 20, True)

    #pygame.draw.rect(screen, bets.GREEN, ((15, 50), (100, 100)))
    #pygame.draw.rect(screen, bets.BLACK, ((15, 50), (100, 100)), 50)


    displacement = 1
    for linea in bets.historialBets:
        if linea != "":
            if linea[0] == ">":
                displacement += 1
            elif linea[0] == "N":
                displacement += 1
                txtLinea = fuenteTxt.render(linea, True, bets.BLACK)
                historyBets_surface.blit(txtLinea, (50, 50 + displacement * 30))
                
                continue

        txtLinea = fuenteTxt.render(linea, True, bets.BLACK)

        historyBets_surface.blit(txtLinea, (100 ,70 + displacement * 30))
        displacement += 1


        

