#!/usr/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

import ruleta
import arrow
import button
import historic

DARK_GREEN = (21, 129, 36)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Ruleta Casino - Álvaro Armas & Alejandro López')

# Declaramos la variables
mouse = {
    "x": -1,
    "y": -1,
    "pressed": False,
    "released": False
}

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
    global mouse

    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse["x"], mouse["y"] = event.pos
            else:
                mouse["x"] = -1
                mouse["y"] = -1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["pressed"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False
            mouse["released"] = True
            
            # Cuando levantamos el click derecho del mouse, verificamos si nos encontramos encima del botón y si no se encuentra girando la ruleta.
            # De esta manera evitamos que se cominece el giro cada vez que pulsamos sobre el botón
            if button.is_hover_button(mouse) and not ruleta.is_spinning:
                ruleta.init_spin()
                arrow.reset_arrow_rotation()
            
    return True

def app_run():
    global mouse, is_spinning

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    # Cambiamos los diferentes estados en el que se puede encontrar el botón si estamos sobre él con el mouse y la ruleta no está girando
    if button.is_hover_button(mouse) and not ruleta.is_spinning:
        button.check_states(mouse)
    else:
        button.is_pressed = False
        button.is_hover = False

    # Si la ruleta se encuentra dando vuelta, tendremos el siguiente orden de actualización:
    #   1. Blink del botón Spin
    #   2. Rotación de la flecha
    #   3. Giro de la ruleta con la siguiente disminuación de la velocidad
    if ruleta.is_spinning:
        button.control_blink_animation(delta_time)
        arrow.control_rotation(delta_time, ruleta.ruleta_actual_speed, ruleta.ANGLE_HALF_STEP)
        ruleta.spin(delta_time)
    
    # Si la ruleta se acaba de parar, pondrá la variable 'has_stopped' a True, en ese entonces añadimos el número al histórico y seteamos esa variable a False otra vez
    if ruleta.has_stopped:
        historic.add_played_number(ruleta.get_winner_number())
        ruleta.reset_has_stopped()

def app_draw():
    global points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(DARK_GREEN)

    # Dibujamos todos los elementos necesarios por pantalla
    ruleta.draw_ruleta(screen)
    arrow.draw_arrow(screen)
    button.draw_button(screen, ruleta.is_spinning)
    historic.draw_historic(screen)

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()