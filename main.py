#!/bin/python3

import devices
from moteur import Moteur
from capteurIR import CapteurIR
from robot import Robot
from djisktra import graphe
from direction import Direction


noeud_max = len(graphe.distances)


def lire_direction():
    dictionnaire = {
        "haut": Direction.HAUT,
        "bas": Direction.BAS,
        "gauche": Direction.GAUCHE,
        "droite": Direction.DROITE,
    }

    while True:
        val = input("Direction initiale (haut/bas/gauche/droite): ").strip().lower()
        if val in dictionnaire:
            return dictionnaire[val]
        print("Entrée invalide.")


def lire_noeud(prompt):
    while True:
        val = input(prompt)
        if (val.isdigit()):
            num = int(val)
            if (num > 0 and num <= noeud_max):
                return num
        print("Entrée invalide.")


depart = lire_noeud(f"Noeud de départ (1-{noeud_max}): ")
arrivee = lire_noeud(f"Noeud d'arrivée (1-{noeud_max}): ")
direction_initiale = lire_direction()

gauche = Moteur(devices.ENA, devices.IN1, devices.IN2, 0.4)
droit = Moteur(devices.ENB, devices.IN3, devices.IN4, 0.4)
capteur = CapteurIR(devices.IR_G, devices.IR_D)
robot = Robot(gauche, droit, capteur, direction_initiale)

chemin = graphe.trouver_chemin(depart, arrivee)

for direction in chemin:
    robot.tourner(direction)
    robot.suivre_ligne()
