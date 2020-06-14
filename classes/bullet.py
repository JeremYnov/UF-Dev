import pygame


# Définition de la classe qui gère les balles tirées par le joueur
class Bullet(pygame.sprite.Sprite):
    def __init__(self, shooter):
        super().__init__()
        self.shooter = shooter
        self.velocity = 20
        self.image = pygame.image.load('./assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = shooter.rect.x + 85
        self.rect.y = shooter.rect.y
        self.originImage = self.image
        self.angle = 0
        
    # Fonction qui permet de donner une rotation à la balle
    def rotate(self):    
        self.angle += 10
        # La fonction rotozoom prend notre image d'origine et lui applique l'angle que nous incrémentons au dessus 
        self.image = pygame.transform.rotozoom(self.originImage,self.angle,1)
        self.rect = self.image.get_rect(center = self.rect.center)

    # Fonction qui supprime la balle si elle sort du cadre de l'écran  
    def remove(self):
        self.shooter.allBullet.remove(self) 

    # Fonction qui permet à la balle d'avancer
    def move(self):
        self.rect.y -= self.velocity
        self.rotate()

        # Vérifier si la balle entre en collision avec un monstre
        for enemy in self.shooter.game.checkCollision(self, self.shooter.game.allEnemies)  :
            self.remove()
            # Infliger les dégats 
            enemy.damage(self.shooter.attack)

        # Vérifier si la balle entre en collision avec un package
        for package in self.shooter.game.checkCollision(self, self.shooter.game.allPackages)  :
            self.remove()
            # Infliger les dégats 
            package.damage(self.shooter.attack)    

        for boss in self.shooter.game.checkCollision(self,self.shooter.game.allBosses) :
            self.remove()
            # Infliger les dégâts 
            boss.damage(self.shooter.attack)

        # Vérifier si le projectile n'est plus présent sur l'écran 
        if self.rect.y < 5:
            self.remove()
            

    