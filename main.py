#!/bin/python3


import devices
from moteur import Moteur
from capteurIR import CapteurIR
from robot import Robot
from djisktra import graphe
from direction import Direction

gauche = Moteur(devices.ENA, devices.IN1, devices.IN2, 0.7)
droit = Moteur(devices.ENB, devices.IN3, devices.IN4, 0.7)
capteur = CapteurIR()
robot = Robot(gauche, droit, capteur, Direction.GAUCHE)

chemin = graphe.trouver_chemin(4, 7)
for direction in chemin:
    robot.tourner(direction)
    robot.suivre_ligne()
