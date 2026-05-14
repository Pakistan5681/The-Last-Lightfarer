import pygame as py
from random import randint, choice, choices # choices is like choice with weights ig
import math
from GUI import Popup, PopupButton
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Projectile:
    def __init__(self, spritePath, startpos, targetpos, speed, damage):       
        self.x = float(startpos[0] * 128)
        self.y = float(startpos[1] * 128)
        self.targetx = float(targetpos[0] * 128)
        self.targety = float(targetpos[1] * 128)
        self.speed = speed
        self.damage = damage
        self.alive = True
        angle = -math.degrees(math.atan2((self.targety - self.y), (self.targetx - self.x)))
        baseSprite = py.transform.scale(py.image.load(spritePath).convert_alpha(),(400,400))
        self.sprite = py.transform.rotate(baseSprite, angle)

    def draw(self, screen, player):
        horizontal_distance = self.targetx - self.x
        vertical_distance = self.targety - self.y
        total_distance = math.sqrt(horizontal_distance**2 + vertical_distance**2)

        if total_distance <= self.speed:
            self.alive = False
        else:
            self.x += (horizontal_distance / total_distance) * self.speed
            self.y += (vertical_distance / total_distance) * self.speed
            scaled_sprite = py.transform.scale(self.sprite, (128, 128))
            screen.blit(scaled_sprite, (self.x, self.y))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
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

        if self.type == "pawn":
            for x in range(enemeypos[0] - self.range, enemeypos[0] + self.range):
                for y in range(enemeypos[1] - self.range, enemeypos[1] + self.range):
                    if (x, y) != enemeypos and (x, y) not in occupied and in_bounds(x, y):
                        squares.append((x, y))
        elif self.type == "rook": 
            for i in range(1, self.range + 1):
                if in_bounds(enemeypos[0], enemeypos[1] + i) and (enemeypos[0], enemeypos[1] + i) not in occupied: squares.append((enemeypos[0], enemeypos[1] + i))      # fix-ed bounds
                if in_bounds(enemeypos[0], enemeypos[1] - i) and (enemeypos[0], enemeypos[1] - i) not in occupied: squares.append((enemeypos[0], enemeypos[1] - i))      # fix-ed bounds
                if in_bounds(enemeypos[0] + i, enemeypos[1]) and (enemeypos[0] + i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] + i, enemeypos[1]))      # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1]) and (enemeypos[0] - i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] - i, enemeypos[1]))      # fix-ed bounds
        elif self.type == "bishop":
            for i in range(1, self.range + 1):  # fix-ed start at 1 to skip own tile
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
                if sq not in occupied and in_bounds(sq[0], sq[1]): 
                    squares.append(sq)
            return squares
        elif self.type == "queen":
            for i in range(1, self.range + 1):
                if in_bounds(enemeypos[0], enemeypos[1] + i) and (enemeypos[0], enemeypos[1] + i) not in occupied: squares.append((enemeypos[0], enemeypos[1] + i))      # fix-ed bounds
                if in_bounds(enemeypos[0], enemeypos[1] - i) and (enemeypos[0], enemeypos[1] - i) not in occupied: squares.append((enemeypos[0], enemeypos[1] - i))      # fix-ed bounds
                if in_bounds(enemeypos[0] + i, enemeypos[1]) and (enemeypos[0] + i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] + i, enemeypos[1]))      # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1]) and (enemeypos[0] - i, enemeypos[1]) not in occupied: squares.append((enemeypos[0] - i, enemeypos[1]))      # fix-ed bounds
            for i in range(1, self.range + 1):
                if in_bounds(enemeypos[0] + i, enemeypos[1] + i) and (enemeypos[0] + i, enemeypos[1] + i) not in occupied: squares.append((enemeypos[0] + i, enemeypos[1] + i))  # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1] - i) and (enemeypos[0] - i, enemeypos[1] - i) not in occupied: squares.append((enemeypos[0] - i, enemeypos[1] - i))  # fix-ed bounds
                if in_bounds(enemeypos[0] + i, enemeypos[1] - i) and (enemeypos[0] + i, enemeypos[1] - i) not in occupied: squares.append((enemeypos[0] + i, enemeypos[1] - i))  # fix-ed bounds
                if in_bounds(enemeypos[0] - i, enemeypos[1] + i) and (enemeypos[0] - i, enemeypos[1] + i) not in occupied: squares.append((enemeypos[0] - i, enemeypos[1] + i))  # fix-ed bounds

        return squares 

