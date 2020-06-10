import pygame 
from classes.game import Game

pygame.init()


# Génération de notre fenêtre de jeu 
pygame.display.set_caption("UF DEV")
# Taille de l'écran Léo (tu mettras en commentaire egalement gros bg)
screen = pygame.display.set_mode((980,850))


# Import du background de l'appli 
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()


running = True 

# Boucle qui nous permet de garder le jeu allumé 
while running:
    # Appliquer le background de l'appli 
    screen.blit(background,(-1100,-100))

    # Appliquer l'image du joueur
    screen.blit(game.shooter.image, game.shooter.rect)

    # Réccupération des balles tirées par le joueur
    for bullet in game.shooter.allBullet:
        bullet.move()

    # Réccupérations des enemies
    for enemy in game.allEnemies:
        enemy.down()

    # Appliquer l'image des balles
    game.shooter.allBullet.draw(screen)

    # Appliquer l'image des énemies
    game.allEnemies.draw(screen)

    if game.pressed.get(pygame.K_LEFT):
        if(game.shooter.rect.x < -100):
            game.shooter.rect.x = 1000
            game.shooter.move_left()
        else:
            game.shooter.move_left()
    elif game.pressed.get(pygame.K_RIGHT):
        if(game.shooter.rect.x > 1000):
            game.shooter.rect.x = -100
            game.shooter.move_right()
        else:
            game.shooter.move_right()

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