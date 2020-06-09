import pygame

# Définition de la classe qui gère les balles tirées par le joueur
class Bullet(pygame.sprite.Sprite):
    def __init__(self, shooter):
        super().__init__()
        self.velocity = 4
        self.shooter = shooter
        self.image = pygame.image.load('./assets/projectile.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = shooter.rect.x + 85
        self.rect.y = shooter.rect.y
        
    def remove(self):
        self.shooter.allBullet.remove(self) 

    def move(self):
        self.rect.y -= self.velocity

        # Vérifier si le projectile n'est plus présent sur l'écran 
        if self.rect.y < 5:
            self.remove()
            

    