#!/bin/python3


import devices
from moteur import Moteur
from capteurIR import CapteurIR
from suiveurLigne import SuiveurLigne
from time import sleep

gauche = Moteur(devices.ENA, devices.IN1, devices.IN2, 0.2)
droit = Moteur(devices.ENB, devices.IN3, devices.IN4, 0.2)
#gauche.avant()
capteur = CapteurIR()
suiveur = SuiveurLigne(capteur)


while True:
    etat = suiveur.etat()
    print(etat)

    if etat == "INTERSECTION":
        gauche.arret()
        droit.arret()

    elif etat == "GAUCHE":
        gauche.arret()
        droit.avant()

    elif etat == "DROITE":
        gauche.avant()
        droit.arret()

    else:  # PERDU
        gauche.avant()
        droit.avant()

    sleep(0.05)
