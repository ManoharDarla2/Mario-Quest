import pyglet
from pyglet.sprite import Sprite
from pyglet.image import load
from utils.paths import MENU_PATH


class Menu:

    def __init__(self):
        background = load(f'{MENU_PATH}/title.png')
        start_img = load(f'{MENU_PATH}/start.png')
        self.title = Sprite(background)
        self.start_btn = Sprite(start_img)
        self.title.position = 149, 280, 0
        self.start_btn.position = 240, 200, 0
        self.start_btn.opacity = 255
        self.title.opacity = 255
        self.batch = pyglet.graphics.Batch()

    def draw(self):
        self.title.draw()
        self.start_btn.draw()

    def start(self, x, y):
        return self.start_btn.x <= x <= self.start_btn.x + self.start_btn.width \
        and self.start_btn.y <= y <= self.start_btn.y + self.start_btn.height

    def hide(self):
        self.title.visible = False
        self.start_btn.visible = False

    def show(self):
        self.title.visible = True
        self.start_btn.visible = True

    def fade(self):
        pass

