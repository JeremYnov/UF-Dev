import pygame 

pygame.init()

# Génération de notre fenêtre de jeu 
pygame.display.set_caption("UF DEV")
screen = pygame.display.set_mode((720,920))


# Import du background de l'appli 
background = pygame.image.load('assets/bg.jpg')

running = True 

# Boucle qui nous permet de garder le jeu allumé 
while running:
    # Appliquer le background de l'appli 
    screen.blit(background,(0,0))

    # Mettre à jour la fenêtre
    pygame.display.flip()

    # On parcours la liste d'evenement 
    for event in pygame.event.get():
        # Si le joueur lance l'evenement quitter alors on coupe notre boucle
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()