class SuiveurLigne:
    def __init__(self, capteur_ir):
        self.__capteur_ir = capteur_ir

    def etat(self):
        g = self.__capteur_ir.detection_gauche()
        d = self.__capteur_ir.detection_droite()

        if g and d:
            return "INTERSECTION"

        if g and not d:
            return "GAUCHE"

        if d and not g:
            return "DROITE"

        return "PERDU"