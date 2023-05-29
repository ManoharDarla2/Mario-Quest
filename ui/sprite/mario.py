from pyglet.sprite import Sprite
from utils.resources import run,stand
from utils.keys import *

s_duration = 0.35


class Mario(Sprite):

    def __init__(self, x, y):
        super().__init__(stand(s_duration)[0])
        self.position = x, y, 0
        self.scale = 0.45
        self.speed = 150
        self.duration = 0.065
        self.is_right = True
        self.is_moving = False

    def animation(self, symbol):
        self._move(symbol)

    def move(self, dt):
        if self.is_moving:
            if self.is_right:
                self.x += self.speed * dt
            else:
                self.x -= self.speed * dt

    def animation_end(self, symbol):
        if symbol == RIGHT or symbol == LEFT:
            self.image = stand(s_duration)[0] if self.is_right else stand(s_duration)[1]
        self.is_moving = False

    def _move(self, symbol):
        self.move_factor = 0
        if symbol == RIGHT:
            if self.image != run(self.duration)[0]:
                self.image = run(self.duration)[0]
            self.is_right = True
            self.is_moving = True

        if symbol == LEFT:
            if self.image != run(self.duration)[1]:
                self.image = run(self.duration)[1]
            self.is_right = False
            self.is_moving = True
