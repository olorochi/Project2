from direction import Direction
import time


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
        time.sleep(0.2)
        while (capteur()):
            time.sleep(0.01)


    def tourner(self, direction):
        print(f"Tourner: {direction}")
        if (direction == self.__direction):
            return
        elif (Direction.inverser(direction) == self.__direction):
            self.tourner_ligne(self.__gauche, self.__droit)
            self.tourner_ligne(self.__gauche, self.__droit)
        else:
            avant, arriere = self.__droit, self.__gauche
            if (Direction.estSensHoraire(self.__direction, direction)):
                avant, arriere = arriere, avant

            self.tourner_ligne(avant, arriere)

        self.__direction = direction

    def suivre_ligne(self):
        print("suivre_ligne")
        g, d = True, True
        while (g or d):
            if not g:
                self.gauche()
            elif not d:
                self.droite()
            else:
                self.avant()

            g, d = self.__capteur_ir.lire()
            time.sleep(0.01)

        self.avant()
        time.sleep(0.1)
