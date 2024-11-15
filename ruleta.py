#!/usr/bin/env python3

# Definim les constants
POSICIONS = 37
FILES = 3
CENTER = (450, 450)
RADI = 350

GREEN = (52, 220, 22)
RED = (220, 22, 22)
BLACK = (0, 0, 0)

# Definim les variables globals
numeros_vermells = [1, 3, 5, 6, 7, 12, 14, 16, 18, 19, 21, 22, 23, 25, 27, 30, 32, 34, 36]
ruleta_distribucio = []

# TODO: Hacer global para tener disponible desde cualquier archivo toda la ruleta (Añadir 'bets')
def init_ruleta():
    global ruleta_distribucip

    fila = 0

    for num in range(POSICIONS):
        # Definim el color de la casella a la ruleta
        if num in numeros_vermells:
            color = RED
        elif num == 0:
            color = GREEN
        else:
            color = BLACK

        posicio = {
            "number": num,                                  # Indica el propi número
            "row": 0 if num == 0 else fila,                 # Indica la fila a la que es troba per apostar, si el número es 0, la fila també serà 0
            "parity": "even" if num % 2 == 0 else "odd",    # Indica si el número es par o impar
            "color": color,                                 # Indica el color del que s'ha de pintar la casella
        }

        # Afegim el diccionari a la ruleta
        ruleta_distribucio.append(posicio)

        fila = 1 if fila == 3 else fila + 1

init_ruleta()
print("Finished")