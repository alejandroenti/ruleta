#!/usr/bin/env python3

import pygame

# Definimos las constantes
BUTTON_EXTERIOR = (450, 60, 150, 75)
BUTTON_INTERIOR = (460, 70, 130, 55)
PADDING = 2

TITLE_TEXT_RECT = (525, 100, 500, 150)

TITLE_TEXT = "CASINO ROULETTE"

TITLE_BLINK_ANIMATION = 0.1
TITLE_LIGHT_SIZE = 50
TITLE_BLINK_ALL_STEP = 6

TOTAL_LIGHTS = 26

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (228, 223, 222)
RED = (248, 64, 64)
RED_DARK = (175, 20, 20)

# Definimos las variables
animation_timer = 0
animation_state = 0
animation_all_step = 0
animation_color = 0
animation_title_brightness = 0

lights = []
lights_limits = [
    TITLE_TEXT_RECT[0] + TITLE_TEXT_RECT[2] - TITLE_LIGHT_SIZE / 2 + 1,
    TITLE_TEXT_RECT[1] + TITLE_TEXT_RECT[3] - TITLE_LIGHT_SIZE / 2 + 1,
    TITLE_TEXT_RECT[0] - TITLE_LIGHT_SIZE / 2 - 1,
    TITLE_TEXT_RECT[1] + TITLE_LIGHT_SIZE / 2 - 1
]
current_light = 0

font_ruleta = pygame.font.SysFont("Arial", 48)

def init_lights():
    '''Inicializamos las luces que estarán alrededor del título y se irán encendiendo y apagando.

    Retorna: None'''

    global lights, lights_limits

    # Configuramos la posición incial de la primera luz
    pos_x = TITLE_TEXT_RECT[0] - TITLE_LIGHT_SIZE / 2
    pos_y = TITLE_TEXT_RECT[1] - TITLE_LIGHT_SIZE / 2

    # Inicializamos el índice de la luz y el límite en el que nos encontramos de la lista de lights_limits
    index = 0
    limit = 0

    while True:
        # Configuramos los 2 colores que puede llegar a tener la luz según su índice
        if index % 2 == 0:
            colors = [GRAY, WHITE]
        else:
            colors = [RED_DARK, RED]

        # Generamos el diccionario con todas sus propiedades
        light = {
            "x": pos_x,
            "y": pos_y,
            "width": TITLE_LIGHT_SIZE,
            "height": TITLE_LIGHT_SIZE,
            "colors": colors,
            "brightness": 0 if index != 0 else 1,
            "border_radius": "top left" if index == 0 else ""
        }

        # Verificamos si nos encontramos en un límite:
        #   Si nos encontramos, deberemos pasar de límite, aumentar la posición como si fuera el siguiente límite y poner el border radius correspondiente
        #       Si es el último límite, sólo añadimos la luz a la lista y salimos
        #   Si no nos encontramos en un límite, deberemos aumentar la posición en la dirección que toque
        if limit == 0:
            if pos_x + TITLE_LIGHT_SIZE >= lights_limits[limit]:
                limit += 1
                pos_y += TITLE_LIGHT_SIZE
                light["border_radius"] = "top right"
            else:
                pos_x += TITLE_LIGHT_SIZE
        elif limit == 1:
            if pos_y + TITLE_LIGHT_SIZE >= lights_limits[limit]:
                limit += 1
                pos_x -= TITLE_LIGHT_SIZE
                light["border_radius"] = "bottom right"
            else:
                pos_y += TITLE_LIGHT_SIZE
        elif limit == 2:
            if pos_x - TITLE_LIGHT_SIZE <= lights_limits[limit]:
                limit += 1
                pos_y -= TITLE_LIGHT_SIZE
                light["border_radius"] = "bottom left"
            else:
                pos_x -= TITLE_LIGHT_SIZE
        elif limit == 3:
            if pos_y - TITLE_LIGHT_SIZE <= lights_limits[limit]:
                lights.append(light)
                break
            else:
                pos_y -= TITLE_LIGHT_SIZE

        # Aádimos la luz a la lista y aumentamos el índice para la siguiente luz
        lights.append(light)
        index += 1


