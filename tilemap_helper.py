import pygame as py
from random import randint, choice

py.init()
screen = py.display.set_mode((1920, 1152))
clock = py.time.Clock()

class Tile:
    def __init__(self, location, spritePath):
        self.location = location
        self.sprite = py.image.load(spritePath).convert_alpha()
        self.rect = self.sprite.get_rect()

    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

test = Tile((0, 0), "sprites//dirt_ground_5.png")
test2 = Tile((1, 0), "sprites//dirt_ground_5.png")

def get_random_tile(category):  
    """
    Category is what sprites will be randomly selected

    Categories are: 'dirt'
    """

    match category:
        case "dirt":
            dirtList = ["sprites//dirt_ground_5.png", "sprites//dirt_ground_4.png", "sprites//dirt_ground_3.png", "sprites//dirt_ground_2.png", "sprites//dirt_ground_1.png"]
            return choice(dirtList)
        
tiles = []

for j in range (9):
    for i in range(16):
        newTile = Tile((i, j), get_random_tile("dirt"))
        tiles.append(newTile)

running = True
while running:
    screen.fill((0, 0, 255))

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    for i in tiles: i.place(screen)

    test.place(screen)
    test2.place(screen)

    py.display.flip()

