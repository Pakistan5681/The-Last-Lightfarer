import pygame as py
import time
from paxtons_helpers import Player, Tile, Tilemap, get_tile_mouse_pos, Projectile, MWeapon, Monster, proj_transition
from main_menu import menu
from helpers import is_adjacent
from death_screen import death
from health_bars import Phealth, PRbar, MPhealth, MPRbar

def main_game():
    py.init()
    
    size = (10, 10)

    run = menu()

    if run:
        screen = py.display.set_mode((size[0] * 128, size[1] * 128))
        player_bar = Phealth()
        Player_red_bar = PRbar(100)
        clock = py.time.Clock()

        tiles = [Tile((4, 0), 'sprites//Tiles//other//wotar.png', True), Tile((4, 1), 'sprites//Tiles//other//wotar.png', True), Tile((4, 2), 'sprites//Tiles//other//wotar.png', True), Tile((4, 3), 'sprites//Tiles//other//wotar.png', True), Tile((4, 4), 'sprites//Tiles//other//wotar.png', True), Tile((4, 5), 'sprites//Tiles//other//wotar.png', True), Tile((4, 6), 'sprites//Tiles//other//wotar.png', True), Tile((5, 6), 'sprites//Tiles//other//wotar.png', True), Tile((5, 7), 'sprites//Tiles//other//wotar.png', True), Tile((5, 8), 'sprites//Tiles//other//wotar.png', True), Tile((5, 9), 'sprites//Tiles//other//wotar.png', True), Tile((4, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 8), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 7), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 7), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 5), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 4), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 2), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((3, 0), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 0), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 2), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 4), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 5), 'sprites//Tiles//stone//watercobble.png', False), Tile((6, 5), 'sprites//Tiles//stone//watercobble.png', False), Tile((6, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((6, 7), 'sprites//Tiles//stone//watercobble.png', False), Tile((6, 8), 'sprites//Tiles//stone//watercobble.png', False), Tile((6, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((1, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 6), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 6), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 6), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 6), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 1), 'sprites//Tiles//stone//cobble.png', False), Tile((6, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 9), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 7), 'sprites//Tiles//dirt//dirt_ground_5.png', False), Tile((2, 0), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((6, 2), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((7, 8), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((3, 9), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((7, 6), 'sprites//Tiles//dirt//dirt_ground_2.png', False), Tile((6, 1), 'sprites//Tiles//dirt//dirt_ground_2.png', False)]

        tilemap = Tilemap(size, tiles)
        player = Player()

        monsters = [Monster("sprites\Frost Strider/frost strider-completed, no vfx-1.png.png",100, (3, 3), MWeapon("Generic Ah Weapon", 5, "rook", 2),25,"sprites/Player Attacks/fireball_01.png"),Monster("sprites/flame hop/flame hopper v1-1.png.png",100, (3, 4), MWeapon("Generic Ah Weapon", 5, "knight", 2),25,"sprites/Player Attacks/fireball_01.png"),Monster("sprites\sylf\sylphwing-right-facing.png.png",100, (4, 3), MWeapon("Generic Ah Weapon", 5, "bishop", 2),25,"sprites/Player Attacks/fireball_01.png")]
        running = True
        
        attackSquares = []
        moveSquares = []
        active_projectiles = []  # fix-ed list to hold live projectiles so they can be drawn 

        currentTurn = "playerAttack" # A variable that decides what actions can take place (i.e. playerAttack means it is the players attack phase)
    else: 
        running = False

    while running:
        
        screen.fill((0, 0, 255))
        clock.tick(60)

        tilemap.draw(screen)
        player.place(screen)
        for i in monsters:
            monster_bar = MPhealth(i.location)
            monster_red_bar = MPRbar(i.health,i.location)
            monster_red_bar.draw(screen, i.health)
            monster_bar.draw(screen)
        Player_red_bar.draw(screen, player.health)
        player_bar.draw(screen)

        monsterPos = []

        for i in monsters: 
            i.place(screen)
            monsterPos.append(i.location)

        if currentTurn == "playerAttack":
            if not attackSquares : attackSquares = player.attack(size, tiles)
            for i in attackSquares: i.place(screen)
        elif currentTurn == "playerMove":
            if not moveSquares: moveSquares = player.move(monsterPos, tiles)
            for i in moveSquares: i.place(screen)
        else:
            # fix-ed pass monsterPos as occupied so monsters don't stack on each other or the player
            occupied = monsterPos + [player.location]
            for t in tiles: 
                if t.isWall: occupied.append(t.location)

            for i in monsters:
                result= i.move(player.location, size, occupied)

                if isinstance(result, Projectile):                 # fix-ed store projectile if one was returned
                    active_projectiles.append(result)
                  # fix-ed capture return value
                if is_adjacent(player.location,i.location) == True and i.weapon.type != "bishop":
                    proj_transition(active_projectiles, screen, player, monsters, tilemap)
                    player.health -= i.damage
                    if player.health <= 0:
                        return death()
                if i.fight == True:
                    proj_transition(active_projectiles, screen, player, monsters, tilemap)
                    i.fight = False
                    player.health -= i.damage
                    if player.health <= 0:                        
                        return death()
                
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
                            active_projectiles.append(Projectile("sprites//Player Attacks//fireball_01.png", player.location, get_tile_mouse_pos(), 10, 20))
                            attackSquares = []
                            proj_transition(active_projectiles, screen, player, monsters, tilemap)
                            for i in monsters:
                                if i.location == get_tile_mouse_pos():                                    
                                    i.health -= player.weapon.damage
                                    if i.health <= 0:
                                        monsters.remove(i)                          
                            currentTurn = "monsterMove"
                            break
                    elif currentTurn == "playerMove":
                        locations = []
                        for i in moveSquares: locations.append(i.location)

                        if get_tile_mouse_pos() in locations:
                            moveSquares = []
                            player.location = get_tile_mouse_pos()
                            proj_transition(active_projectiles, screen, player, monsters, tilemap)
                            currentTurn = "playerAttack"

        py.display.flip()

cont = True
while cont:
    cont = main_game()