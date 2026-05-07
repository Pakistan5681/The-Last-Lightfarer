import pygame as py
import math
class Projectile:
    def __init__(self, spritePath, startpos, targetpos, speed, damage):       
        self.x = float(startpos[0] * 128)
        self.y = float(startpos[1] * 128)
        self.targetx = float(targetpos[0] * 128)
        self.targety = float(targetpos[1] * 128)
        self.speed = speed
        self.damage = damage
        self.alive = True
        angle = math.degrees(math.atan((self.targetx - startpos[0]) / (self.targety - startpos[1])))
        self.sprite = py.transform.rotate(py.transform.scale(py.image.load(spritePath).convert_alpha(),(400,400)), angle)

    def draw(self, screen, player):
        horizontal_distance = self.targetx - self.x
        vertical_distance = self.targety - self.y
        total_distance = math.sqrt(horizontal_distance**2 + vertical_distance**2)

        if total_distance <= self.speed:
            player.health -= self.damage
            self.alive = False
        else:
            self.x += (horizontal_distance / total_distance) * self.speed
            self.y += (vertical_distance / total_distance) * self.speed
            scaled_sprite = py.transform.scale(self.sprite, (128, 128))
            screen.blit(scaled_sprite, (self.x, self.y))