import pygame 

windowWidth, windowHeight = 850, 980

# font = pygame.font.SysFont('lunchtimedoublysoregular', 20)
# Import du background de l'appli 
gameBackground = pygame.image.load('assets/backgrounds/bg.jpg')

# Import du background du menu 
menuBackground = pygame.image.load('assets/backgrounds/menu_bg.jpg')
menuBackground = pygame.transform.scale(menuBackground, (windowHeight, windowWidth))


# Taille de l'écran
screen = pygame.display.set_mode((windowHeight,windowWidth))

icon = pygame.image.load('assets/ovni.png')