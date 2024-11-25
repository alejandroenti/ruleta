#!/usr/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

import ruleta
import arrow
import button
import historic
import jugadores
import bets
import title

DARK_GREEN = (21, 129, 36)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1500, 844))
pygame.display.set_caption('Ruleta Casino - Álvaro Armas & Alejandro López')

# Declaramos las diferentes surfaces
bets_surface = pygame.Surface((175, 90 * 44 + 15), pygame.SRCALPHA)   # Configuramos surface a la altura de la tabla
bets_surface.fill((222, 222, 222))

# Declaramos la variables
mouse = {
    "x": -1,
    "y": -1,
    "pressed": False,
    "released": False,
    "dragging": False
}

scroll = {
    "percentage": 0,
    "dragging": False,
    "x": 1450,
    "y": 260,
    "width": 5,
    "height": 255,
    "radius": 8,
    "surface_offset": 0,
    "visible_height": 255
}

# Bucle de l'aplicació
def main():
    is_looping = True

    ruleta.init_ruleta()
    title.init_lights()

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
            mouse["released"] = False

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False
            mouse["dragging"] = False
            mouse["released"] = True

            # Cuando levantamos el click derecho del mouse, verificamos si nos encontramos encima del botón y si no se encuentra girando la ruleta.
            # De esta manera evitamos que se cominece el giro cada vez que pulsamos sobre el botón
            if button.is_hover_button(mouse) and not ruleta.is_spinning:
                ruleta.init_spin()
                arrow.reset_arrow_rotation()
            
    return True

def app_run():
    global mouse, is_spinning, bets_surface

    delta_time = clock.get_time() / 1000.0  # Convertir a segons

    manage_scroll()
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
        #print(ruleta.get_winner_number())
        bets.comprobarResultados(ruleta.get_winner_number())
        historic.add_played_number(ruleta.get_winner_number())
        bets.clearBets()
        bets_surface.fill((222, 222, 222))
        ruleta.reset_has_stopped()
        
    
    historic.control_animations(delta_time)
    """
    if not ruleta.is_spinning:
        bets.releaseChipOnCell(mouse) #Por motivos de comodidad al programar, esto es mejor comentado, pero a la hora de la verdad descomentarlo
    """
    bets.releaseChipOnCell(mouse)
    title.control_blink_animation(delta_time)
    
def app_draw():
    global bets_surface, points, buttons_width, buttons_color, padding, selected_color

    # Pintar el fons de blanc
    screen.fill(DARK_GREEN)

    sub_bets_surface = bets_surface.subsurface((0, scroll["surface_offset"], bets_surface.get_width(), scroll["visible_height"]))
    screen.blit(sub_bets_surface, (1250, 260))

    # Dibujamos todos los elementos necesarios por pantalla
    ruleta.draw_ruleta(screen)
    arrow.draw_arrow(screen)
    button.draw_button(screen, ruleta.is_spinning)
    historic.draw_historic(screen)
    jugadores.printJugadores(screen, (35, 635))

    bets.drawBetTable(mouse, screen, (720, 300))
    bets.drawBets(bets_surface, (10, 5))
    bets.drawPlayerChips(screen, (620, 550))
    
    """if not ruleta.is_spinning:
        bets.isMouseClickOnChip(screen, mouse) #Por motivos de comodidad al programar, esto es mejor comentado, pero a la hora de la verdad descomentarlo
    """
    bets.isMouseClickOnChip(screen, mouse) #Cambiada posición porque el problema sería que estaba detrás del resto de cosas y no se veía

    title.draw_title(screen)

    draw_scroll()
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

def manage_scroll():
    global scroll

    radi = scroll["radius"]
    center = {
        "x": int(scroll["x"] + scroll["width"] / 2),
        "y": int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"])
    }

    if mouse["pressed"] and not scroll["dragging"] and utils.is_point_in_circle(mouse, center, radi):
        scroll["dragging"] = True

    if not mouse["pressed"]:
        scroll["dragging"] = False

    if scroll["dragging"]:
        relative_y = max(min(mouse["y"], scroll["y"] + scroll["height"]), scroll["y"])
        scroll["percentage"] = ((relative_y - scroll["y"]) / scroll["height"]) * 100

    scroll["surface_offset"] = int((scroll["percentage"] / 100) * (bets_surface.get_height() - scroll["visible_height"]))

def draw_scroll():
    rect = (scroll["x"], scroll["y"], scroll["width"], scroll["height"])

    center = (scroll["x"] + scroll["width"] / 2, int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"]))
    radius = scroll["radius"]

    pygame.draw.rect(screen, GRAY, rect)
    pygame.draw.circle(screen, BLACK, center, radius)

if __name__ == "__main__":
    main()