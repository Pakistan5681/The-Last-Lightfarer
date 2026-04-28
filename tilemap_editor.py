import paxtons_helpers as ph
import pygame as py

py.init()

screen = py.display.set_mode(1280, 1280)
clock = py.time.Clock()

drawTiles = {
    1: "sprites//Tiles//dirt//dirt_ground_1.png",
    2: "sprites//Tiles//dirt//dirt_ground_2.png",
    3: "sprites//Tiles//dirt//dirt_ground_3.png",
    4: "sprites//Tiles//dirt//dirt_ground_4.png",
    5: "sprites//Tiles//dirt//dirt_ground_5.png",
    6: "sprites//Tiles//stone//cobble.png",
    7: "sprites//Tiles//stone//watercobble.png"
}

tiles = []

for x in range(10):
    for y in range(10):
        tiles.append(ph.Tile((x, y), "sprites//Tiles//dirt//dirt_ground_1.png"))

max = 7

scrollPause = False
scrollDelay = 10
scrollClock = 0
current = 1

def export(tiles):
    outString = "["
    for i in tiles:
        outString += f"Tile(({i.location[0]}, {i.location[0]}), {i.spritePath}), "
    outString += "]"

    return outString

while True:

    mousepos = ph.get_tile_mouse_pos()

    for event in py.event.get():
        if event == py.MOUSEBUTTONDOWN:
            if not scrollPause:
                if event.button == 4:
                    if current != max: current += 1
                    scrollPause = True
                elif event.button == 5:
                    if current != 1: current -= 1
                    scrollPause = True
        elif event == py.KEYDOWN:
            if event.key == py.K_e:
                print(export())


    if scrollPause:
        scrollClock += 1
        if scrollClock >= scrollDelay:
            scrollClock = 0
            scrollPause = False

    tile = drawTiles[current]

    for t in tiles:
        if t.location == mousepos:
            tiles.remove(t)
            tiles.append(ph.Tile(mousepos, tile))
            break

    tilemap = ph.Tilemap((10, 10), tiles)
    tilemap.draw()