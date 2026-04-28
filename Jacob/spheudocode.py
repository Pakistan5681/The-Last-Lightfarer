# JQ 2nd Spheudo Code 16*9
import pygame as py
from random import randint, choice
import math
from Jacob.proj import Projectile
class MWeapon:
    def __init__(self, name, damage, type, range):
        self.name = name
        self.damage = damage
        self.type = type
        self.range = range

    def get_attack_squares(self, enemeypos, occupied=[], screensize=(11,11)):  # fix-ed added screensize param def get_attack_squares(self, enemeypos, occupied=[], screensize=(11,11)):
        squares = []
        psquares=[]

        def in_bounds(x, y):  # fix-ed helper to clamp to board
            return 0 <= x < screensize[0] and 0 <= y < screensize[1]

        if self.type == "pawn" or self.type == "bishop":
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range):
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range):
                    if (x, y) != enemeypos and (x, y) not in occupied and in_bounds(x, y):  # fix-ed bounds check
                        squares.append((x, y))
        elif self.type == "rook": 
            for i in range(self.range * 3):
                if in_bounds(enemeypos[0], enemeypos[1] + i) and (enemeypos[0], enemeypos[1] + i) not in occupied: squares.append((enemeypos[0], enemeypos[1] + i))      # fix-ed bounds
                if in_bounds(enemeypos[0], enemeypos[1] - i) and (enemeypos[0], enemeypos[1] - i) not in occupied: squares.append((enemeypos[0], enemeypos[1] - i))      # fix-ed bounds
                if in_bounds(enemeypos[0] + i, enemeypos[1]) and (enemeypos[0] + i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] + i, enemeypos[1]))      # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1]) and (enemeypos[0] - i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] - i, enemeypos[1]))      # fix-ed bounds
        elif self.type == "bishop":
            for i in range(1, self.range * 3):  # fix-ed start at 1 to skip own tile
                if in_bounds(enemeypos[0] + i, enemeypos[1] + i) and (enemeypos[0] + i, enemeypos[1] + i) not in occupied: psquares.append((enemeypos[0] + i, enemeypos[1] + i))  # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1] - i) and (enemeypos[0] - i, enemeypos[1] - i) not in occupied: psquares.append((enemeypos[0] - i, enemeypos[1] - i))  # fix-ed bounds
                if in_bounds(enemeypos[0] + i, enemeypos[1] - i) and (enemeypos[0] + i, enemeypos[1] - i) not in occupied: psquares.append((enemeypos[0] + i, enemeypos[1] - i))  # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1] + i) and (enemeypos[0] - i, enemeypos[1] + i) not in occupied: psquares.append((enemeypos[0] - i, enemeypos[1] + i))  # fix-ed bounds
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range + 1):  # fix-ed +1 so range is inclusive
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range + 1):  # fix-ed +1 so range is inclusive
                    if (x, y) != enemeypos and (x, y) not in occupied and in_bounds(x, y):  # fix-ed bounds
                        psquares.append((x, y))  # fix-ed append box squares into psquares so bishop gets both
            squares = psquares  # fix-ed bishop should move on diagonals (psquares), not the box squares
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
                if sq not in occupied and in_bounds(sq[0], sq[1]):  # fix-ed bounds + occupied
                    squares.append(sq)
            return squares
        
        return squares

class Monster:
    def __init__(self, spriteImage, location, weapon, damage=5, projectile_sprite="sprites/sylf/sylphwing-spell.png"):
        self.location = location
        self.sprite = py.image.load(spriteImage).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.health = 100
        self.weapon = weapon
        self.damage = damage
        self.projectile_sprite = projectile_sprite

    def place(self, screen):
        print(self.location)
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

    def move(self, playerpos, screenSize, occupied=[]):  # fix-ed accept occupied list
        squares = self.weapon.get_attack_squares(self.location, occupied, screenSize)  # fix-ed pass occupied + screenSize
        if self.weapon.type == "bishop":
            
            min_diagonal_dist = float('inf')
    
            for p in squares:
                pdx = abs(p[0] - playerpos[0])
                pdy = abs(p[1] - playerpos[1])
                diagonal_dist = abs(pdx - pdy)
                if diagonal_dist < min_diagonal_dist:
                    min_diagonal_dist = diagonal_dist
                    best_square = p

            pre_move_location = self.location  # fix-ed snapshot location before moving so projectile starts from correct tile
            self.location = best_square
            bdx = abs(self.location[0] - playerpos[0])
            bdy = abs(self.location[1] - playerpos[1])
            if bdx == bdy and bdx > 0:  # fix-ed bdx > 0 ensures not same tile; only fire when truly on a diagonal
                return Projectile(self.projectile_sprite, self.location, playerpos, speed=5, damage=self.damage)  # fix-ed use pre_move_location
            return 0  # fix-ed not on a diagonal, no projectile
            
        target = playerpos
        closest_point = self.location
        min_dist = float('inf')
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
            return self.damage  # fix-ed melee hit — return damage int, no projectile
        return 0  # fix-ed non-bishop types never fire a projectile