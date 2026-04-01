#!/bin/python3


import devices
from moteur import Moteur
from capteurIR import CapteurIR
from robot import Robot
from djisktra import graphe

gauche = Moteur(devices.ENA, devices.IN1, devices.IN2, 1)
droit = Moteur(devices.ENB, devices.IN3, devices.IN4, 1)
capteur = CapteurIR()
robot = Robot(gauche, droit, capteur)
robot.suivre_ligne()

# chemin = graphe.trouver_chemin(2, 9)
# for direction in chemin:

