import pygame
from classes.bullet import Bullet

# Cette classe représente notre joueur
class Shooter(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 1
        self.attack = 1
        self.allBullet = pygame.sprite.Group()
        self.movementSpeed = 3
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 600
        self.bullet = Bullet(self)

    def move_right(self):
        if not self.game.checkCollision(self, self.game.allEnemies):
            self.rect.x += self.movementSpeed

    def move_left(self):
        if not self.game.checkCollision(self, self.game.allEnemies):
            self.rect.x -= self.movementSpeed  

    def shoot(self):
        # Création d'une instance de la classe bullet
        self.allBullet.add(Bullet(self))   

    def die(self):
        if self.health <= 0 : 
            print("GAME OVER MOTHER FUCKER")