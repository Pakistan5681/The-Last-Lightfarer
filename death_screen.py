import pygame as py

def death():
    screen = py.display.set_mode((1920, 1080))

    titleFont = py.font.Font("Fonts//Felipa-Regular.ttf", 150)
    buttonFont = py.font.Font("Fonts//Felipa-Regular.ttf", 75)

    mainTextS = titleFont.render("You Died", True, (176, 0, 0))

    startButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    startButtonText = buttonFont.render("Retart", True, (8, 0, 36))
    startRect = startButton.get_rect(topleft=(650, 250))

    quitButton = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    quitText = buttonFont.render("Quit", True, (8, 0, 36))
    quitRect = startButton.get_rect(topleft=(650, 500))

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

        screen.blit(mainTextS, (650, 50))

        screen.blit(startTint, startRect)
        screen.blit(startButtonText, (850, 320))

        screen.blit(quitTint, quitRect)
        screen.blit(quitText, (850, 570))

        

        py.display.flip()

