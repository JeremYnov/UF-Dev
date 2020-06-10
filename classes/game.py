import pygame
from classes.shooter import Shooter
from classes.enemy import Enemy

class Game:
    def __init__(self):
        # generer notre hero
        self.shooter = Shooter()

        # Définition d'un groupe de monstre 
        self.allEnemies = pygame.sprite.Group()

        self.pressed = {}
        self.spawnEnemy()

    # Fonction qui gère le spawn des énemies  
    def spawnEnemy(self):
        # monster = Monster()
        self.allEnemies.add(Enemy())