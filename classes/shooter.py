import pygame
from classes.bullet import Bullet

pygame.mixer.init()
pygame.mixer.music.load("assets/sounds/tir.ogg")
pygame.mixer.music.set_volume(5)

# Cette classe représente notre joueur


class Shooter(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 1
        self.max_health = 1
        self.attack = 1
        self.allBullet = pygame.sprite.Group()
        self.movementSpeed = 3
        self.image = pygame.image.load('./assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 370
        self.rect.y = 600

    # Fonction permettant le mouvement du personnage vers la droite
    def move_right(self):
        # Le personnage peut se déplacer seulement si il n'y a pas de collision avec un enemie
        if not self.game.checkCollision(self, self.game.allEnemies):
            self.rect.x += self.movementSpeed

    # Fonction permettant le mouvement du personnage vers la gauche
    def move_left(self):
        # Le personnage peut se déplacer seulement si il n'y a pas de collision avec un enemie
        if not self.game.checkCollision(self, self.game.allEnemies):
            self.rect.x -= self.movementSpeed

    # Fonction permettant au perssonage de tirer des balles 
    def shoot(self):
        # Initialisation des sons
        shotSound = pygame.mixer.Sound("assets/sounds/tir.ogg")
        shotSound.set_volume(0.1)

        # Création d'une instance de la classe bullet
        bullet = Bullet(self)
        shotSound.play()
        # Ajout de la balle tiré dans le groupe allBullet
        self.allBullet.add(Bullet(self))

    def die(self):
        if self.health <= 0:
            print("GAME OVER")
