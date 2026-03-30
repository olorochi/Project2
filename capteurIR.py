import devices
from gpiozero import DigitalInputDevice


class CapteurIR:
    def __init__(self):
        self.__gauche = DigitalInputDevice(devices.IR_G)
        self.__droit = DigitalInputDevice(devices.IR_D)

    def gauche(self):
        return self.__gauche.value

    def droit(self):
        return self.__droit.value

    def detection_gauche(self):
        return self.__gauche.value == 0

    def detection_droite(self):
        return self.__droit.value == 0

    def lire(self):
        return (self.__gauche.value, self.__droit.value)