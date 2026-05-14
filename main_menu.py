import pygame as py
from michael.saving_loading import loadCurrentLevel

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

    save1 = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    save1Text = buttonFont.render("Save 1", True, (8, 0, 36))
    save1Rect = save1.get_rect(topleft=(700, 250))

    save2= py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    save2text = buttonFont.render("Save 2", True, (8, 0, 36))
    save2rect = save2.get_rect(topleft=(700, 500))

    save3= py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525, 256))
    save3text = buttonFont.render("Save 3", True, (8, 0, 36))
    save3rect = save3.get_rect(topleft=(700, 750))

    playerImage = py.transform.scale(py.image.load("sprites//MCfront//Idle.png").convert_alpha(), (1000, 1000))
    playerRect = playerImage.get_rect(topleft=(-200, 50))

    monsterImage = py.transform.scale(py.image.load("sprites//sylf//sylphwing-left-facing-with-vfx.png.png").convert_alpha(), (600, 600))
    monsterRect = playerImage.get_rect(topleft=(1300, 250))

    colorR = 18
    colorB = 99

    clock = 0
    inverted = False

    saveMenu = False

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

        clicked = False
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True

        if not saveMenu:
            startTint = startButton.copy()
            quitTint = quitButton.copy()

            if startRect.collidepoint(mousepos):
                startTint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

                if clicked:
                    saveMenu = True

            if quitRect.collidepoint(mousepos):
                quitTint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

                if clicked:
                    return False   
                
            screen.blit(startTint, startRect)
            screen.blit(startButtonText, (900, 320))
    
            screen.blit(quitTint, quitRect)
            screen.blit(quitText, (900, 570)) 
        else:
            save1Tint = save1.copy()
            save2Tint = save2.copy()
            save3Tint = save3.copy()

            if save1Rect.collidepoint(mousepos):
                save1Tint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

                if clicked:
                    result = loadCurrentLevel(1)
                    if result != "fail":
                        return result, 1
                    else:
                        return "new_game", 1
                
            if save2rect.collidepoint(mousepos):
                save2Tint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

                if clicked:
                    result = loadCurrentLevel(2)
                    if result != "fail":
                        return result, 2
                    else:
                        return "new_game", 2
                
            if save3rect.collidepoint(mousepos):
                save3Tint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

                if clicked:
                    result = loadCurrentLevel(3)
                    if result != "fail":
                        return result, 3
                    else:
                        return "new_game", 3
                
            screen.blit(save1Tint, save1Rect)
            screen.blit(save2Tint, save2rect)
            screen.blit(save3Tint, save3rect)
            screen.blit(save1Text, (900, 320))
            screen.blit(save2text, (900, 570))
            screen.blit(save3text, (900, 820))
   
        screen.blit(playerImage, playerRect)
        screen.blit(monsterImage, monsterRect)

        screen.blit(mainTextS, (500, 50))          

        py.display.flip()