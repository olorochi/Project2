from time import sleep


class Robot:
    def __init__(self, gauche, droit, capteur_ir):
        self.__capteur_ir = capteur_ir
        self.__gauche = gauche
        self.__droit = droit

    def gauche(self):
        print("gauche")
        self.__gauche.arret()
        self.__droit.avant()

    def droite(self):
        print("droite")
        self.__gauche.avant()
        self.__droit.arret()

    def avant(self):
        print("avant")
        self.__droit.avant()
        self.__gauche.avant()

    def suivre_ligne(self):
        g = False
        d = False
        while (not (g and d)):
            if g:
                self.gauche()
            elif d:
                self.droite()
            else:
                self.avant()

            g = not self.__capteur_ir.detection_gauche()
            d = not self.__capteur_ir.detection_droite()
