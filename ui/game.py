import pyglet
from pyglet.window import Window, mouse
from main import Main
from sprite.menu import MenuSprite
from ui.sprite.mario import Mario

game = Window(800, 600)

main = Main()
menu = MenuSprite()
mario = Mario(0, main.get_ground_height()-10)

@game.event
def on_draw():
    game.clear()
    main.draw()
    menu.draw()
    mario.draw()

@game.event
def on_key_press(symbol, modifiers):
    mario.animation(symbol)

@game.event
def on_key_release(symbol, modifiers):
    mario.animation_end(symbol)

def update(dt):
    menu.fade_update(dt)
    mario.move(dt)

@game.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if menu.is_clicked(x, y):
            menu.fade()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()
