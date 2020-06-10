import pygame
from classes.shooter import Shooter
from shooter import Shooter

class Game:
    def __init__(self):
        # definir si notre jeu a commencé
        self.is_playing = False
        # generer notre hero
        self.shooter = Shooter()
        self.pressed = {
            "right" : False,
            "left" : False,
        }

    def update(self, screen):

        # Appliquer l'image du joueur
        screen.blit(self.shooter.image, self.shooter.rect)

        for bullet in self.shooter.allBullet:
            bullet.move()

        # Appliquer l'image des balles
        self.shooter.allBullet.draw(screen)

        if self.pressed.get(pygame.K_LEFT):
            if(self.shooter.rect.x < -100):
                self.shooter.rect.x = 1000
                self.shooter.move_left()
            else:
                self.shooter.move_left()
        elif self.pressed.get(pygame.K_RIGHT):
            if(self.shooter.rect.x > 1000):
                self.shooter.rect.x = -100
                self.shooter.move_right()
            else:
                self.shooter.move_right()