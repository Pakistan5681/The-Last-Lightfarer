import pygame as py
from paxtons_helpers import Player, Tile, Tilemap, get_tile_mouse_pos
from Jacob.spheudocode import MWeapon, Monster
from Jacob.proj import Projectile

py.init()

size = (10, 10)

screen = py.display.set_mode((size[0] * 128, size[1] * 128))
clock = py.time.Clock()

tiles = [Tile((1, 1), 'sprites//Tiles//stone//cobble.png'), Tile((1, 1), 'sprites//Tiles//stone//cobble.png'), Tile((1, 1), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((8, 8), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((1, 1), 'sprites//Tiles//stone//cobble.png'), Tile((2, 2), 'sprites//Tiles//stone//cobble.png'), Tile((3, 3), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((6, 6), 'sprites//Tiles//stone//cobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png'), Tile((3, 3), 'sprites//Tiles//stone//watercobble.png'), Tile((3, 3), 'sprites//Tiles//stone//watercobble.png'), Tile((6, 6), 'sprites//Tiles//stone//watercobble.png'), Tile((6, 6), 'sprites//Tiles//stone//watercobble.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((1, 1), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((8, 8), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((8, 8), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((8, 8), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((7, 7), 'sprites//Tiles//stone//cobble.png'), Tile((8, 8), 'sprites//Tiles//stone//cobble.png'), Tile((8, 8), 'sprites//Tiles//stone//cobble.png'), Tile((8, 8), 'sprites//Tiles//stone//cobble.png'), Tile((1, 1), 'sprites//Tiles//stone//cobble.png'), Tile((1, 1), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((8, 8), 'sprites//Tiles//dirt//dirt_ground_5.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_4.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_4.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_4.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_4.png'), Tile((1, 1), 'sprites//Tiles//dirt//dirt_ground_4.png'), Tile((1, 1), 'sprites//Tiles//dirt//dirt_ground_4.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((1, 1), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((0, 0), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((8, 8), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((8, 8), 'sprites//Tiles//dirt//dirt_ground_1.png'), Tile((9, 9), 'sprites//Tiles//dirt//dirt_ground_1.png')]

tilemap = Tilemap(size, tiles)
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