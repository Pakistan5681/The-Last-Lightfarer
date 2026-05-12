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



class MPhealth():
    def __init__(self,mLocation):
        self.sprite = py.image.load("sprites//GUI//health_bar.png").convert_alpha()
        self.x = float(mLocation[0] * 128)
        self.y = float(mLocation[1] * 128) 

    def draw(self, screen):
        newImage = py.transform.scale(self.sprite, (200, 400))
        up = self.y + 28
        newRect = newImage.get_rect(topleft=(self.x,up))
        screen.blit(newImage, newRect)


class MPRbar():
    def __init__(self, player_max,mLocation):
        self.image = py.Surface((player_max * 2, 40))
        self.x = float(mLocation[0] * 128)
        self.y = float(mLocation[1] * 128)   

    def draw(self, screen, mHealth):
        location = ()
        if mHealth < 0:mpHealth = 0
        newImage = py.transform.scale(self.image, (mHealth * 2, 40))
        self.image.fill((255, 0, 0))
        up = self.y + 28
        newRect = newImage.get_rect(topleft=(self.x,up))
        screen.blit(newImage, newRect)


