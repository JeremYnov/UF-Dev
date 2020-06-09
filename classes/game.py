import pygame
from classes.shooter import Shooter

class Game:
    def __init__(self):
        # generer notre hero
        self.shooter = Shooter()
        self.pressed = {
            "right" : False,
            "left" : False,
        }