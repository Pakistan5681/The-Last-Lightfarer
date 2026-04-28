import paxtons_helpers as ph
import pygame as py

tiles = {
    1: "sprites\Tiles\dirt\dirt_ground_1.png",
    2: "sprites\Tiles\dirt\dirt_ground_2.png",
    3: "sprites\Tiles\dirt\dirt_ground_3.png",
    4: "sprites\Tiles\dirt\dirt_ground_4.png",
    5: "sprites\Tiles\dirt\dirt_ground_5.png",
    6: "sprites\Tiles\stone\cobble.png",
    7: "sprites\Tiles\stone\watercobble.png"
}

tiles = []

for x in range(10):
    for y in range(10):
        tiles.append(ph.Tile((x, y), "sprites\Tiles\dirt\dirt_ground_1.png"))

tilemap = ph.Tilemap((10, 10))

max = 7

scrollPause = False
scollDelay = 10
scrollClock = 0
current = 1
while True:
    for event in py.event.get():
        if event == py.MOUSEBUTTONDOWN:

