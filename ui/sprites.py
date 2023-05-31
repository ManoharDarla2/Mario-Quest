import pyglet
import random
from pyglet.sprite import Sprite
from pyglet.graphics import Batch
from utils.resources import *
from utils.keys import *


class Ground(Sprite):

    def __init__(self, x, y, batch):
        super().__init__(ground_img, x, y, 0, batch=batch)
        self.speed = 200
        self.is_right = True
        self.is_moving = False

    def run(self, symbol):
        self._move(symbol)

    def stop(self, symbol):
        self.is_moving = False

    def move(self, dt):
        if self.is_moving:
            self.x -= self.speed * dt

    def _move(self, symbol):
        if symbol == RIGHT:
            self.is_moving = True

    def on_motion(self):
        return self.is_moving

    def attach(self, sprite):
        sprite.y = self.height
        sprite.x = self.x

    def attach_coin(self, c):
        c.y = self.height
        c.x = c.last_x + self.x



class Menu(Sprite):

    def __init__(self, x, y, batch):
        super().__init__(menu, x=x, y=y, batch=batch)
        self.original_opacity = self.opacity
        self.fade_duration = 0.5
        self.fade_elapsed = 0.0
        self.fading = False

    def is_clicked(self, x, y):
        return self.x + 95 <= x <= self.y + 380 and self.y + 20 <= y <= self.y + 55

    def fade(self):
        self.fading = True
        self.fade_elapsed = 0.0

    def fade_update(self, dt):
        if self.fading:
            self.fade_elapsed += dt
            if self.fade_elapsed >= self.fade_duration:
                self.opacity = 0
                self.fading = False
                self.visible = False
            else:
                self.opacity = int((1 - (self.fade_elapsed / self.fade_duration)) * self.original_opacity)


class Mario(Sprite):

    def __init__(self, x, y, batch):
        super().__init__(stand(0.35)[0], x=x, y=y, batch=batch)
        self.def_y = y
        self.velocity_y = 0
        self.gravity = -600
        self.time_elapsed = 0
        self.scale = 0.45
        self.speed = 200
        self.duration = 0.06
        self.is_right = True
        self.is_moving = False

    def on_jump(self, dt):
        self.y += self.velocity_y * dt
        self.velocity_y -= 500 * dt
        if self.y < self.def_y:
            self.y = self.def_y
            self.velocity_y = 0

    def animation(self, symbol):
        if symbol == SPACE:
            self.velocity_y = 400
        self._move(symbol)

    def move(self, dt):
        if self.is_moving:
            if self.is_right:
                self.x += self.speed * dt
            else:
                self.x -= self.speed * dt

    def animation_end(self, symbol):
        if symbol == RIGHT or symbol == LEFT:
            self.image = stand(0.35)[0] if self.is_right else stand(0.35)[1]
        self.is_moving = False

    def _move(self, symbol):
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

class Coin(Sprite):

    def __init__(self, x, batch):
        super().__init__(coin_anim, batch=batch)
        self.last_x = x
