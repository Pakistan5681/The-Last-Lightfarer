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

class Weapon:
    def __init__(self, name, damage, type, range):
        self.name = name
        self.damage = damage
        self.type = type
        self.range = range

    def get_attack_squares(self, playerpos, screensize):
        squares = []

        if self.type == "warrior": # Warrior targets the adjacent squares 
            for x in range(playerpos[0] - self.range, playerpos[0] + self.range + 1):
                for y in range(playerpos[1] - self.range, playerpos[1] + self.range + 1):
                    if (x, y) != playerpos and x >= 0 and y >= 0: squares.append((x, y))
        elif self.type == "marksman": # Marksman targets in a cross + pattern
            for i in range(self.range * 3):
                if playerpos[1] + i >= 0 and (playerpos[0], playerpos[1] + i) != playerpos: squares.append((playerpos[0], playerpos[1] + i))
                if playerpos[1] - i >= 0 and (playerpos[0], playerpos[1] - i) != playerpos: squares.append((playerpos[0], playerpos[1] - i))
                if playerpos[0] + i >= 0 and (playerpos[0] + i, playerpos[1]) != playerpos: squares.append((playerpos[0] + i, playerpos[1]))
                if playerpos[0] - i >= 0 and (playerpos[0] - i, playerpos[1]) != playerpos: squares.append((playerpos[0] - i, playerpos[1]))
        elif self.type == "assasin": # Assasin targets in a diagonal x pattern
            for i in range(self.range * 3):
                if playerpos[0] + i >= 0 and playerpos[1] + i >= 0 and (playerpos[0] + i, playerpos[1] + i) != playerpos: squares.append((playerpos[0] + i, playerpos[1] + i))
                if playerpos[0] - i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] - i, playerpos[1] - i) != playerpos: squares.append((playerpos[0] - i, playerpos[1] - i))
                if playerpos[0] + i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] + i, playerpos[1] - i) != playerpos: squares.append((playerpos[0] + i, playerpos[1] - i))
                if playerpos[0] - i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] - i, playerpos[1] + i) != playerpos: squares.append((playerpos[0] - i, playerpos[1] + i))
        elif self.type == "blitzer": # Blitzer targets many random squares
            for i in range(self.range * 15):
                newSquare = playerpos
                while (newSquare in squares) or newSquare == playerpos:
                    newSquare = (randint(0, screensize[0]), randint(0, screensize[1]))

                squares.append(newSquare)

        return squares
    
class DisplaySprite:
    def __init__(self, spritepath, location):
        self.location = location
        self.sprite = py.image.load(spritepath).convert_alpha()
        self.rect = self.sprite.get_rect()
    
    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

class Player:
    def __init__(self):
        self.location = (5, 5)
        self.sprite = py.image.load("sprites//MCfront//Idle.png").convert_alpha()
        self.rect = self.sprite.get_rect()
        self.health = 100
        self.weapon = Weapon("Lantern", 5, "blitzer", 2)


    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

    def attack(self, screen, tilemapSize):
        attackTiles = self.weapon.get_attack_squares(self.location, tilemapSize)
        out = []
        for i in attackTiles:
            out.append(DisplaySprite("sprites//Indicators//attack_indicator.png", i))

        return out



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
attackSquares = None

currentTurn = "playerAttack" # A variable that decides what actions can take place (i.e. playerAttack means it is the players attack phase)

while running:
    screen.fill((0, 0, 255))

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            if currentTurn == "playerAttack":
                locations = []
                for i in attackSquares: locations.append(i.location)

                if get_tile_mouse_pos() in locations:
                    attackSquares = None
                    currentTurn = "enemies"

    tilemap.draw(screen)
    player.place(screen)

    if currentTurn == "playerAttack":
        if attackSquares == None : attackSquares = player.attack(screen, size)
        for i in attackSquares: i.place(screen)

    py.display.flip()