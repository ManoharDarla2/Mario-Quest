from pyglet.sprite import Sprite
from pyglet.image import load
from utils.paths import MAIN_PATH

class Main:

    def __init__(self):
        sky_img = load(f'{MAIN_PATH}/sky.png')
        ground_img = load(f'{MAIN_PATH}/ground.png')
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