class Monster:
    def __init__(self, spriteImage, health, location, weapon, damage=5, projectile_sprite="sprites/sylf/sylphwing-spell.png"):
        self.location = location
        self.sprite = py.image.load(spriteImage).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.health = health
        self.weapon = weapon
        self.damage = damage
        self.projectile_sprite = projectile_sprite
        self.fight = False

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
                self.fight = True
                return Projectile(self.projectile_sprite, self.location, playerpos, speed=5, damage=self.damage)  # fix-ed use pre_move_location
            return 0  # fix-ed not on a diagonal, no projectile

        if self.weapon.type == "pawn":
            target = playerpos
            closest_point = self.location
            min_dist = float('inf')
            for p in squares:
                dist = math.sqrt((p[0] - target[0])**2 + (p[1] - target[1])**2)
                print(f"distance: {dist}")
                if dist < min_dist:
                    min_dist = dist
                    closest_point = p
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
        return self.damage  # fix-ed non-bishop types never fire a projectile
    

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------



class Tile:
    def __init__(self, location, spritePath, isWall):
        self.location = location
        self.sprite = py.image.load(spritePath).convert_alpha()
        self.rect = self.sprite.get_rect()
        self.spritePath = spritePath
        self.isWall = isWall

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

class Level:
    def __init__(self, tilemap, monsters):
        self.tilemap = tilemap
        self.monsters = monsters

    def get_level_data(self):
        return self.tilemap, self.monsters

class Weapon:
    def __init__(self, name, damage, type, range):
        self.name = name
        self.damage = damage
        self.type = type
        self.range = range

    def getIsWall(self, position, tiles):
        for t in tiles:
            if t.location == position:
                if t.isWall: return True
                else: return False

    def get_attack_squares(self, playerpos, screensize, tiles):
        squares = []

        if self.type == "warrior": # Warrior targets the adjacent squares 
            for x in range(playerpos[0] - self.range, playerpos[0] + self.range + 1):
                for y in range(playerpos[1] - self.range, playerpos[1] + self.range + 1):
                    if (x, y) != playerpos and x >= 0 and y >= 0 and not self.getIsWall((x, y), tiles): squares.append((x, y))
        elif self.type == "marksman": # Marksman targets in a cross + pattern
            for i in range((self.range * 2) + 1):
                if playerpos[1] + i >= 0 and (playerpos[0], playerpos[1] + i) != playerpos and not self.getIsWall((playerpos[0], playerpos[1] + i), tiles): squares.append((playerpos[0], playerpos[1] + i))
                if playerpos[1] - i >= 0 and (playerpos[0], playerpos[1] - i) != playerpos and not self.getIsWall((playerpos[0], playerpos[1] - i), tiles): squares.append((playerpos[0], playerpos[1] - i))
                if playerpos[0] + i >= 0 and (playerpos[0] + i, playerpos[1]) != playerpos and not self.getIsWall((playerpos[0] + i, playerpos[1]), tiles): squares.append((playerpos[0] + i, playerpos[1]))
                if playerpos[0] - i >= 0 and (playerpos[0] - i, playerpos[1]) != playerpos and not self.getIsWall((playerpos[0] - i, playerpos[1]), tiles): squares.append((playerpos[0] - i, playerpos[1]))
        elif self.type == "assassin": # assassin targets in a diagonal x pattern
            for i in range((self.range * 2) + 1):
                if playerpos[0] + i >= 0 and playerpos[1] + i >= 0 and (playerpos[0] + i, playerpos[1] + i) != playerpos and not self.getIsWall((playerpos[0] + i, playerpos[1] + i), tiles): squares.append((playerpos[0] + i, playerpos[1] + i))
                if playerpos[0] - i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] - i, playerpos[1] - i) != playerpos and not self.getIsWall((playerpos[0] - i, playerpos[1] - i), tiles): squares.append((playerpos[0] - i, playerpos[1] - i))
                if playerpos[0] + i >= 0 and playerpos[1] - i >= 0 and (playerpos[0] + i, playerpos[1] - i) != playerpos and not self.getIsWall((playerpos[0] + i, playerpos[1] - i), tiles): squares.append((playerpos[0] + i, playerpos[1] - i))
                if playerpos[0] - i >= 0 and playerpos[1] + i >= 0 and (playerpos[0] - i, playerpos[1] + i) != playerpos and not self.getIsWall((playerpos[0] - i, playerpos[1] + i), tiles): squares.append((playerpos[0] - i, playerpos[1] + i))
        elif self.type == "blitzer": # Blitzer targets many random squares
            for i in range(self.range * 15):
                newSquare = playerpos
                while (newSquare in squares) or newSquare == playerpos:
                    newSquare = (randint(0, screensize[0]), randint(0, screensize[1]))

                if not self.getIsWall(newSquare, tiles): squares.append(newSquare)

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
    def __init__(self, weapon=Weapon("Lantern", 50, "blitzer", 1), health=100, speed=5):
        self.location = (7, 5)
        self.sprite = py.image.load("sprites//MCfront//Idle.png").convert_alpha()
        self.rect = self.sprite.get_rect()
        self.health = 100
        self.weapon = Weapon("Lantern", 50, "blitzer", 2)
        self.speed = 5

    def place(self, screen):
        self.rect.topleft = ((self.location[0]) * 128, (self.location[1]) * 128)
        outSprite = py.transform.scale(self.sprite, (128, 128))
        screen.blit(outSprite, self.rect.topleft)

    def attack(self, tilemapSize, tiles):
        attackTiles = self.weapon.get_attack_squares(self.location, tilemapSize, tiles)
        out = []
        for i in attackTiles:
            out.append(DisplaySprite("sprites//Indicators//attack_indicator.png", i))

        return out
    
    def getIsWall(self, position, tiles):
        for t in tiles:
            if t.location == position:
                if t.isWall: return True
                else: return False
    
    def move(self, monsters, tiles):
        squares = []
        for x in range(self.location[0] - self.speed, self.location[0] + self.speed + 1):
            for y in range(self.location[1] - self.speed, self.location[1] + self.speed + 1):
                if (x, y) != self.location and x >= 0 and y >= 0 and (not (x, y) in monsters) and not self.getIsWall((x, y), tiles): squares.append(DisplaySprite("sprites//Indicators//move_indicator.png", (x, y)))

        return squares
    
