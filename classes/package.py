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
        self.special = random.randint(0,9)
        self.image = pygame.image.load('./assets/airdrop.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 900)
        self.rect.y = -100
        self.speed = 1
   
    # Fonction permettant de supprimer un package 
    def remove(self):
        self.game.allPackages.remove(self) 
    
    # Fonction permettant au package de descendre et de le supprimer si il sort de l'écran
    def down(self):
        if  self.rect.y >= 700 :
            self.remove()
        else : 
            self.rect.y += self.speed

    # Fonction permettant d'infliger les dégats du personnage au packages 
    def damage(self, amount):
        # Infliger les dégâts
        self.health -= amount
        # Vérifier si l'enemie est mort 
        if self.health <= 0:
            # Choix du bonus ou malus en fonction de la variable random special
            # 30% de chance +1 SPEED
            # 30% de chance +1 ATTACK
            # 20% de chance -1 SPEED
            # 20% de chance -0.1 ATTACK 
            if self.special >= 0 and self.special <= 2:
                self.game.shooter.movementSpeed += 1
                print("SPEED +1")
            elif self.special > 2 and self.special <= 5: 
                if self.game.shooter.attack < 3:
                    self.game.shooter.attack += 1
                print("ATTACK +1")
            elif self.special > 5 and self.special <= 7:
                # if self.game.shooter.movementSpeed > 2 :
                self.game.shooter.movementSpeed -= 1
                print("SPEED -1")
            elif self.special > 7 and self.special <= 9 :
                # if self.game.shooter.attack > 0.6:
                self.game.shooter.attack -= 0.1
                print("ATTACK -0.1")

            self.special = random.randint(0,9)
            print(self.special)

            # Suppression de l'entité
            # self.rect.x = random.randint(50, 950)
            
            self.remove()
            self.rect.y = -100
            # self.game.score += 1
            print("SCORE : " + str(self.game.score))
            if len(self.allEnemies) < 8:
                self.game.spawnEnemy()  
            

            self.health = self.maxHealth        