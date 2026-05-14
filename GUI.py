import pygame as py
import textwrap

class Popup():
    def __init__(self, text, color, buttons):
        self.text = text
        self.image = py.Surface((500, 500))
        self.rect = self.image.get_rect(topleft=(390, 390))
        self.buttons = buttons
        self.image.fill(color)
        self.font = py.font.Font("Fonts//Felipa-Regular.ttf", 38)
        self.words = textwrap.wrap(text, 30)

        for i in self.buttons: i.popup = self

    def draw(self, screen, isClicking):
        screen.blit(self.image, self.rect)
        for i, line in enumerate(self.words): # I actually just found out about enumerate. Jolly good function (even though its technically a class)
            textOut = self.font.render(line, True, (255, 255, 255))
            screen.blit(textOut, (440, 440 + (i * 45)))
        for i in self.buttons:
            i.draw(screen, isClicking)
    
        if any(i.clicked for i in self.buttons):
            return False
        return True

class PopupButton():
    def __init__(self, text, location):
        self.popup = None
        self.text = text
        self.location = location
        self.image = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525 / 2, 256 / 2))
        self.rect = self.image.get_rect(topleft=(location))
        self.font = py.font.Font("Fonts//Felipa-Regular.ttf", 38)
        self.words = self.font.render(text, True, (0, 0, 0))
        self.wordRect = self.words.get_rect(topleft=(location[0] + 100, location[1] + 35))
        self.clicked = False

    def draw(self, screen, isClicking):
        tint = self.image.copy()

        mousepos = py.mouse.get_pos()

        if self.rect.collidepoint(mousepos):
            tint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

            if isClicking:
                self.clicked = True
            
        screen.blit(tint, self.rect)
        screen.blit(self.words, self.wordRect)