import pygame as py
class Phealth():
    def __init__(self):
        self.sprite = py.image.load("sprites//MCfront//Idle.png").convert_alpha()
        self.rect = self.sprite.get_rect()
        self.rect.center = (0,0)
        self.speed = 5


class PRbar():
    def __init__(self,player_max,player_current):
        self.image = py.Surface((50, 50))
        self.image.fill((0, 255, 0)) 
        self.rect = self.image.get_rect()
        self.rect.center = (0,0)
        new_width = self.rect.width - 10
        if new_width > 0:
            new_image = py.transform.scale(self.rect, (new_width, self.rect.height))
            self.rect = new_image
            self.rect.width = new_width


