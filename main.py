import pygame
import math
from settings import settings



from classes.game import Game

mainClock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/music/game_music.mp3")
pygame.mixer.music.set_volume(0.1)

screenWidth = pygame.display.get_surface().get_width()
screenHeight= pygame.display.get_surface().get_height()
middleScreenWidth = screenWidth / 2
middleScreenHeight = screenHeight / 2



# Variable contenant la font que nous utiliserons ainsi que sa taille  
titleFont = pygame.font.SysFont('lunchtimedoublysoregular', 30)
font = pygame.font.SysFont('lunchtimedoublysoregular', 20)
fontgo = pygame.font.SysFont('lunchtimedoublysoregular', 80)

# Fonction permettant d'ajouter du texte sur la fenêtre de jeu 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# running = True 

# Génération de notre fenêtre de jeu 
pygame.display.set_caption("UFO Abduction")
pygame.display.set_icon(settings.icon)



def main_menu():
    while True:
        click = pygame.mouse.get_pressed()
        
        settings.screen.blit(settings.menuBackground,(0,0))
        # settings.screen.fill((0,0,0))
        draw_text('Menu Principal', titleFont, (255, 255, 255), settings.screen, 390, 20)
 
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(360, 170, 295, 50)
        
        button_2 = pygame.Rect(360, 270, 295, 50)

        button_3 = pygame.Rect(360, 370, 295, 50)
        
        if button_1.collidepoint((mx, my)):
            if click[0] == 1:
                game()
        if button_2.collidepoint((mx, my)):
            if click[0] == 1:
                instructions()
        if button_3.collidepoint((mx, my)):
            if click[0] == 1:
                instructions()
        pygame.draw.rect(settings.screen, (255, 0, 0), button_1)
        pygame.draw.rect(settings.screen, (255, 0, 0), button_2)
        pygame.draw.rect(settings.screen, (255, 0, 0), button_3)
        draw_text('Lancer la partie', titleFont, (255, 255, 255),settings.screen, 370, 180)
        draw_text('Options', titleFont, (255, 255, 255),settings.screen, 370, 280)
        draw_text('Instructions', titleFont, (255, 255, 255),settings.screen, 370, 380)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    # sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.flip()
        mainClock.tick(60)


def game():
    pygame.mixer.music.play()
    running = True

    # Charger le jeu
    game = Game()
    

    # Boucle qui nous permet de garder le jeu allumé 
    while running:

        # Appliquer le background de l'appli 
        settings.screen.blit(settings.gameBackground,(-1100,-100))

        # Appliquer le score du joueur en haut à gauche 
        draw_text('SCORE : '+ str(game.score), titleFont, (255, 255, 255), settings.screen, 20, 20)

        # Afficher les caractéristiques du joueur
        draw_text('Speed : '+ str(game.shooter.movementSpeed), font, (255, 255, 255), settings.screen, 820, 20)
        draw_text('Attack : '+ str(game.shooter.attack), font, (255, 255, 255), settings.screen, 820, 50)
        draw_text('Bullet Velocity : '+ str(game.shooter.bullet.velocity), font, (255, 255, 255), settings.screen, 720, 80)

        # Appliquer l'image du joueur
        settings.screen.blit(game.shooter.image, game.shooter.rect)

        # Réccupération des balles tirées par le joueur
        for bullet in game.shooter.allBullet:
            # print("ENTREE DANS LA BOUCLE FOR BULLET")
            bullet.move()

        # Réccupérations des enemies
        for enemy in game.allEnemies:
            # print("ENTREE DANS LA BOUCLE ENEMIES")
            enemy.down()

        for package in game.allPackages:
            # print("ENTREE DANS LA BOUCLE PACKAGES")
            package.down()

        # Appliquer l'image des balles
        game.shooter.allBullet.draw(settings.screen)

        # Appliquer l'image des énemies
        game.allEnemies.draw(settings.screen)

        # Appliquer l'image des énemies
        game.allPackages.draw(settings.screen)

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

        if game.shooter.health <= 0 :
            game_over()

        # On parcours la liste d'evenement 
        for event in pygame.event.get():
            # Si le joueur lance l'evenement quitter alors on coupe notre boucle
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # Détecter les déplacements du joueur 
                game.pressed[event.key] = True
                # print("TEST KEYDOWN")
                if event.key == pygame.K_SPACE:
                    game.shooter.shoot()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            
       
        # Mettre à jour la fenêtre
        pygame.display.flip()
        mainClock.tick(60)


def instructions():
    running = True
    while running:
        settings.screen.fill((0,0,0))
 
        draw_text('Options', titleFont(), (255, 255, 255), settings.screen, 20, 20)
        draw_text('Bonjour jeune aventurier des temps modernes et bienvenu sur notre jeu.', font, (255, 255, 255), settings.screen, 20, 70)
        draw_text("Tout d'abord voici la liste des commandes que tu dois connaitre :", font, (255, 255, 255), settings.screen, 20, 95)
        draw_text("Se deplacer vers la droite : Fleche de droite ", font, (255, 255, 255), settings.screen, 20, 140)
        draw_text("Se deplacer vers la gauche : Fleche de gauche ", font, (255, 255, 255), settings.screen, 20, 165)
        draw_text("Tirer une balle : Espace ", font, (255, 255, 255), settings.screen, 20, 190)
        draw_text("Retourner au menu precedent : Echap ", font, (255, 255, 255), settings.screen, 20, 215)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
       
        pygame.display.flip()
        mainClock.tick(60)

def game_over():
    running = True
    while running:
        click = pygame.mouse.get_pressed()

        settings.screen.blit(settings.gameOverBackground,(0,0))
        # settings.screen.fill((0,0,0))

        draw_text('GAME OVER', fontgo, (255, 0, 0), settings.screen, 300, 200)
        draw_text("Tu t'es battu de toutes tes forces,", font, (255, 255, 255), settings.screen, 310, 300)
        draw_text("mais cela n'a pas suffit.", font, (255, 255, 255), settings.screen, 310, 350)
        draw_text("Tu peux toujours retenter ta chance", font, (255, 255, 255), settings.screen, 310, 400)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(360, 570, 295, 50)
        
        if button_1.collidepoint((mx, my)):
            if click[0] == 1:
                game()
        pygame.draw.rect(settings.screen, (255, 0, 0), button_1)
        draw_text('Reessayer', titleFont, (255, 255, 255),settings.screen, 435, 580)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 

        pygame.display.flip()
        mainClock.tick(60)


main_menu()