import pygame
import math
import json
import time
from settings import settings


from classes.game import Game

mainClock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("assets/music/game_music.mp3")
pygame.mixer.music.set_volume(0.03)

screenWidth = pygame.display.get_surface().get_width()
screenHeight = pygame.display.get_surface().get_height()
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

# Génération de notre fenêtre de jeu
pygame.display.set_caption("UFO Abduction")
pygame.display.set_icon(settings.icon)


def main_menu():
    settings.shopping = False
    while True:
        click = pygame.mouse.get_pressed()

        settings.screen.blit(settings.menuBackground, (0, 0))
        draw_text('Menu Principal', titleFont,
                  (255, 255, 255), settings.screen, 390, 20)

        mx, my = pygame.mouse.get_pos()

        shadow_button1 = pygame.Rect(340, 160, 340, 50)
        shadow_button2 = pygame.Rect(340, 260, 340, 50)
        shadow_button3 = pygame.Rect(340, 360, 340, 50)
        shadow_button4 = pygame.Rect(340, 460, 340, 50)
        shadow_button5 = pygame.Rect(340, 560, 340, 50)

        button_1 = pygame.Rect(330, 170, 340, 50)

        button_2 = pygame.Rect(330, 270, 340, 50)

        button_3 = pygame.Rect(330, 370, 340, 50)

        button_4 = pygame.Rect(330, 470, 340, 50)

        button_5 = pygame.Rect(330, 570, 340, 50)

        if button_1.collidepoint((mx, my)):
            if click[0] == 1:
                game()
        if button_2.collidepoint((mx, my)):
            if click[0] == 1:
                settings.loadingGame = True
                game()
        if button_3.collidepoint((mx, my)):
            if click[0] == 1:
                instructions()
        if button_4.collidepoint((mx, my)):
            if click[0] == 1:
                instructions()
        if button_5.collidepoint((mx, my)):
            if click[0] == 1:
                settings.shopping = True
                game()

        pygame.draw.rect(settings.screen, (64, 64, 122), shadow_button1)
        pygame.draw.rect(settings.screen, (64, 64, 122), shadow_button2)
        pygame.draw.rect(settings.screen, (64, 64, 122), shadow_button3)
        pygame.draw.rect(settings.screen, (64, 64, 122), shadow_button4)
        pygame.draw.rect(settings.screen, (64, 64, 122), shadow_button5)

        pygame.draw.rect(settings.screen, (44, 44, 84), button_1)
        pygame.draw.rect(settings.screen, (44, 44, 84), button_2)
        pygame.draw.rect(settings.screen, (44, 44, 84), button_3)
        pygame.draw.rect(settings.screen, (44, 44, 84), button_4)
        pygame.draw.rect(settings.screen, (44, 44, 84), button_5)

        draw_text('Nouvelle partie', titleFont,
                  (255, 255, 255), settings.screen, 370, 180)
        draw_text('Charger la partie', titleFont,
                  (255, 255, 255), settings.screen, 370, 280)
        draw_text('Instructions', titleFont,
                  (255, 255, 255), settings.screen, 370, 380)
        draw_text('Options', titleFont, (255, 255, 255),
                  settings.screen, 370, 480)
        draw_text('Magasin', titleFont, (255, 255, 255),
                  settings.screen, 370, 580)

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


def save(data):
    with open('save.json', 'w') as outfile:
        json.dump(data, outfile)





