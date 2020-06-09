import pygame
from classes.bullet import Bullet
# Cette classe représente notre joueur
class Shooter(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.shootingSpeed = 100
        self.allBullet = pygame.sprite.Group()
        self.movementSpeed = 3
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 420

    def move_right(self):
        self.rect.x += self.movementSpeed

    def move_left(self):
        self.rect.x -= self.movementSpeed  

    def shoot(self):
        # Création d'une instance de la classe bullet
        self.allBullet.add(Bullet(self))    