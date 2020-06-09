import pygame 

pygame.init()

# Creation d'une classe game
class Game:

    def __init__(self):
        # generer notre hero
        self.player = Player()

# creation du hero
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

# Génération de notre fenêtre de jeu 
pygame.display.set_caption("UF DEV")
screen = pygame.display.set_mode((720,920))


# Import du background de l'appli 
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()


running = True 

# Boucle qui nous permet de garder le jeu allumé 
while running:
    # Appliquer le background de l'appli 
    screen.blit(background,(0,0))

    #Aplliquer l'image du hero
    screen.blit(game.player.image, game.player.rect)

    # Mettre à jour la fenêtre
    pygame.display.flip()

    # On parcours la liste d'evenement 
    for event in pygame.event.get():
        # Si le joueur lance l'evenement quitter alors on coupe notre boucle
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()