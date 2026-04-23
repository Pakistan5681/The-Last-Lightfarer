# JQ 2nd Spheudo Code 16*9
import pygame as py
from random import randint, choice
import math

class Weapon:
    def __init__(self, name, damage, type, range,ranged,playerpos):
        self.name = name
        self.damage = damage
        self.type = type
        self.range = range
        self.ranged = ranged

    def get_attack_squares(self, enemeypos, screensize):
        squares = []
        psquares=[]
        if self.type == "pawn": # Warrior targets the adjacent squares 
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range):
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range):
                    if (x, y) != enemeypos: squares.append((x, y))
        elif self.type == "rook": # Marksman targets in a cross + pattern
            for i in range(self.range * 3):
                squares.append((enemeypos[0], enemeypos[1] + i))
                squares.append((enemeypos[0], enemeypos[1] - i))
                squares.append((enemeypos[0] + i, enemeypos[1]))
                squares.append((enemeypos[0] - i, enemeypos[1]))
        elif self.type == "bishop": # Assasin targets in a diagonal x pattern
            for i in range(self.range * 3):
                psquares.append((enemeypos[0] + i, enemeypos[1] + i))
                psquares.append((enemeypos[0] - i, enemeypos[1] - i))
                psquares.append((enemeypos[0] + i, enemeypos[1] - i))
                psquares.append((enemeypos[0] - i, enemeypos[1] + i))
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range):
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range):
                    if (x, y) != enemeypos: squares.append((x, y))      
        elif self.type == "Knight": # Blitzer targets many random squares
            for i in range(self.range * 15):
                squares.append((enemeypos[0] + i, enemeypos[1] + 1))
                squares.append((enemeypos[0] + i, enemeypos[1] - 1))
                squares.append((enemeypos[0] - i, enemeypos[1] - 1))
                squares.append((enemeypos[0] - i, enemeypos[1] + 1))
                squares.append((enemeypos[0] -1, enemeypos[1] + i))
                squares.append((enemeypos[0] +1, enemeypos[1] + i))
                squares.append((enemeypos[0] -1, enemeypos[1] - i))
                squares.append((enemeypos[0] +1, enemeypos[1] - i))
    def attacking(squares,playerpos):
        if self.type == "bishop":

        for ex, ey in squares:
            playerpos 
        

class Monster:
    def __init__(self,sprite):
        self.location = (7, 5)
        self.sprite = py.image.load(sprite).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.health = 100


    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

# Create class monster
#   initialize with:
#       name
#       damage
#       type
#       range
#       ranged