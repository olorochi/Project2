import devices


class CapteurIR:
    def __init__(self, gauche, droit):
        self.__gauche = gauche
        self.__droit = droit

    def gauche(self):
        return self.__gauche.value == 0

    def droite(self):
        return self.__droit.value == 0

    def lire(self):
        return (self.gauche(), self.droite())
