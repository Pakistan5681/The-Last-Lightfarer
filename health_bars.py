import pygame as py
class Phealth():
    def __init__(self):
        self.sprite = py.image.load("sprites//GUI//health_bar.png").convert_alpha()

    def draw(self, screen):
        newImage = py.transform.scale(self.sprite, (200, 400))
        newRect = newImage.get_rect(topleft=(50, -50))
        screen.blit(newImage, newRect)


class PRbar():
    def __init__(self, player_max):
        self.image = py.Surface((player_max * 2, 40))    

    def draw(self, screen, pHealth):
        if pHealth < 0: pHealth = 0
        newImage = py.transform.scale(self.image, (pHealth * 2, 40))
        self.image.fill((255, 0, 0))
        newRect = newImage.get_rect(topleft=(50, 50))
        screen.blit(newImage, newRect)



