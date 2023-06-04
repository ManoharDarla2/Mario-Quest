import random
from pyglet.sprite import Sprite
from utils.resources import *
from utils.keys import *
from audio import *


class Base(Sprite):

    def __init__(self, img, x, y, batch):
        super().__init__(img, x=x, y=y, batch=batch)
        self.last_x = x

    def is_above(self, n, sprite):
        return self.x - (sprite.width // 2) <= sprite.x <= (self.x + self.width * n) - (sprite.width // 2) and \
            self.y + self.height <= sprite.y <= self.y + self.height + 10

    def is_below(self, n, sprite):
        return self.x - (sprite.width // 2) <= sprite.x <= (self.x + self.width * n) - (sprite.width // 2) and \
            self.y >= sprite.y + sprite.height

    def is_touched(self, sprite):
        return self.x + (self.width // 2) >= sprite.x >= self.x - (sprite.width // 2) and \
            sprite.y <= self.y + self.height and self.visible


class Ground(Base):

    def __init__(self, x, y, batch):
        super().__init__(ground_img, x, y, batch)
        self.speed = 200
        self.is_right = True
        self.is_moving = False

    def run(self, symbol):
        if symbol == RIGHT:
            self.is_moving = True

    def stop(self, symbol):
        if symbol == RIGHT:
            self.is_moving = True
        if symbol == SPACE:
            self.is_moving = True

    def move(self, dt):
        if self.is_moving:
            self.x -= self.speed * dt

    def attach(self, sprite, is_on_base):
        if is_on_base:
            sprite.y = self.y + self.height
        sprite.x = sprite.last_x + self.x


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

    def jump(self, dt):
        self.y += self.velocity_y * dt
        self.velocity_y -= 800 * dt
        if self.y < self.def_y:
            self.y = self.def_y
            self.velocity_y = 0

    def start(self, symbol):
        if symbol == SPACE and self.y <= self.def_y + 10:
            jump_sfx.play()
            self.velocity_y = 500

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

    def move(self, dt):
        if self.is_moving:
            if self.is_right:
                self.x += self.speed * dt
            else:
                self.x -= self.speed * dt

    def stop(self, symbol):
        if symbol == RIGHT or symbol == LEFT:
            self.image = stand(0.35)[0] if self.is_right else stand(0.35)[1]
            self.is_moving = False

    def is_dead(self, enemy):
        return enemy.x + (enemy.width // 2) >= self.x >= enemy.x - (self.width // 2) and \
                self.y <= enemy.y + enemy.height and enemy.visible


class Coins:

    def __init__(self, y, batch):
        self.y = y
        self.batch = batch
        self.coins = []

    def create(self, n, start, end):
        for _ in range(n):
            coin_x = random.randint(start, end)
            c = Base(coin_anim, x=coin_x, y=self.y, batch=self.batch)
            self.coins.append(c)
        return self.coins

    def collected(self, player, base):
        points = 0
        for c in self.coins:
            base.attach(c, True)
            if c.is_touched(player):
                coin_sfx.play()
                c.visible = False
                points = 1
        return points


class Bricks:

    def __init__(self, patterns, xs, ys, batch):
        self.ys = ys
        self.batch = batch
        self.brick_set = []
        self.bricks = []
        self.patterns = patterns
        self.xs = xs
        self.width = brick_img.width
        self.pos_x = []
        self.pos_width = []

    def create(self):
        for j, pattern in enumerate(self.patterns):
            brick_x = self.xs[j] + brick_img.width
            for i, _ in enumerate(pattern):
                b = Base(brick_img, x=brick_x, y=self.ys[j], batch=self.batch)
                brick_x += brick_img.width
                self.bricks.append(b)
                if i == len(pattern) - 1:
                    self.brick_set.append(self.bricks)
                    self.bricks = []
                self.pos_x.append(self.xs[j])
                self.pos_width.append(self.xs[j] * len(pattern))

    def set(self, ground, player):
        for bricks in self.brick_set:
            for brick in bricks:
                ground.attach(brick, False)
            if bricks[0].is_above(len(bricks), player):
                player.y = bricks[0].y + bricks[0].height
                player.velocity_y = 0


class Enemy:

    def __init__(self, xs, y, batch):
        self.enemies = []
        for x in xs:
            en = Base(brick_img, x, y, batch)
            self.enemies.append(en)

    def move(self, speed):
        for enemy in self.enemies:
            enemy.x -= speed

    def get(self):
        return self.enemies
