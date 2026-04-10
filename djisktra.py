from sys import maxsize
from direction import Direction


Inf = maxsize


class Noeud:
    def __init__(self, distance=Inf, prec=None, vu=False):
        self.distance = distance
        self.prec = prec
        self.vu = vu

    def regarder(self, distance, prec):
        if (distance < self.distance):
            self.distance = distance
            self.prec = prec


class Graphe:
    def __init__(self, n):
        self.__distances = [[(0 if i == j else Inf, None) for i in range(n)] for j in range(n)]

    def ajouter(self, p1, p2, distance, direction):
        p1 -= 1
        p2 -= 1
        self.__distances[p1][p2] = (distance, direction)
        self.__distances[p2][p1] = (distance, Direction.inverser(direction))

    def trouver_chemin(self, debut, fin):
        fin -= 1

        noeuds = [Noeud() for _ in range(len(self.__distances))]
        courant = debut - 1
        noeuds[courant].distance = 0

        while courant != fin:
            courant = min(range(len(noeuds)), key=lambda n: Inf if noeuds[n].vu else noeuds[n].distance)
            noeuds[courant].vu = True

            for n, distance in enumerate(self.__distances[courant]):
                noeuds[n].regarder(distance[0] + noeuds[courant].distance, courant)

        chemin = []
        while noeuds[courant].prec is not None:
            prec = noeuds[courant].prec
            chemin.append(self.__distances[prec][courant][1])
            courant = prec

        return chemin


graphe = Graphe(14)
for arc in [
    (1, 2, 2, Direction.DROITE),
    (2, 3, 2, Direction.BAS),
    (1, 6, 3, Direction.BAS),
    (3, 4, 4, Direction.DROITE),
    (3, 7, 2, Direction.BAS),
    (4, 9, 2, Direction.BAS),
    (5, 6, 3, Direction.DROITE),
    (5, 10, 2, Direction.BAS),
    (6, 11, 2, Direction.BAS),
    (7, 8, 2, Direction.DROITE),
    (7, 13, 4, Direction.BAS),
    (8, 9, 2, Direction.DROITE),
    (8, 14, 4, Direction.BAS),
    (10, 11, 3, Direction.DROITE),
    (10, 12, 9.28, Direction.GAUCHE),
    (11, 12, 3, Direction.BAS),
    (12, 13, 2, Direction.DROITE),
    (13, 14, 2, Direction.DROITE),
]:
    graphe.ajouter(*arc)  # https://stackoverflow.com/questions/48451228/how-to-spread-a-python-array
