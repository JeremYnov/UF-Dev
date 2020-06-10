import pygame 
import random


# Classe qui va gérer nos enemies 
class Enemy(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.allEnemies = game.allEnemies
        self.health = 2
        self.maxHealth = 2
        self.special = 0
        self.image = pygame.image.load('./assets/secoupe.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 900)
        self.speed = 1

    def down(self):
        if self.game.checkCollision(self,self.game.allShooters) or self.rect.y >= 700 :
            self.game.shooter.health = 0 
            self.game.shooter.die()
        else : 
            self.rect.y += self.speed

    def damage(self, amount):
        # Infliger les dégâts
        self.health -= amount
        # Vérifier si l'enemie est mort 
        if self.health <= 0:
             

            # Suppression de l'entité
            self.rect.x = random.randint(50, 950)
            # print(self.rect.x)
            self.rect.y = -100
            self.game.score += 1
            print("SCORE : " + str(self.game.score))
            if len(self.allEnemies) < 8:
                self.game.spawnEnemy()  

            self.health = self.maxHealth