def proj_transition(activeProjectiles, screen, player, monsters, tilemap):
    while activeProjectiles:
        screen.fill((0, 0, 255))
        
        tilemap.draw(screen)
        player.place(screen)

        for i in monsters: 
            i.place(screen)

        for i in activeProjectiles:
            i.draw(screen, player)
            if not i.alive: activeProjectiles.remove(i)

        py.display.flip()

def create_weapon_name():
    weaponNames1 = ["Light", "Dark", "Eternity", "Vast", "End", "Void", "Bright"]
    weaponNames2 = ["bringer", "ender", "crusher", "flame", "singer", "splitter", "lance"]
    return choice(weaponNames1) + choice(weaponNames2)

def create_random_weapon(levelIndex):
    name = create_weapon_name()
    if levelIndex == 1: levelIndex = 0
    damage = randint(round(20 + (levelIndex / 10)), round(40 + (levelIndex / 10)))
    wType = choice(["warrior", "marksman", "assassin", "blitzer"])
    wRange = choices([1, 2, 3], [6, 3, 1])[0]
    return Weapon(name, damage, wType, wRange)

def weapon_popup(screen,currentWeapon, level, tilemap, player):
    newWeapon = create_random_weapon(level)
    popup = Popup(f"""You got the {newWeapon.name} \nDamage: {newWeapon.damage} \nType: {newWeapon.type} \nRange: {newWeapon.range}
""", (8, 0, 36), [PopupButton("Grab", (315, 775)), PopupButton("Leave", (715, 775))])
    while True:
        screen.fill((0, 0, 0))
        tilemap.draw(screen)
        player.place(screen)
        clicking = False
        for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                    clicking = True
        popup.draw(screen, clicking)
        if popup.buttons[0].clicked:
            return newWeapon
        elif popup.buttons[1].clicked:
            return currentWeapon
        
        py.display.flip()

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