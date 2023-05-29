from pyglet.sprite import Sprite
from utils.resources import menu


class MenuSprite(Sprite):

    """
    A Menu Sprite that shows before start of a game
    """
    
    def __init__(self):
        super().__init__(menu)
        self.position = 200, 150, 0
        self.original_opacity = self.opacity
        self.fade_duration = 0.5  # Duration of the fade effect in seconds
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

