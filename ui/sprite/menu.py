import pyglet
from pyglet.sprite import Sprite
from pyglet.image import load
from utils.paths import MENU_PATH

class MenuSprite(Sprite):
    
    def __init__(self):
        menu = load(f'{MENU_PATH}/menu.png')
        super().__init__(menu)
        self.position = 200, 150, 0
        self.original_opacity = self.opacity
        self.fade_duration = 0.5  # Duration of the fade effect in seconds
        self.fade_elapsed = 0.0
        self.fading = False

    def is_clicked(self, x, y):
        return self.x + 95 <= x <= self.y + 330 and self.y + 20 <= y <= self.y + 55

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

