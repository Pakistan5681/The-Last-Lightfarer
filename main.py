import pygame as py
from paxtons_helpers import Player, Tile, Tilemap, get_tile_mouse_pos
from Jacob.spheudocode import MWeapon, Monster
from Jacob.proj import Projectile

py.init()

size = (10, 10)

screen = py.display.set_mode((size[0] * 128, size[1] * 128))
clock = py.time.Clock()

tiles = [Tile((4, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 1), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 1), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 1), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 1), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 3), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 3), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 5), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 5), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((1, 8), 'sprites//Tiles//other//bricks.png', True), Tile((8, 7), 'sprites//Tiles//other//bricks.png', True), Tile((4, 4), 'sprites//Tiles//other//bricks.png', True), Tile((7, 3), 'sprites//Tiles//other//bricks.png', True), Tile((5, 6), 'sprites//Tiles//other//bricks.png', True), Tile((3, 5), 'sprites//Tiles//other//bricks.png', True), Tile((1, 2), 'sprites//Tiles//other//bricks.png', True), Tile((4, 1), 'sprites//Tiles//other//bricks.png', True), Tile((8, 1), 'sprites//Tiles//other//bricks.png', True), Tile((9, 4), 'sprites//Tiles//other//bricks.png', True), Tile((6, 9), 'sprites//Tiles//other//bricks.png', True), Tile((3, 8), 'sprites//Tiles//other//bricks.png', True), Tile((0, 9), 'sprites//Tiles//other//bricks.png', True), Tile((0, 6), 'sprites//Tiles//other//bricks.png', True), Tile((1, 4), 'sprites//Tiles//other//bricks.png', True), Tile((6, 2), 'sprites//Tiles//other//bricks.png', True), Tile((2, 0), 'sprites//Tiles//other//bricks.png', True), Tile((9, 9), 'sprites//Tiles//other//bricks.png', True), Tile((7, 5), 'sprites//Tiles//other//bricks.png', True), Tile((4, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 8), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 7), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 5), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 4), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 2), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 0), 'sprites//Tiles//stone//watercobble.png', False), Tile((8, 8), 'sprites//Tiles//other//grass.png', False), Tile((9, 8), 'sprites//Tiles//other//grass.png', False), Tile((9, 7), 'sprites//Tiles//other//grass.png', False), Tile((8, 6), 'sprites//Tiles//other//grass.png', False), Tile((9, 5), 'sprites//Tiles//other//grass.png', False), Tile((8, 5), 'sprites//Tiles//other//grass.png', False), Tile((8, 3), 'sprites//Tiles//other//grass.png', False), Tile((9, 3), 'sprites//Tiles//other//grass.png', False), Tile((9, 2), 'sprites//Tiles//other//grass.png', False), Tile((9, 1), 'sprites//Tiles//other//grass.png', False), Tile((0, 8), 'sprites//Tiles//other//grass.png', False), Tile((0, 7), 'sprites//Tiles//other//grass.png', False), Tile((1, 6), 'sprites//Tiles//other//grass.png', False), Tile((1, 5), 'sprites//Tiles//other//grass.png', False), Tile((0, 5), 'sprites//Tiles//other//grass.png', False), Tile((0, 3), 'sprites//Tiles//other//grass.png', False), Tile((0, 2), 'sprites//Tiles//other//grass.png', False), Tile((1, 0), 'sprites//Tiles//other//grass.png', False), Tile((0, 0), 'sprites//Tiles//other//grass.png', False), Tile((8, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((8, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((8, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((8, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((9, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((9, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((1, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((0, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((1, 1), 'sprites//Tiles//stone//cobble.png', False), Tile((1, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((1, 3), 'sprites//Tiles//stone//cobble.png', False), Tile((0, 1), 'sprites//Tiles//stone//cobble.png', False)]

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
        if attackSquares == None : attackSquares = player.attack(size, tiles)
        for i in attackSquares: i.place(screen)
    elif currentTurn == "playerMove":
        if moveSquares == None: moveSquares = player.move(monsterPos, tiles)
        for i in moveSquares: i.place(screen)
    else:
        # fix-ed pass monsterPos as occupied so monsters don't stack on each other or the player
        occupied = monsterPos + [player.location]
        for t in tiles: 
            if t.isWall: occupied.append(t.location)

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