def draw_title(screen):
    '''Dibujamos el título de la Aplicación

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    # Dibujamos las luces del título
    draw_lights(screen)

    # Dibujamos el rectángulo con el texto
    color = RED_DARK if animation_title_brightness == 0 else RED
    pygame.draw.rect(screen, color, TITLE_TEXT_RECT, border_radius=32)
    pygame.draw.rect(screen, BLACK, TITLE_TEXT_RECT, 4, border_radius=32)

    # Añadimos el texto
    string_surface = font_ruleta.render(TITLE_TEXT, True, WHITE)
    string_rect = string_surface.get_rect()

    # Centramos el texto
    center = (TITLE_TEXT_RECT[0] + TITLE_TEXT_RECT[2] / 2, TITLE_TEXT_RECT[1] + TITLE_TEXT_RECT[3] / 2)
    string_rect.centerx = center[0]
    string_rect.centery = center[1]

    screen.blit(string_surface, string_rect)

def draw_lights(screen):
    '''Dibujamos las luces que se encuentran alrededor del títutlo.

    Input:
        -screen(): Superfície del Pygame.

    Retorna: None'''

    for light in lights:
        # Generamos el rect de la luz actual
        rect = (light["x"], light["y"], light["width"], light["height"])

        # Verificamos si la luz se encuentra en uno de los límites por si tiene border_radius
        if len(light["border_radius"]) > 0:
            # Separamos el contenido e imprimos la luz con los bordes correspondientes
            coords = light["border_radius"].split()
            if coords[0] == "top":
                if coords[1] == "left":
                    pygame.draw.rect(screen, light["colors"][light["brightness"]], rect, border_top_left_radius=32)      
                    pygame.draw.rect(screen, BLACK, rect, 4, border_top_left_radius=32)
                elif coords[1] == "right":
                    pygame.draw.rect(screen, light["colors"][light["brightness"]], rect, border_top_right_radius=32)      
                    pygame.draw.rect(screen, BLACK, rect, 4, border_top_right_radius=32)
            elif coords[0] == "bottom":
                if coords[1] == "left":
                    pygame.draw.rect(screen, light["colors"][light["brightness"]], rect, border_bottom_left_radius=32)      
                    pygame.draw.rect(screen, BLACK, rect, 4, border_bottom_left_radius=32)
                elif coords[1] == "right":
                    pygame.draw.rect(screen, light["colors"][light["brightness"]], rect, border_bottom_right_radius=32)      
                    pygame.draw.rect(screen, BLACK, rect, 4, border_bottom_right_radius=32)
        else:
            # En caso que no tenga border_radius imprimimos de manera normal la luz con su rect cuadrado
            pygame.draw.rect(screen, light["colors"][light["brightness"]], rect)      
            pygame.draw.rect(screen, BLACK, rect, 4)


def control_blink_animation(delta_time):
    '''Controlamos la animación de parpadeo de las luces. Tendrás dos variantes, una luz sóla parpadeando y todas las luces con el fondo del título.

    Input:
        -delta_time(float): Tiempo entre fotogramas calculado por Pygame.

    Retorna: None'''

    global animation_timer, animation_state, animation_all_step, animation_title_brightness, current_light, lights

    # Aumentamos el temporizador de la animación
    animation_timer += delta_time
    
    # Si hemos llegado al límite del parpadeo, verificaremos en que estado nos encontramos antes de realizar ninguna acción.
    if animation_timer >= TITLE_BLINK_ANIMATION:
        if animation_state == 0:
            # Si no nos encontramos en la última luz (TOTAL_LIGHTS - 1), apagaremos la luz actual y encederemos la siguiente
            if current_light < TOTAL_LIGHTS - 1:
                lights[current_light]["brightness"] = 0
                current_light += 1
                lights[current_light]["brightness"] = 1
            else:
                # Si estamos en la última, cambiamos de animación
                animation_state = 1
        else:
            # Si no nos encontramos en el último apagón, encederemos o apagaremos todas as luces
            if animation_all_step <= TITLE_BLINK_ALL_STEP:
                for light in lights:
                    light["brightness"] = 0 if animation_all_step % 2 == 0 else 1
                animation_title_brightness = (animation_title_brightness + 1) % 2
                animation_all_step += 1
            else:
                # Si estamos en el último, reseteamos los apagones y pasamos a la anterior animación, seteando la luz actual a la primera
                animation_state = 0
                animation_all_step = 0
                animation_title_brightness = 0
            current_light = 0
        
        # Siempre que entremos, deberemos resetear el contador para que vuelva a esperar el tiempo que queremos
        animation_timer = 0