import pygame as py

py.init()

def menu():
    screen = py.display.set_mode((1920, 1080))

    titleFont = py.font.Font("Fonts//Felipa-Regular.ttf", 150)
    buttonFont = py.font.Font("Fonts//Felipa-Regular.ttf", 75)

    mainTextS = titleFont.render("The Last Lightfarer", True, (255, 200, 0))

    startButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    startButtonText = buttonFont.render("Start", True, (8, 0, 36))
    startRect = startButton.get_rect(topleft=(700, 250))

    quitButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    quitText = buttonFont.render("Quit", True, (8, 0, 36))
    quitRect = startButton.get_rect(topleft=(700, 500))

    playerImage = py.transform.scale(py.image.load("sprites//MCfront//Idle.png").convert_alpha(), (1000, 1000))
    playerRect = playerImage.get_rect(topleft=(-200, 50))

    monsterImage = py.transform.scale(py.image.load("sprites//sylf//sylphwing-left-facing-with-vfx.png.png").convert_alpha(), (600, 600))
    monsterRect = playerImage.get_rect(topleft=(1300, 250))

    colorR = 18
    colorB = 99

    clock = 0
    inverted = False

    running = True
    while running:
        screen.fill((colorR, 0, colorB))
        
        mousepos = py.mouse.get_pos()

        if clock < 1000:
            clock += 1
        else:
            clock = 0
            inverted = not inverted

        if inverted:
            colorB -= 0.05
            colorR -= 0.05
        else:
            colorB += 0.05
            colorR += 0.05

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        mouse_buttons = py.mouse.get_pressed()

        startTint = startButton.copy()
        quitTint = quitButton.copy()

        if startRect.collidepoint(mousepos):
            startTint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

            if mouse_buttons[0]:
                return True
            
        if quitRect.collidepoint(mousepos):
            quitTint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

            if mouse_buttons[0]:
                return False   
        
        screen.blit(playerImage, playerRect)
        screen.blit(monsterImage, monsterRect)

        screen.blit(mainTextS, (500, 50))

        screen.blit(startTint, startRect)
        screen.blit(startButtonText, (900, 320))

        screen.blit(quitTint, quitRect)
        screen.blit(quitText, (900, 570))    

        py.display.flip()