from asyncio import sleep


class Robot:
    def __init__(self, gauche, droit, capteur_ir):
        self.__capteur_ir = capteur_ir
        self.__gauche = gauche
        self.__droit = droit

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

    def tourner_gauche(self, duree=0.35):
        self.__gauche.arriere()
        self.__droit.avant()
        sleep(duree)
        self.arret()
    
    def tourner_droite(self, duree=0.35):
        self.__gauche.avant()
        self.__droit.arriere()
        sleep(duree)
        self.arret()

    def tourner(self.mouvement):
        if mouvement == "GAUCHE":
            self.tourner_gauche()
        elif mouvement == "DROITE":
            self.tourner_droite()
        elif mouvement == "INTERSECTION":
            self.avant()
            sleep(0.2)
            self.arret()

    def suivre_ligne(self):
        g = True
        d = True
        while (g or d):
            if not g:
                self.gauche()
            elif not d:
                self.droite()
            else:
                self.avant()

            g = self.__capteur_ir.detection_gauche()
            d = self.__capteur_ir.detection_droite()
