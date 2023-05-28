import pyglet
from pyglet.window import Window, mouse
from main import Main
from sprite.menu import MenuSprite


class Game(Window):

    def __init__(self):
        """
        A game window class from pyglet.window.Window used for our mario game.
        """
        super().__init__(800,600)
        self.main = Main()
        self.menu = MenuSprite()
        self.batch = pyglet.graphics.Batch()

    def on_draw(self):
        self.clear()
        self.main.draw()
        self.menu.draw()

    def update(self, dt):
        self.menu.fade_update(dt)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.menu.is_clicked(x, y):
                self.menu.fade()



if __name__ == '__main__':
    window = Game()
    pyglet.clock.schedule_interval(window.update, 1 / 60)
    pyglet.app.run()
