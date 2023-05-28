import pyglet
from pyglet.window import Window, mouse
from pyglet.sprite import Sprite
from pyglet.image import load
from utils.paths import MENU_PATH


class Menu(Window):

    def __init__(self):
        super().__init__(800,600)
        background = load(f'{MENU_PATH}/menu_bg.png')
        start_img = load(f'{MENU_PATH}/start.png')
        self.bg_sprite = Sprite(background)
        self.start_btn = Sprite(start_img)
        self.start_btn.position = 240, 200, 0

    def on_draw(self):
        self.clear()
        self.bg_sprite.draw()
        self.start_btn.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.start_btn.x <= x <= self.start_btn.x + self.start_btn.width \
                    and self.start_btn.y <= y <= self.start_btn.y + self.start_btn.height:
                print("test clicked")
                self.close()


if __name__ == '__main__':
    window = Menu()
    pyglet.app.run()
