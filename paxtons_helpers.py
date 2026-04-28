import pygame as py
from random import randint, choice
import math
from Jacob.spheudocode import Monster, MWeapon
from time import sleep
from Jacob.proj import Projectile
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
    def __init__(self, size, tilemap):
        self.size = size
        self.tiles = tilemap

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
            for i in range((self.range * 2) + 1):
                if playerpos[1] + i >= 0 and (playerpos[0], playerpos[1] + i) != playerpos: squares.append((playerpos[0], playerpos[1] + i))
                if playerpos[1] - i >= 0 and (playerpos[0], playerpos[1] - i) != playerpos: squares.append((playerpos[0], playerpos[1] - i))
                if playerpos[0] + i >= 0 and (playerpos[0] + i, playerpos[1]) != playerpos: squares.append((playerpos[0] + i, playerpos[1]))
                if playerpos[0] - i >= 0 and (playerpos[0] - i, playerpos[1]) != playerpos: squares.append((playerpos[0] - i, playerpos[1]))
        elif self.type == "assassin": # assassin targets in a diagonal x pattern
            for i in range((self.range * 2) + 1):
                if playerpos[0] + i >= 0 and playerpos[1] + i >= 0 and (playerpos[0] + i, playerpos[1] + i) != playerpos: squares.append((playerpos[0] + i, playerpos[1] + i))
                if playerpos[0] - i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] - i, playerpos[1] - i) != playerpos: squares.append((playerpos[0] - i, playerpos[1] - i))
                if playerpos[0] + i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] + i, playerpos[1] - i) != playerpos: squares.append((playerpos[0] + i, playerpos[1] - i))
                if playerpos[0] - i >= 0 and playerpos[1] + i >= 0 and (playerpos[0] - i, playerpos[1] + i) != playerpos: squares.append((playerpos[0] - i, playerpos[1] + i))
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
        self.weapon = Weapon("Lantern", 5, "blitzer", 1)
        self.speed = 5

    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

    def attack(self, tilemapSize):
        attackTiles = self.weapon.get_attack_squares(self.location, tilemapSize)
        out = []
        for i in attackTiles:
            out.append(DisplaySprite("sprites//Indicators//attack_indicator.png", i))

        return out
    
    def move(self, monsters):
        squares = []
        for x in range(self.location[0] - self.speed, self.location[0] + self.speed + 1):
            for y in range(self.location[1] - self.speed, self.location[1] + self.speed + 1):
                if (x, y) != self.location and x >= 0 and y >= 0 and (not (x, y) in monsters): squares.append(DisplaySprite("sprites//Indicators//move_indicator.png", (x, y)))

        return squares


def get_random_tile(category):  
    """
    Category is what sprites will be randomly selected

    Categories are: 'dirt'
    """

    match category:
        case "dirt":
            dirtList = ["sprites//Tiles//dirt//dirt_ground_5.png", "sprites//Tiles//dirt//dirt_ground_4.png", "sprites//Tiles//dirt//dirt_ground_3.png", "sprites//Tiles//dirt//dirt_ground_2.png", "sprites//Tiles//dirt//dirt_ground_1.png"]
            return choice(dirtList)
        
def get_tile_mouse_pos():
    mousepos = py.mouse.get_pos()
    mouseX = math.floor(mousepos[0] / 128)
    mouseY = math.floor(mousepos[1] / 128)
    return (mouseX, mouseY)

py.init()

size = (10, 10)

screen = py.display.set_mode((size[0] * 128, size[1] * 128))
clock = py.time.Clock()

tilemap = Tilemap(size, "dirt")
player = Player()

monsters = [Monster("sprites/flame hop/flame hopper v1-1.png.png", (3, 3), MWeapon("Generic Ah Weapon", 5, "bishop", 2),5)]
running = True
attackSquares = None
moveSquares = None
active_projectiles = []  # fix-ed list to hold live projectiles so they can be drawn 

currentTurn = "playerAttack" # A variable that decides what actions can take place (i.e. playerAttack means it is the players attack phase)

while running:
    screen.fill((0, 0, 255))

    tilemap.draw(screen)
    player.place(screen)

    monsterPos = []

    for i in monsters: 
        i.place(screen)
        monsterPos.append(i.location)

    if currentTurn == "playerAttack":
        if attackSquares == None : attackSquares = player.attack(size)
        for i in attackSquares: i.place(screen)
    elif currentTurn == "playerMove":
        if moveSquares == None: moveSquares = player.move(monsterPos)
        for i in moveSquares: i.place(screen)
    else:
        # fix-ed pass monsterPos as occupied so monsters don't stack on each other or the player
        occupied = monsterPos + [player.location]
        for i in monsters:
            result = i.move(player.location, size, occupied)  # fix-ed capture return value
            if isinstance(result, Projectile):                 # fix-ed store projectile if one was returned
                active_projectiles.append(result)
        currentTurn = "playerMove"

    # fix-ed draw and update all live projectiles every frame
    for proj in active_projectiles[:]:
        proj.draw(screen, player)
        if not proj.alive:
            active_projectiles.remove(proj)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:
                if currentTurn == "playerAttack":
                    locations = []
                    for i in attackSquares: locations.append(i.location)

                    if get_tile_mouse_pos() in locations:
                        attackSquares = None
                        currentTurn = "monsterMove"
                elif currentTurn == "playerMove":
                    locations = []
                    for i in moveSquares: locations.append(i.location)

                    if get_tile_mouse_pos() in locations:
                        moveSquares = None
                        player.location = get_tile_mouse_pos()
                        currentTurn = "playerAttack"

    py.display.flip()