import pygame
import math

from classes.game import Game

pygame.init()


# Génération de notre fenêtre de jeu 
pygame.display.set_caption("UF DEV")
# Taille de l'écran Léo (tu mettras en commentaire egalement gros bg)
screen = pygame.display.set_mode((980,620))


# Import du background de l'appli 
background = pygame.image.load('assets/bg.jpg')

# Import de la bannière (qu'on changera par la suite)
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer le bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# Charger le jeu
game = Game()


running = True 

# Boucle qui nous permet de garder le jeu allumé 
while running:


    # Appliquer le background de l'appli 
    screen.blit(background,(0, -280))

    # verifier si le jeu a commencé ou non 
    if game.is_playing:
        #declancher les instruction de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commencé
    else: 
        # ajouter l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        
    # Mettre à jour la fenêtre
    pygame.display.flip()

    # On parcours la liste d'evenement 
    for event in pygame.event.get():
        # Si le joueur lance l'evenement quitter alors on coupe notre boucle
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Détecter les déplacements du joueur 
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                game.shooter.shoot()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Pour savoir si la souris peut cliquer sur le bouton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en true
                game.is_playing = True