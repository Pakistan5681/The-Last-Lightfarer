import pygame as py

def death():
    screen = py.display.set_mode((1920, 1080))

    titleFont = py.font.Font("Fonts//Felipa-Regular.ttf", 150)
    buttonFont = py.font.Font("Fonts//Felipa-Regular.ttf", 75)

    mainTextS = titleFont.render("The Last Lightfarer", True, (255, 200, 0))

    startButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    startButtonText = buttonFont.render("Retart", True, (8, 0, 36))
    startRect = startButton.get_rect(topleft=(750, 250))

    quitButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    quitText = buttonFont.render("Quit", True, (8, 0, 36))
    quitRect = startButton.get_rect(topleft=(750, 500))

    playerImage = py.transform.scale(py.image.load("sprites//MCfront//Idle.png").convert_alpha(), (1000, 1000))
    playerRect = playerImage.get_rect(topleft=(-200, 50))

    monsterImage = py.transform.scale(py.image.load("sprites//sylf//sylphwing-left-facing-with-vfx.png.png").convert_alpha(), (600, 600))
    monsterRect = playerImage.get_rect(topleft=(1300, 250))

    running = True
    while running:
        screen.fill((0, 0, 0))
        mousepos = py.mouse.get_pos()

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

        screen.blit(mainTextS, (550, 50))

        screen.blit(startTint, startRect)
        screen.blit(startButtonText, (950, 320))

        screen.blit(quitTint, quitRect)
        screen.blit(quitText, (950, 570))

        

        py.display.flip()

