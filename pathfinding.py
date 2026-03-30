import sys
from enum import Enum


Inf = sys.maxsize


class Direction(Enum):
    HAUT = 1
    BAS = -1
    GAUCHE = 2
    DROIT = -2


class Noeud:
    def __init__(self, distance=Inf, prec=None, vu=False):
        self.distance = distance
        self.prec = prec
        self.vu = vu


class Graphe:
    def __init__(self, n):
        self.__data = [[(0 if i == j else Inf, None) for i in n] for j in n]

    def ajouter(self, p1, p2, distance, direction):
        self.__data[p1][p2] = (distance, direction)
        self.__data[p2][p1] = (distance, direction * -1)

    def trouver_chemin(self, debut, fin):
        noeuds = [Noeud() for _ in range(len(self.__data))]
        noeuds[debut].distance = 0
        courant = debut

        while not noeuds[fin].vu:
            courant = min(noeuds, key=lambda v: Inf if v.vu else v.distance)


graphe = Graphe(14)
for arc in [
    (1, 2, 2, Direction.DROIT),
    (2, 3, 2, Direction.BAS),
    (1, 6, 3, Direction.BAS),
    (3, 4, 4, Direction.DROIT),
    (3, 7, 2, Direction.BAS),
    (4, 9, 2, Direction.BAS),
    (5, 6, 3, Direction.DROIT),
    (5, 10, 2, Direction.BAS),
    (6, 11, 2, Direction.BAS),
    (7, 8, 2, Direction.DROIT),
    (7, 13, 4, Direction.BAS),
    (8, 9, 2, Direction.DROIT),
    (8, 14, 4, Direction.BAS),
    (10, 11, 3, Direction.DROIT),
    (10, 12, 9.28, Direction.GAUCHE),
    (11, 12, 3, Direction.BAS),
    (12, 13, 2, Direction.DROIT),
    (13, 14, 2, Direction.DROIT),
]:
    graphe.ajouter(arc[0], arc[1], arc[2], arc[3])
