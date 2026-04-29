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

    @staticmethod
    def tourner_ligne(avant, arriere, capteur):
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
                capteur = self.__capteur_ir.gauche
            else:
                capteur = self.__capteur_ir.droite

            self.tourner_ligne(avant, arriere, capteur)

        self.__direction = direction

    def suivre_ligne(self):
        print("suivre_ligne")
        g, d = True, True
        while (g or d):
            if g:
                self.droite()
            elif d:
                self.gauche()
            else:
                self.avant()

            g, d = self.__capteur_ir.lire()
            time.sleep(0.01)

        self.avant()
        time.sleep(0.1)
