from paxtons_helpers import Player, Tile, Tilemap, get_tile_mouse_pos, Weapon, Monster, MWeapon, Projectile, proj_transition
from health_bars import Phealth, PRbar, MPhealth, MPRbar
from GUI import Popup, PopupButton
from helpers import is_adjacent
from death_screen import death
from random import choice
import pygame as py
import textwrap

# good code innit?


            
        
def tutorial():
    def generic_popup(popup, player, tilemap, running):
        active = True
        while running and active:
            screen.fill((0, 0, 0))

            clicking = False
            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                    clicking = True

            tilemap.draw(screen)
            player.place(screen)      
            active = popup.draw(screen, clicking)     

            py.display.flip()

        return running


    py.init()
    screen = py.display.set_mode((1280, 1280))
    level = [Tile((2, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 6), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((4, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 5), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 3), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 5), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 9), 'sprites//Tiles//other//wotar.png', True), Tile((7, 8), 'sprites//Tiles//other//wotar.png', True), Tile((7, 7), 'sprites//Tiles//other//wotar.png', True), Tile((7, 6), 'sprites//Tiles//other//wotar.png', True), Tile((8, 6), 'sprites//Tiles//other//wotar.png', True), Tile((9, 6), 'sprites//Tiles//other//wotar.png', True), Tile((9, 5), 'sprites//Tiles//other//wotar.png', True), Tile((9, 4), 'sprites//Tiles//other//wotar.png', True), Tile((9, 3), 'sprites//Tiles//other//wotar.png', True), Tile((8, 3), 'sprites//Tiles//other//wotar.png', True), Tile((7, 3), 'sprites//Tiles//other//wotar.png', True), Tile((7, 2), 'sprites//Tiles//other//wotar.png', True), Tile((7, 1), 'sprites//Tiles//other//wotar.png', True), Tile((8, 1), 'sprites//Tiles//other//wotar.png', True), Tile((8, 0), 'sprites//Tiles//other//wotar.png', True), Tile((8, 7), 'sprites//Tiles//dirt//dirt_ground_1.png', False), Tile((9, 1), 'sprites//Tiles//dirt//dirt_ground_1.png', False), Tile((6, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 9), 'sprites//Tiles//dirt//dirt_ground_5.png', False), Tile((8, 2), 'sprites//Tiles//dirt//dirt_ground_5.png', False), Tile((8, 4), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((7, 0), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((4, 7), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((0, 9), 'sprites//Tiles//other//bricks.png', True), Tile((1, 9), 'sprites//Tiles//other//bricks.png', True), Tile((1, 8), 'sprites//Tiles//other//bricks.png', True), Tile((0, 8), 'sprites//Tiles//other//bricks.png', True), Tile((0, 6), 'sprites//Tiles//other//bricks.png', True), Tile((1, 6), 'sprites//Tiles//other//bricks.png', True), Tile((1, 5), 'sprites//Tiles//other//bricks.png', True), Tile((0, 5), 'sprites//Tiles//other//bricks.png', True), Tile((1, 3), 'sprites//Tiles//other//bricks.png', True), Tile((0, 3), 'sprites//Tiles//other//bricks.png', True), Tile((0, 2), 'sprites//Tiles//other//bricks.png', True), Tile((1, 2), 'sprites//Tiles//other//bricks.png', True), Tile((1, 0), 'sprites//Tiles//other//bricks.png', True), Tile((0, 0), 'sprites//Tiles//other//bricks.png', True), Tile((3, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 0), 'sprites//Tiles//stone//cobble.png', False)]
    player = Player()
    player.weapon = Weapon("Lance", 25, "marksman", 1)
    player.speed = 5
    tilemap = Tilemap((10, 10), level)
    player.location = (4, 7) # Pos should be (4, 9)
    player_bar = Phealth()
    Player_red_bar = PRbar(100)

    popup = Popup("Some good words would go here. Backstory and the like. This part isn't important to the game in any way, shape, or form.", (8, 0, 36), [PopupButton("Next", (515, 775))]) 

    running = True
    running = generic_popup(popup, player, tilemap, running)

    popup = Popup("Likely more backstory. 'Youre the last lightfarer and must save the world' typa deal.", (8, 0, 36), [PopupButton("Next", (515, 775))]) 
    running = generic_popup(popup, player, tilemap, running)

    popup = Popup("You will see orange circles on your screen. They indicate where you can move. You can't move to water or building tiles. Click an orange circle.", (8, 0, 36), [PopupButton("Next", (515, 775))]) 
    running = generic_popup(popup, player, tilemap, running)

    active = True
    while running and active:
        screen.fill((0, 0, 0))

        tilemap.draw(screen)
        player.place(screen)  

        moveSquares = player.move([], level)
        for i in moveSquares: i.place(screen)

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                locations = []
                for i in moveSquares: locations.append(i.location)
                if get_tile_mouse_pos() in locations:
                    player.location = get_tile_mouse_pos()
                    active = False

        py.display.flip()

    active = True
    popup = Popup("You are under attack! The red squares indicate where you can attack! Hit the monster!", (8, 0, 36), [PopupButton("Next", (515, 775))]) 
    running = generic_popup(popup, player, tilemap, running)

    active = True
    attackSquares = player.attack((10, 10), level)
    spawn = choice(attackSquares).location
    new = Monster("sprites//flame hop//flame hopper v1-1.png.png", 50, spawn, MWeapon("Does it matter?", 10, "pawn", 1), 10, "sprites//Player Attacks//fireball_01.png")
    monsters = [new] 
    active_projectiles = []

    while running and active:
        screen.fill((0, 0, 0))

        tilemap.draw(screen)
        player.place(screen)  
        for i in monsters: i.place(screen)

        for i in monsters:
            monster_bar = MPhealth(i.location)
            monster_red_bar = MPRbar(i.health,i.location)
            monster_red_bar.draw(screen, i.health)
            monster_bar.draw(screen)
        Player_red_bar.draw(screen, player.health)
        player_bar.draw(screen)

        for i in attackSquares: i.place(screen)

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
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

                    active = False
        py.display.flip()

    occupied = [player.location]
    for t in level: 
        if t.isWall: occupied.append(t.location)

    for i in monsters:
        result= i.move(player.location, (10, 10), occupied)

        if isinstance(result, Projectile):                 # fix-ed store projectile if one was returned
            active_projectiles.append(result)
          # fix-ed capture return value
        if is_adjacent(player.location,i.location) == True and i.weapon.type != "bishop":
            proj_transition(active_projectiles, screen, player, monsters, tilemap)
            player.health -= i.damage
            if player.health <= 0:
                running = False
                quit()
        if i.fight == True:
            proj_transition(active_projectiles, screen, player, monsters, tilemap)
            i.fight = False
            player.health -= i.damage
            if player.health <= 0:                        
                return death()
    
    active = True
    popup = Popup("You didn't quite finish off the monster, and it fought back. Position yourself to hit it, and deal the finishing blow!", (8, 0, 36), [PopupButton("Next", (515, 775))]) 
    running = generic_popup(popup, player, tilemap, running)

    while monsters and running:
        active = True
        while running and active:
            screen.fill((0, 0, 0))

            tilemap.draw(screen)
            player.place(screen)  

            for i in monsters: i.place(screen)

            for i in monsters:
                monster_bar = MPhealth(i.location)
                monster_red_bar = MPRbar(i.health,i.location)
                monster_red_bar.draw(screen, i.health)
                monster_bar.draw(screen)
            Player_red_bar.draw(screen, player.health)
            player_bar.draw(screen)

            moveSquares = player.move([], level)
            for i in moveSquares: i.place(screen)

            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                    locations = []
                    for i in moveSquares: locations.append(i.location)
                    if get_tile_mouse_pos() in locations:
                        player.location = get_tile_mouse_pos()
                        active = False

            py.display.flip()

        active = True

        attackSquares = player.attack((10, 10), level)

        while running and active:
            screen.fill((0, 0, 0))

            tilemap.draw(screen)
            player.place(screen)  
            for i in monsters: i.place(screen)

            for i in monsters:
                monster_bar = MPhealth(i.location)
                monster_red_bar = MPRbar(i.health,i.location)
                monster_red_bar.draw(screen, i.health)
                monster_bar.draw(screen)
            Player_red_bar.draw(screen, player.health)
            player_bar.draw(screen)

            for i in attackSquares: i.place(screen)

            for event in py.event.get():
                if event.type == py.QUIT:
                    running = False
                elif event.type == py.MOUSEBUTTONDOWN and event.button == 1:
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

                        active = False

            py.display.flip()

        occupied = [player.location]
        for t in level: 
            if t.isWall: occupied.append(t.location)

        for i in monsters:
            result= i.move(player.location, (10, 10), occupied)

            if isinstance(result, Projectile):                 # fix-ed store projectile if one was returned
                active_projectiles.append(result)
              # fix-ed capture return value
            if is_adjacent(player.location,i.location) == True and i.weapon.type != "bishop":
                proj_transition(active_projectiles, screen, player, monsters, tilemap)
                player.health -= i.damage
                if player.health <= 0:
                    running = False
                    quit()
            if i.fight == True:
                proj_transition(active_projectiles, screen, player, monsters, tilemap)
                i.fight = False
                player.health -= i.damage
                if player.health <= 0:                        
                    return death()
        
    active = True
    popup = Popup("You did it screen. 'Go and save the world' or something cornballish like that", (8, 0, 36), [PopupButton("Next", (515, 775))]) 
    running = generic_popup(popup, player, tilemap, running)