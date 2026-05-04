import paxtons_helpers as ph
import pygame as py
import json

py.init()

screen = py.display.set_mode((1280, 1280))
clock = py.time.Clock()

drawTiles = {
    1: "sprites//Tiles//dirt//dirt_ground_1.png",
    2: "sprites//Tiles//dirt//dirt_ground_2.png",
    3: "sprites//Tiles//dirt//dirt_ground_3.png",
    4: "sprites//Tiles//dirt//dirt_ground_4.png",
    5: "sprites//Tiles//dirt//dirt_ground_5.png",
    6: "sprites//Tiles//stone//cobble.png",
    7: "sprites//Tiles//stone//watercobble.png",
    8: "sprites//Tiles//other//bricks.png",
    9: "sprites//Tiles//other//grass.png"
}

wallTiles ={
    "place" : "sprites//Tiles//editor//Add Wall.png",
    "delete" : "sprites//Tiles//editor//Add Wall.png"
}

tiles = []
walls = []

for x in range(10):
    for y in range(10):
        tiles.append(ph.Tile((x, y), "sprites//Tiles//dirt//dirt_ground_1.png", False))

max = 9

scrollPause = False
scrollDelay = 10
scrollClock = 0
current = 1
wallCurrent = "place"

mode = "tiles"

def export(tiles, walls):
    with open("tme_out.json", "w") as file:
        outString = "["
        for i in tiles:
            outString += f"Tile(({i.location[0]}, {i.location[1]}), '{i.spritePath}', {getIsWall((i.location[0], i.location[1]), walls)}), "
        outString += "]"

        json.dump(outString, file)

def getIsWall(pos, walls):

    for i in walls:
        if i.location == pos:
            return True
    
    return False

while True:
    screen.fill((0, 0, 0))
    if mode == "tiles":
        screen.fill((0, 0, 0))
        clock.tick(60)
        mousepos = ph.get_tile_mouse_pos()

        tilemap = ph.Tilemap((10, 10), tiles)
        tilemap.draw(screen)
        tile = drawTiles[current]

        ph.Tile(mousepos, tile, False).place(screen)

        for event in py.event.get():
            if event.type == py.MOUSEBUTTONDOWN:
                if not scrollPause:
                    if event.button == 4:
                        if current != max: current += 1
                        scrollPause = True
                    elif event.button == 5:
                        if current != 1: current -= 1
                        scrollPause = True                
            elif event.type == py.KEYDOWN:
                if event.key == py.K_e:
                    export(tiles)
                elif event.key == py.K_w:
                    mode = "walls"

        mousebuttons = py.mouse.get_pressed()

        if mousebuttons[0]:
            for t in tiles:
                if t.location == mousepos:
                    tiles.remove(t)
                    tiles.append(ph.Tile(mousepos, tile, False))
                    break

        if scrollPause:
            scrollClock += 1
            if scrollClock >= scrollDelay:
                scrollClock = 0
                scrollPause = False

        py.display.flip()
    else:
        screen.fill((0, 0, 0))
        clock.tick(60)
        mousepos = ph.get_tile_mouse_pos()

        tilemap = ph.Tilemap((10, 10), tiles)
        wallsMap = ph.Tilemap((10, 10), walls)
        tilemap.draw(screen)
        wallsMap.draw(screen)
        tile = wallTiles[wallCurrent]
        ph.Tile(mousepos, tile, False).place(screen)

        mousebuttons = py.mouse.get_pressed()

        if mousebuttons[0]:
            if wallCurrent == "place":
                # only place if empty
                for t in walls:
                    if t.location == mousepos:
                        break
                else:
                    walls.append(ph.Tile(mousepos, tile, False))

            else:  # delete
                for t in walls:
                    if t.location == mousepos:
                        walls.remove(t)
                        break
        
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_p:
                    wallCurrent = "place"
                elif event.key == py.K_d:
                    wallCurrent = "delete"
                elif event.key == py.K_t:
                    mode = "tiles"
        
        py.display.flip()