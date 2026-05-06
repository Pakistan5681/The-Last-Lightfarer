import pygame as py
from paxtons_helpers import DisplaySprite

py.init()

def menu():
    screen = py.display.set_mode((1920, 1080))

    titleFont = py.font.Font("Fonts//Felipa-Regular.ttf", 150)
    buttonFont = py.font.Font("Fonts//Felipa-Regular.ttf", 75)

    mainTextS = titleFont.render("The Last Lightfarer", True, (255, 200, 0))

    startButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    startButtonText = buttonFont.render("Start", True, (8, 0, 36))
    startRect = startButton.get_rect()

    quitButton = py.image.load("sprites//GUI//button.png").convert_alpha()
    startRect = startButton.get_rect()

    running = True
    while running:
        screen.fill((18, 0, 99))

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.blit(mainTextS, (550, 50))

        screen.blit(startButton, (750, 250))
        screen.blit(startButtonText, (950, 320))

        py.display.flip()

menu()