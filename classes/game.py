import pygame
import random
from classes.shooter import Shooter
from classes.enemy import Enemy
from classes.package import Package
from classes.boss import Boss


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

        # Définition d'un groupe de package
        self.allPackages = pygame.sprite.Group()

        # Définition d'un groupe de boss
        self.allBosses = pygame.sprite.Group()

        self.pressed = {}

        # Spawn du premier enemy
        self.spawnEnemy()

    # Fonction qui gère le spawn des énemies
    def spawnEnemy(self):
        enemy = Enemy(self)
        package = Package(self)

        # Boost d'un monstre lorsque le joueur atteint des paliers de 50 points
        if self.score >= 50 and self.score < 100:
            enemy.speed += 0.5

        if self.score >= 100 and self.score < 150: 
            enemy.speed += 1

        if self.score >= 150:
            enemy.speed += 1.5

        choiceEnemy = random.randint(1,10)
        if choiceEnemy >= 0 and choiceEnemy <= 8:
            self.allEnemies.add(enemy)
        elif choiceEnemy > 8 and choiceEnemy <= 10:
            self.allPackages.add(package)

    # Fonction qui gère le spawn des boss
    def spawnBoss(self):
        boss = Boss(self)
        self.allBosses.add(boss)

    def checkCollision(self, sprite, group):
        # Nous définissons les collisions, pour tuer le joueur à la collision remplacer False par True
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