def game():
    pygame.mixer.music.play(-1)
    running = True
    spawnBoss = 50

    # Charger le jeu
    game = Game()

    game.shooter.health = game.shooter.max_health
    if settings.shopping:
        running == False
        shop(game)

    if settings.loadingGame:
        load(game)
        settings.loadingGame = False

    # Boucle qui nous permet de garder le jeu allumé
    while running:

        # Appliquer le background de l'appli
        settings.gameBackground = pygame.transform.scale(
            settings.gameBackground, (1500, 900))
        settings.screen.blit(settings.gameBackground, (-300, 0))

        # Appliquer le score du joueur en haut à gauche
        draw_text('SCORE : ' + str(game.score), titleFont,
                  (255, 255, 255), settings.screen, 20, 20)

        # Préparation de la sauvegarde et réccupération des données du joueur et de la party
        with open('save.json') as json_file:
            data = json.load(json_file)
        for value in data['partyTokens']:
            tokens = value['tokens']

        tokens = game.score + tokens
        data = {}
        data['playerInformations'] = []
        data['playerInformations'].append({"playerSpeed": game.shooter.movementSpeed,
                                           "playerAttack": game.shooter.attack})
        data['partyTokens']=[]
        data['partyTokens'].append({"tokens":tokens})
        data['partyInformations'] = []
        data['partyInformations'].append({
            "score": game.score,
        })

        # Afficher les caractéristiques du joueur
        draw_text('Speed : ' + str(game.shooter.movementSpeed),
                  font, (255, 255, 255), settings.screen, 820, 20)
        draw_text('Attack : ' + str(game.shooter.attack), font,
                  (255, 255, 255), settings.screen, 820, 50)

        # Appliquer l'image du joueur
        settings.screen.blit(game.shooter.image, game.shooter.rect)

        # Réccupération des balles tirées par le joueur
        for bullet in game.shooter.allBullet:
            bullet.move()

        # Réccupérations des enemies
        for enemy in game.allEnemies:
            enemy.down()

        for package in game.allPackages:
            package.down()

        if game.score == spawnBoss:
            game.spawnBoss()
            spawnBoss += 50
            print("SORE SPAWNBOSS =" + str(game.score))
            print("SPAWNBOSS = " + str(spawnBoss))
            game.score += 1

        for boss in game.allBosses:
            boss.down()

        # Appliquer l'image des balles
        game.shooter.allBullet.draw(settings.screen)

        # Appliquer l'image des énemies
        game.allEnemies.draw(settings.screen)

        # Appliquer l'image des énemies
        game.allPackages.draw(settings.screen)

        # Appliquer l'image des énemies
        game.allBosses.draw(settings.screen)

        if game.pressed.get(pygame.K_LEFT) and game.shooter.rect.x > -30:
            game.shooter.move_left()
        # elif game.pressed.get(pygame.K_RIGHT) and game.shooter.rect.x  < 810:
        #   Pour Léo
        elif game.pressed.get(pygame.K_END) and game.shooter.rect.x  < 810:
            game.shooter.move_right()

        if game.shooter.health <= 0:
            game_over(game.score)

        # On parcours la liste d'evenement
        for event in pygame.event.get():
            # Si le joueur lance l'evenement quitter alors on coupe notre boucle
            if event.type == pygame.QUIT:
                save(data)
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                # Détecter les déplacements du joueur
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.shooter.shoot()
                elif event.key == pygame.K_ESCAPE:
                    save(data)
                    main_menu()
                    running = False
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        # Mettre à jour la fenêtre
        pygame.display.flip()
        mainClock.tick(60)


