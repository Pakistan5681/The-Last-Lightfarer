# JQ 2nd Spheudo Code 16*9
import pygame as py
from random import randint, choice
import math
from Jacob.projectile import Projectile
class Weapon:
    def __init__(self, name, damage, type, range):
        self.name = name
        self.damage = damage
        self.type = type
        self.range = range

    def get_attack_squares(self, enemeypos,occupied=[]):
        squares = []
        psquares=[]
        if self.type == "pawn":
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range):
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range):
                    if (x, y) != enemeypos and (x, y) not in occupied: squares.append((x, y))
        elif self.type == "rook": 
            for i in range(self.range * 3):
                if (enemeypos[0], enemeypos[1] + i) not in occupied: squares.append((enemeypos[0], enemeypos[1] + i))
                if (enemeypos[0], enemeypos[1] - i) not in occupied: squares.append((enemeypos[0], enemeypos[1] - i))
                if (enemeypos[0] + i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] + i, enemeypos[1]))
                if (enemeypos[0] - i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] - i, enemeypos[1]))
        elif self.type == "bishop": 
            for i in range(self.range * 3):
                psquares.append((enemeypos[0] + i, enemeypos[1] + i))
                psquares.append((enemeypos[0] - i, enemeypos[1] - i))
                psquares.append((enemeypos[0] + i, enemeypos[1] - i))
                psquares.append((enemeypos[0] - i, enemeypos[1] + i))
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range):
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range):
                    if (x, y) != enemeypos and (x, y) not in occupied: squares.append((x, y))
        elif self.type == "Knight":
            knight_moves = [
                (enemeypos[0] + 2, enemeypos[1] + 1),
                (enemeypos[0] + 2, enemeypos[1] - 1),
                (enemeypos[0] - 2, enemeypos[1] + 1),
                (enemeypos[0] - 2, enemeypos[1] - 1),
                (enemeypos[0] + 1, enemeypos[1] + 2),
                (enemeypos[0] - 1, enemeypos[1] + 2),
                (enemeypos[0] + 1, enemeypos[1] - 2),
                (enemeypos[0] - 1, enemeypos[1] - 2),
            ]
            for sq in knight_moves:
                if sq not in occupied:
                    squares.append(sq)
            return squares
        return squares         
class Monster:
    def __init__(self, spriteImage, location, weapon, damage, projectile_sprite="sprites/sylf/sylphwing-spell.png"):
        self.location = location
        self.sprite = py.image.load(spriteImage).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.health = 100
        self.weapon = weapon
        self.damage = damage
        self.projectile_sprite =projectile_sprite 

    def place(self, screen):
        print(self.location)
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

    def move(self, playerpos, screenSize):
        squares = self.weapon.get_attack_squares(self.location)
        if self.weapon.type == "bishop":
            best_square = self.location
            min_diagonal_dist = float('inf')
    
            for p in squares:
                pdx = abs(p[0] - playerpos[0])
                pdy = abs(p[1] - playerpos[1])
                diagonal_dist = abs(pdx - pdy)
                if diagonal_dist < min_diagonal_dist:
                    min_diagonal_dist = diagonal_dist
                    best_square = p
    
            self.location = best_square
            bdx = abs(self.location[0] - playerpos[0])
            bdy = abs(self.location[1] - playerpos[1])
            if bdx == bdy:
                return Projectile(self.projectile_sprite, self.location, playerpos, speed=5, damage=self.damage)
            return 0
        target = playerpos
        closest_point = self.location
        min_dist = float('inf') # Start with infinity
        for p in squares:
            dist = math.sqrt((p[0] - target[0])**2 + (p[1] - target[1])**2)
            print(f"distance: {dist}")
            if dist < min_dist:
                min_dist = dist
                closest_point = p

        self.location = closest_point   
        dx = abs(self.location[0] - playerpos[0])
        dy = abs(self.location[1] - playerpos[1])
        if dx <= 1 and dy <= 1 and (dx + dy) > 0:
                return self.damage
        return 0

# Create class monster
#   initialize with:
#       name
#       damage
#       type
#       range
#       ranged
# if monster type is bishop, graph all squares in an x shape
# if monster type is knight, graph all squares in an x shape jump pattern
# if monster type is rook, graph all squares in an + shape
# if monster type is pawn, graph all squares in an square shape
#        if self.type == "bishop":
#            for p in squares:
#                out = []
#                out.append(DisplaySprite("sprites//Indicators//attack_indicator.png", i))
#                dist = math.sqrt((p[0] - target[0])**2 + (p[1] - target[1])**2)
#                if dist < min_dist:
#                    min_dist = dist
#                    closest_point = p
#            self.location = closest_point
#            if self.weapon.type == "bishop":
    # Find which of the 4 diagonals the player is on relative to the monster
    # A square is on the same diagonal if dx == dy
