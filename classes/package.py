import pygame
import random

# Classe qui va gérer nos enemies


class Package(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.allEnemies = game.allEnemies
        self.health = 1
        self.maxHealth = 1
        self.special = 0
        self.image = pygame.image.load('./assets/ovni.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 900)
        self.speed = 1

    # Fonction qui supprime la balle si elle sort du cadre de l'écran
    def remove(self):
        self.game.allPackage.remove(self)

    def down(self):
        if self.game.checkCollision(self, self.game.allShooters) or self.rect.y >= 700:
            self.game.shooter.health = 0
            self.game.shooter.die()
        else:
            self.rect.y += self.speed

# Fonction qui supprime la balle si elle sort du cadre de l'écran
    def remove(self):
        self.shooter.allBullet.remove(self)

    # Fonction qui permet à la balle d'avancer
    def move(self):
        self.rect.y -= self.velocity
        self.rotate()

        # Vérifier si la balle entre en collision avec un monstre
        for enemy in self.shooter.game.checkCollision(self, self.shooter.game.allEnemies):
            self.remove()
            # infliger les dégats
            enemy.damage(self.shooter.attack)

        # Vérifier si le projectile n'est plus présent sur l'écran
        if self.rect.y < 5:
            self.remove()

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
