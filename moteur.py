class Moteur:
    def __init__(self, en, avant, arriere, vitesse=1, freq=100):
        self.__en = en
        self.__avant = avant
        self.__arriere = arriere
        self.freq = freq
        self.__en.blink(vitesse)

    def set_vitesse(self, vitesse):
        tot = 1 / self.freq  # 0.01
        on = tot * vitesse
        self.__en.blink(on, tot - on)

    def avant(self):
        self.__avant.on()
        self.__arriere.off()

    def arriere(self):
        self.__avant.off()
        self.__arriere.on()

    def frein(self):
        self.__avant.on()
        self.__arriere.on()

    def arret(self):
        self.__avant.off()
        self.__arriere.off()
