from paxtons_helpers import Player, Tile, Tilemap, get_tile_mouse_pos, Projectile, MWeapon, Monster, proj_transition, Level
import pygame as py

class Popup():
    def __init__(self, text, buttons):
        self.text = text
        self.image = py.surface(())
        self.buttons = buttons
        for i in self.buttons: i.popup = self

    def draw():


class PopupButton():
    def __init__(self, text, location):
        self.popup = None
        self.text = text
        self.location = location
        self.image = py.transform.scale(py.image.load("sprites//GUI//button.png").convert_alpha(), (525 / 2, 256 / 2))
        self.rect = self.image.get_rect(topleft=(location))
        self.font = py.font.Font("Fonts//Felipa-Regular.ttf", 38)
        self.words = self.font.render(text, True, (0, 0, 0))
        self.wordRect = self.words.get_rect(topleft=(location[0] + 100, location[1] + 35))

    def draw(self, screen):
        tint = self.image.copy()

        mousepos = py.mouse.get_pos()
        mouse_buttons = py.mouse.get_pressed()

        if self.rect.collidepoint(mousepos):
            tint.fill((200, 200, 200), special_flags=py.BLEND_RGBA_MULT)

            if mouse_buttons[0]:
                return True
            
        screen.blit(tint, self.rect)
        screen.blit(self.words, self.wordRect)
            
        
def tutorial():
    py.init()
    screen = py.display.set_mode((1280, 1280))
    level = [Tile((2, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 9), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 6), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 7), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((0, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((1, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((2, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((4, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 5), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 3), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((4, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 4), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 5), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 7), 'sprites//Tiles//stone//cobble.png', False), Tile((5, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((7, 9), 'sprites//Tiles//other//wotar.png', True), Tile((7, 8), 'sprites//Tiles//other//wotar.png', True), Tile((7, 7), 'sprites//Tiles//other//wotar.png', True), Tile((7, 6), 'sprites//Tiles//other//wotar.png', True), Tile((8, 6), 'sprites//Tiles//other//wotar.png', True), Tile((9, 6), 'sprites//Tiles//other//wotar.png', True), Tile((9, 5), 'sprites//Tiles//other//wotar.png', True), Tile((9, 4), 'sprites//Tiles//other//wotar.png', True), Tile((9, 3), 'sprites//Tiles//other//wotar.png', True), Tile((8, 3), 'sprites//Tiles//other//wotar.png', True), Tile((7, 3), 'sprites//Tiles//other//wotar.png', True), Tile((7, 2), 'sprites//Tiles//other//wotar.png', True), Tile((7, 1), 'sprites//Tiles//other//wotar.png', True), Tile((8, 1), 'sprites//Tiles//other//wotar.png', True), Tile((8, 0), 'sprites//Tiles//other//wotar.png', True), Tile((8, 7), 'sprites//Tiles//dirt//dirt_ground_1.png', False), Tile((9, 1), 'sprites//Tiles//dirt//dirt_ground_1.png', False), Tile((6, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 2), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((6, 1), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((9, 0), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((7, 4), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 5), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 8), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((8, 9), 'sprites//Tiles//dirt//dirt_ground_5.png', False), Tile((8, 2), 'sprites//Tiles//dirt//dirt_ground_5.png', False), Tile((8, 4), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((7, 0), 'sprites//Tiles//dirt//dirt_ground_4.png', False), Tile((4, 7), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 3), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 6), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 4), 'sprites//Tiles//stone//watercobble.png', False), Tile((5, 1), 'sprites//Tiles//stone//watercobble.png', False), Tile((4, 9), 'sprites//Tiles//stone//watercobble.png', False), Tile((0, 9), 'sprites//Tiles//other//bricks.png', True), Tile((1, 9), 'sprites//Tiles//other//bricks.png', True), Tile((1, 8), 'sprites//Tiles//other//bricks.png', True), Tile((0, 8), 'sprites//Tiles//other//bricks.png', True), Tile((0, 6), 'sprites//Tiles//other//bricks.png', True), Tile((1, 6), 'sprites//Tiles//other//bricks.png', True), Tile((1, 5), 'sprites//Tiles//other//bricks.png', True), Tile((0, 5), 'sprites//Tiles//other//bricks.png', True), Tile((1, 3), 'sprites//Tiles//other//bricks.png', True), Tile((0, 3), 'sprites//Tiles//other//bricks.png', True), Tile((0, 2), 'sprites//Tiles//other//bricks.png', True), Tile((1, 2), 'sprites//Tiles//other//bricks.png', True), Tile((1, 0), 'sprites//Tiles//other//bricks.png', True), Tile((0, 0), 'sprites//Tiles//other//bricks.png', True), Tile((3, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 6), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 8), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 3), 'sprites//Tiles//dirt//jungle_grass.png', False), Tile((3, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 2), 'sprites//Tiles//stone//cobble.png', False), Tile((3, 0), 'sprites//Tiles//stone//cobble.png', False), Tile((2, 0), 'sprites//Tiles//stone//cobble.png', False)]
    player = Player()
    tilemap = Tilemap((10, 10), level)
    player.location = (4, 9)

    button = PopupButton("Test", (300, 300))

    while True:
        screen.fill((0, 0, 0))

        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        
        tilemap.draw(screen)
        player.place(screen)
        button.draw(screen)

        py.display.flip()


tutorial()