def shop(game):
    running = True

    with open('save.json') as json_file:
        data = json.load(json_file)
        for value in data['partyTokens']:
            tokens = value['tokens']

    while running:
        click = pygame.mouse.get_pressed()
        mx, my = pygame.mouse.get_pos()
        settings.screen.fill((0, 0, 0))

        tokens_square = pygame.Rect(320, 100, 340, 70)
        pygame.draw.rect(settings.screen, (64, 64, 122), tokens_square)

        square_1 = pygame.Rect(80, 220, 340, 300)
        pygame.draw.rect(settings.screen, (64, 64, 122), square_1)

        square_2 = pygame.Rect(550, 220, 340, 300)
        pygame.draw.rect(settings.screen, (64, 64, 122), square_2)

        title_1 = pygame.Rect(80, 220, 340, 70)
        pygame.draw.rect(settings.screen, (44, 44, 84), title_1)

        title_2 = pygame.Rect(550, 220, 340, 70)
        pygame.draw.rect(settings.screen, (44, 44, 84), title_2)

        

        title_3 = pygame.Rect(80, 450, 340, 70)
        pygame.draw.rect(settings.screen, (44, 44, 84), title_3)

        title_4 = pygame.Rect(550, 450, 340, 70)
        pygame.draw.rect(settings.screen, (44, 44, 84), title_4)

        button_1 = pygame.Rect(80, 450, 70, 70)
        pygame.draw.rect(settings.screen, (44, 0, 84), button_1)

        button_2 = pygame.Rect(350, 450, 70, 70)
        pygame.draw.rect(settings.screen, (44, 0, 84), button_2)

        button_3 = pygame.Rect(550, 450, 70, 70)
        pygame.draw.rect(settings.screen, (44, 0, 84), button_3)

        button_4 = pygame.Rect(820, 450, 70, 70)
        pygame.draw.rect(settings.screen, (44, 0, 84), button_4)

        shadow_button5 = pygame.Rect(610, 700, 340, 50)
        pygame.draw.rect(settings.screen, (64, 64, 122), shadow_button5)
        button_5 = pygame.Rect(600, 710, 340, 50)
        pygame.draw.rect(settings.screen, (44, 44, 84), button_5)

        speed_icon = pygame.image.load('./assets/shop/speed.png')
        speed_icon = pygame.transform.scale(speed_icon, (120, 120))
        settings.screen.blit(speed_icon, (180, 310))

        attack_icon = pygame.image.load('./assets/shop/attack.png')
        attack_icon = pygame.transform.scale(attack_icon, (120, 120))
        settings.screen.blit(attack_icon, (660, 310))

        more_icon = pygame.image.load('./assets/shop/more.png')
        more_icon = pygame.transform.scale(more_icon, (40, 40))
        settings.screen.blit(more_icon, (365, 465))
        settings.screen.blit(more_icon, (835, 465))

        less_icon = pygame.image.load('./assets/shop/less.png')
        less_icon = pygame.transform.scale(less_icon, (40, 40))
        settings.screen.blit(less_icon, (95, 465))
        settings.screen.blit(less_icon, (565, 465))

        draw_text('Speed', titleFont,
                  (255, 255, 255), settings.screen, 200, 240)

        draw_text(str(game.shooter.movementSpeed), titleFont,
                  (255, 255, 255), settings.screen, 235, 470)  
        
        draw_text('Attack', titleFont,
                  (255, 255, 255), settings.screen, 670, 240)

        draw_text(str(game.shooter.attack), titleFont,
                  (255, 255, 255), settings.screen, 700, 470)          

        draw_text('Magasin', titleFont, (255, 255, 255),
                  settings.screen, 430, 20)

        draw_text('Credits : '+ str(tokens), titleFont, (255, 255, 255),
                  settings.screen, 380, 120)

        draw_text('Lancer la partie', titleFont, (255, 255, 255),
                  settings.screen, 640, 720)
        


        if button_1.collidepoint((mx, my)):
            if click[0] == 1:
                if game.shooter.movementSpeed > 3 :
                    tokens += 100
                    data['partyTokens'].pop(0)
                    data['partyTokens'].append({"tokens": tokens})
                    save(data)
                    game.shooter.movementSpeed -= 1
                    time.sleep(0.5)
        if button_2.collidepoint((mx, my)):
            if click[0] == 1:
                if game.shooter.movementSpeed < 10 and tokens >= 100:
                    tokens -= 100
                    data['partyTokens'].pop(0)
                    data['partyTokens'].append({"tokens": tokens})
                    save(data)
                    game.shooter.movementSpeed += 1
                    time.sleep(0.5)
        if button_3.collidepoint((mx, my)):
            if click[0] == 1:
                if game.shooter.attack > 1 :
                    tokens += 100
                    data['partyTokens'].pop(0)
                    data['partyTokens'].append({"tokens": tokens})
                    save(data)
                    game.shooter.attack -= 1
                    time.sleep(0.5)
        if button_4.collidepoint((mx, my)):
            if click[0] == 1:
                if game.shooter.attack < 4 and tokens >= 100:
                    tokens -= 100
                    data['partyTokens'].pop(0)
                    data['partyTokens'].append({"tokens": tokens})
                    save(data)
                    game.shooter.attack += 1
                    time.sleep(0.5)
        if button_5.collidepoint((mx, my)):
            if click[0] == 1:
                settings.shopping = False
                running = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings.shopping = False
                    running = False

        pygame.display.flip()
        mainClock.tick(60)


