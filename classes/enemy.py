import pygame 

# Classe qui va gérer nos enemies 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 2
        self.special = 0
        self.image = pygame.image.load('./assets/alien/alien1.png')
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.speed = 1

    def down(self):
        self.rect.y += self.speed