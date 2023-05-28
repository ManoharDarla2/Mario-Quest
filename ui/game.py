import pyglet
from pyglet.window import Window, mouse
from menu import Menu
from main import Main


class Game(Window):

    def __init__(self):
        """
        A game window class from pyglet.window.Window used for our mario game.
        """
        super().__init__(800,600)
        self.main = Main()
        self.menu = Menu()
        self.batch = pyglet.graphics.Batch()

    def on_draw(self):
        self.clear()
        self.main.draw()
        self.menu.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == mouse.LEFT:
            if self.menu.start(x, y):
                self.menu.hide()



if __name__ == '__main__':
    window = Game()
    pyglet.app.run()
