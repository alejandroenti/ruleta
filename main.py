#!/usr/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

import ruleta

WHITE = (255, 255, 255)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Ruleta Casino - Álvaro Armas & Alejandro López')

# Bucle de l'aplicació
def main():
    is_looping = True

    ruleta.init_ruleta()

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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ruleta.init_spin()
    
    return True

def app_run():
    global is_spinning

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    if ruleta.is_spinning:
        ruleta.spin(delta_time)

def app_draw():
    global points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(WHITE)

    ruleta.draw_ruleta(screen)
    ruleta.draw_arrow(screen)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()