from enum import Enum


class Direction(Enum):
    HAUT = 0
    DROITE = 1
    BAS = 2
    GAUCHE = 3

    def inverser(direction):
        return Direction((direction.value + 2) % 4)

    def estSensHoraire(d1, d2):
        return (d1.value - d2.value) % 4 == 3
