import random
from pyglet.sprite import Sprite
from utils.resources import *
from utils.keys import *
from audio import *


# Base Sprite Class for Game
class Base(Sprite):
    """
        Base Sprite class Required for frame movements w.r.t to their Positions
    """

    def __init__(self, img, x, y, batch):
        super().__init__(img, x=x, y=y, batch=batch)
        self.last_x = x  # Special Class variable used for frame movements

    def is_above(self, n, sprite):
        """
            Check whether the given sprite is above on the base sprite
        :param n: No of same sprite if they attached
        :param sprite: Sprite that required to check
        :return: True if given sprite is above else false
        """
        return self.x - (sprite.width // 2) <= sprite.x <= (self.x + self.width * n) - (sprite.width // 2) and \
            self.y + self.height <= sprite.y <= self.y + self.height + 10

    def is_below(self, n, sprite):
        """
            Check whether the given sprite is below on the base sprite
        :param n: No of same sprite if they attached
        :param sprite: Sprite that required to check
        :return: True if given sprite is below else false
        """
        return self.x - (sprite.width // 2) <= sprite.x <= (self.x + self.width * n) - (sprite.width // 2) and \
            self.y >= sprite.y + sprite.height

    def is_touched(self, sprite):
        """
            Check whether the given sprite is touched base sprite
        :param sprite: Given sprite that required to check
        :return: True if given sprite is touched else false
        """
        return self.x + (self.width // 2) >= sprite.x >= self.x - (sprite.width // 2) and \
            sprite.y <= self.y + self.height and self.visible


class Ground(Base):
    """
        Ground Sprite class inherited from Base Sprite Class.
        This has some special methods for movement of sprites in screen.
    """

    def __init__(self, x, y, batch):
        super().__init__(ground_img, x, y, batch)
        self.speed = 200
        self.is_right = True
        self.is_moving = False

    def run(self, symbol):
        """
            Required when key presses
        :param symbol: the argument required to get key state
        """
        if symbol == RIGHT:
            self.is_moving = True

    def stop(self, symbol):
        """
            Required when key realises
        :param symbol: the argument required to get key state
        """
        if symbol == RIGHT:
            self.is_moving = True
        if symbol == SPACE:
            self.is_moving = True

    def move(self, dt):
        """
            Required for movement in on update function
        :param dt: the argument required to get key state
        """
        if self.is_moving:
            self.x -= self.speed * dt

    def attach(self, sprite, is_on_base):
        """
            Attach sprite to the ground. This helps when the ground is moved
        :param sprite: Sprite that need to be attached
        :param is_on_base: Whether the sprite need to be above the ground
        """
        if is_on_base:
            sprite.y = self.y + self.height
        sprite.x = sprite.last_x + self.x


class Menu(Sprite):
    """
        Simple Menu Sprite for with click method
    """

    def __init__(self, x, y):
        super().__init__(menu, x=x, y=y)

    def is_clicked(self, x, y):
        return self.x + 95 <= x <= self.y + 380 and self.y + 20 <= y <= self.y + 55


class Mario(Sprite):
    """
        Main Player Sprite with jump and movement methods
    """

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
        """
            jumps when the velocity is given
        :param dt: update argument
        """
        self.y += self.velocity_y * dt
        self.velocity_y -= 800 * dt
        if self.y < self.def_y:
            self.y = self.def_y
            self.velocity_y = 0

    def start(self, symbol):
        """
            The method that start animation and movements when specific key is pressed
        :param symbol: argument required to get key state
        """
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
        """
            Method to move the mario left and right
        :param dt: Update argument
        """
        if self.is_moving:
            if self.is_right:
                self.x += self.speed * dt
            else:
                self.x -= self.speed * dt

    def stop(self, symbol):
        """
            The method that stops animation and movements when specific key is pressed
        :param symbol: argument required to get key state
        """
        if symbol == RIGHT or symbol == LEFT:
            self.image = stand(0.35)[0] if self.is_right else stand(0.35)[1]
            self.is_moving = False

    def is_dead(self, enemy):
        """
            The method checks whether the player is dead
        :param enemy: the enemy sprite
        :return: True if he touches the enemy
        """
        return enemy.x + (enemy.width // 2) >= self.x >= enemy.x - (self.width // 2) and \
            self.y <= enemy.y + enemy.height and enemy.visible


class Coins:
    """
        Coins class that create coin sprites with range and use random to create in the given range
    """

    def __init__(self, y, batch):
        self.y = y
        self.batch = batch
        self.coins = []

    def create(self, n, start, end):
        """
            The Main method to create coins
        :param n: No of coins
        :param start: starting of coins
        :param end: ending of coins
        """
        for _ in range(n):
            coin_x = random.randint(start, end)
            c = Base(coin_anim, x=coin_x, y=self.y, batch=self.batch)
            self.coins.append(c)
        return self.coins

    def collected(self, player, base):
        """
            checks when coin is collected by player and plays sfx on collecting
        :param player: The player Sprite
        :param base: required to attach the coin to ground
        :return: points when coins collected
        """
        points = 0
        for c in self.coins:
            base.attach(c, True)
            if c.is_touched(player):
                coin_sfx.play()
                c.visible = False
                points = 1
        return points


class Bricks:
    """
        Bricks class that creates the bricks with pattern and x positions
    """

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
    """
        Enemy class that create enemies at xs positions
    """

    def __init__(self, xs, y, batch):
        self.enemies = []
        for x in xs:
            en = Base(enemy_anim, x, y, batch)
            self.enemies.append(en)

    def move(self, speed):
        for enemy in self.enemies:
            enemy.x -= speed

    def get(self):
        return self.enemies
