import pygame as py
from random import randint, choice
import math

class Tile:
    def __init__(self, location, spritePath):
        self.location = location
        self.sprite = py.image.load(spritePath).convert_alpha()
        self.rect = self.sprite.get_rect()

    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

class Tilemap:
    def __init__(self, size, tileCategory):
        self.size = size
        baseTiles = []
        for x in range(size[0]):
            for y in range(size[1]):
                newTile = Tile((x, y), get_random_tile(tileCategory))
                baseTiles.append(newTile)

        self.tiles = baseTiles

    def draw(self, screen):
        for t in self.tiles: t.place(screen)

class Player:
    def __init__(self):
        self.location = (5, 5)
        self.sprite = py.image.load("sprites//MCfront//Idle.png").convert_alpha()
        self.rect = self.sprite.get_rect()

    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

def get_random_tile(category):  
    """
    Category is what sprites will be randomly selected

    Categories are: 'dirt'
    """

    match category:
        case "dirt":
            dirtList = ["sprites//dirt_ground_5.png", "sprites//dirt_ground_4.png", "sprites//dirt_ground_3.png", "sprites//dirt_ground_2.png", "sprites//dirt_ground_1.png"]
            return choice(dirtList)
        
def get_tile_mouse_pos():
    mousepos = py.mouse.get_pos()
    mouseX = math.floor(mousepos[0] / 128)
    mouseY = math.floor(mousepos[1] / 128)
    return (mouseX, mouseY)

py.init()

size = (16, 9)

screen = py.display.set_mode((size[0] * 128, size[1] * 128))
clock = py.time.Clock()

tilemap = Tilemap(size, "dirt")
player = Player()
      
running = True
while running:
    screen.fill((0, 0, 255))

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            player.location = get_tile_mouse_pos()

    tilemap.draw(screen)
    player.place(screen)

    py.display.flip()

