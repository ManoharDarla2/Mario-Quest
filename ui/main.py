from pyglet.sprite import Sprite
from utils.resources import sky_img, ground_img


class Main:

    def __init__(self):
        self.sky = Sprite(sky_img)
        self.ground = Sprite(ground_img)

    def draw(self):
        self.sky.draw()
        self.ground.draw()

    def hide(self):
        self.sky.visible = False
        self.ground.visible = False

    def show(self):
        self.sky.visible = True
        self.ground.visible = True

    def get_ground_height(self):
        return self.ground.y + self.ground.height

    def get_ground(self):
        return self.ground

    def set_ground(self, x=None, y=None):
        self.ground.x = x if x is not None else self.ground.x
        self.ground.y = y if y is not None else self.ground.y
