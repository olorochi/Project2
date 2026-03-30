#!/bin/python3


import devices
from moteur import Moteur


gauche = Moteur(devices.ENA, devices.IN1, devices.IN2, 0.2)
droit = Moteur(devices.ENB, devices.IN3, devices.IN4, 0.2)
gauche.avant()

while True:
    pass
