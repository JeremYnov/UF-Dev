import pygame
# import time
from classes.shooter import Shooter
from classes.enemy import Enemy

class Game:
    def __init__(self):
        self.score = 0
        # Générer un group pour les collisions 
        self.allShooters = pygame.sprite.Group()
        # Générer notre joueur
        self.shooter = Shooter(self)
        # Ajout du joueur dans le group 
        self.allShooters.add(self.shooter)

        # Définition d'un groupe de monstre 
        self.allEnemies = pygame.sprite.Group()

        self.pressed = {}
        self.spawnEnemy()

    # Fonction qui gère le spawn des énemies  
    def spawnEnemy(self):
        enemy = Enemy(self)
        # time.sleep(2)
        self.allEnemies.add(enemy)
        print(len(self.allEnemies))
        

    def checkCollision(self,sprite,group):
        # Nous définissons les collisions, pour tuer le joueur à la collision remplacer False par True
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
