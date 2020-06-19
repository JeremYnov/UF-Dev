import pygame 
import random


# Classe qui va gérer nos enemies 
class Boss(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.allBosses = game.allBosses
        self.health = 30
        self.maxHealth = 30
        self.image = pygame.image.load('./assets/boss.png')
        self.image = pygame.transform.scale(self.image,(300,300))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 900)
        self.rect.y = -300
        self.speed = 1.5

    # Fonction de descente du boss 
    def down(self):
        if self.game.checkCollision(self,self.game.allShooters) or self.rect.y >= 700 :
            self.game.shooter.health = 0 
            self.game.shooter.die()
        else : 
            self.rect.y += self.speed

    # Fonction qui permet de détruire le boss si il meurt
    def remove(self):
        self.game.allBosses.remove(self) 

    def damage(self, amount):
        # Infliger les dégâts
        self.health -= amount

        # Vérifier si l'enemie est mort 
        if self.health <= 0:
            self.game.score += 10
            
            # print("SCORE : " + str(self.game.score))

            # Destruction du boss
            self.remove()

            # Suppression de l'entité
            self.rect.x = random.randint(50, 800)
            self.rect.y = -300
            self.health = self.maxHealth