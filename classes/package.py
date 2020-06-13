import pygame
import random

# Classe qui va gérer nos packages
class Package(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.allPackages = game.allPackages
        self.health = 1
        self.maxHealth = 1
        self.allEnemies = game.allEnemies
        self.special = random.randint(0,10)
        self.image = pygame.image.load('./assets/airdrop.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 900)
        self.rect.y = -100
        self.speed = 1

    def remove(self):
        self.game.allPackages.remove(self) 

    def down(self):
        if  self.rect.y >= 700 :
            self.remove()
        else : 
            self.rect.y += self.speed

    def damage(self, amount):
        # Infliger les dégâts
        self.health -= amount
        # Vérifier si l'enemie est mort 
        if self.health <= 0:
            if self.special == 0 or self.special == 1:
                self.game.shooter.movementSpeed += 1
                print("SPEED +1")
            elif self.special == 3 or self.special == 4: 
                self.game.shooter.attack += 1
                print("ATTACK +1")
            elif self.special == 6 :
                if self.game.shooter.movementSpeed > 2 :
                    self.game.shooter.movementSpeed -= 1
                    print("SPEED -1")
            elif self.special == 9 :
                if self.game.shooter.attack > 0.5:
                    self.game.shooter.attack -= 0.1
                    print("ATTACK -0.1")
            # elif self.special >= 0  :
            #     self.game.shooter.bullet.velocity += 1 
            #     print("BULLET VELOCITY  = " + str(self.game.shooter.bullet.velocity))
            self.special = random.randint(0,9)

            # Suppression de l'entité
            # self.rect.x = random.randint(50, 950)
            
            self.remove()
            self.rect.y = -100
            # self.game.score += 1
            print("SCORE : " + str(self.game.score))
            if len(self.allEnemies) < 8:
                self.game.spawnEnemy()  
            

            self.health = self.maxHealth        