def load(game):
    with open('save.json') as json_file:
        data = json.load(json_file)
        for value in data['playerInformations']:
            game.shooter.attack = value['playerAttack']
            game.shooter.movementSpeed = value['playerSpeed']
        for value in data['partyInformations']:
            game.score = value['score']


def instructions():
    running = True
    while running:
        settings.screen.fill((0, 0, 0))

        draw_text('Instructions', titleFont, (255, 255, 255),
                  settings.screen, 400, 20)
        draw_text('Bonjour jeune aventurier des temps modernes et bienvenu sur notre jeu.',
                  font, (255, 255, 255), settings.screen, 20, 70)
        draw_text("Tout d'abord voici la liste des commandes que tu dois connaitre :",
                  font, (255, 255, 255), settings.screen, 20, 95)
        draw_text("Se deplacer vers la droite : Fleche de droite ",
                  font, (255, 255, 255), settings.screen, 20, 140)
        draw_text("Se deplacer vers la gauche : Fleche de gauche ",
                  font, (255, 255, 255), settings.screen, 20, 165)
        draw_text("Tirer une balle : Espace ", font,
                  (255, 255, 255), settings.screen, 20, 190)
        draw_text("Retourner au menu precedent : Echap ", font,
                  (255, 255, 255), settings.screen, 20, 215)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        mainClock.tick(60)


def game_over(score):
    gameOverSound = pygame.mixer.Sound("assets/sounds/game_over.ogg")
    gameOverSound.set_volume(0.1)
    gameOverSound.play()
    running = True
    while running:
        click = pygame.mouse.get_pressed()

        settings.screen.blit(settings.gameOverBackground, (0, 0))
        # settings.screen.fill((0,0,0))

        draw_text('GAME OVER', fontgo, (255, 0, 0), settings.screen, 300, 100)
        draw_text('SCORE :' + str(score), titleFont, (255, 255, 255), settings.screen, 400, 200)
        draw_text("Tu t'es battu de toutes tes forces,", font,
                  (255, 255, 255), settings.screen, 310, 300)
        draw_text("mais cela n'a pas suffit.", font,
                  (255, 255, 255), settings.screen, 310, 350)
        draw_text("Tu peux toujours retenter ta chance", font,
                  (255, 255, 255), settings.screen, 310, 400)

        mx, my = pygame.mouse.get_pos()

        shadow_button1 = pygame.Rect(370, 560, 295, 50)
        button_1 = pygame.Rect(360, 570, 295, 50)

        if button_1.collidepoint((mx, my)):
            if click[0] == 1:
                settings.loadingGame = False
                game()
        # pygame.draw.rect(settings.screen, (255, 0, 0), button_1)
        pygame.draw.rect(settings.screen, (255, 77, 77), shadow_button1)
        pygame.draw.rect(settings.screen, (255, 0, 0), button_1)

        draw_text('Reessayer', titleFont, (255, 255, 255),
                  settings.screen, 435, 580)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()
        mainClock.tick(60)


main_menu()
