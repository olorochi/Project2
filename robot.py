from direction import Direction


class Robot:
    def __init__(self, gauche, droit, capteur_ir, direction):
        self.__capteur_ir = capteur_ir
        self.__gauche = gauche
        self.__droit = droit
        self.__direction = direction

    def gauche(self):
        self.__gauche.arret()
        self.__droit.avant()

    def droite(self):
        self.__gauche.avant()
        self.__droit.arret()

    def avant(self):
        self.__droit.avant()
        self.__gauche.avant()

    def arret(self):
        self.__droit.arret()
        self.__gauche.arret()

    def tourner_ligne(self, avant, arriere):
        capteur = self.__capteur_ir.droite if (avant is self.__gauche) else self.__capteur_ir.gauche
        avant.avant()
        arriere.arriere()
        while (capteur()): pass
        while (not capteur()): pass
        while (capteur()): pass

    def tourner(self, direction):
        if (direction == self.__direction):
            return
        elif (Direction.inverser(direction) == self.__direction):
            self.tourner_ligner(self.__gauche, self.__droit)
            self.tourner_ligner(self.__gauche, self.__droit)
        else:
            avant, arriere = self.__droit, self.__gauche
            if (Direction.estSensHoraire(direction, self.__direction)):
                avant, arriere = arriere, avant

            self.tourner_ligne(avant, arriere)

        self.__direction = direction

    def suivre_ligne(self):
        g, d = True, True
        while (g or d):
            if not g:
                self.gauche()
            elif not d:
                self.droite()
            else:
                self.avant()

            g, d = self.__capteur_ir.lire()
