import pyglet
from pyglet.window import Window, mouse
from pyglet.sprite import Sprite
from utils.resources import sky_img, ground_img
from sprite.menu import MenuSprite
from ui.sprite.mario import Mario
import helper

game = Window(800, 600)
sky = Sprite(sky_img)
ground = Sprite(ground_img)
menu = MenuSprite()
mario = Mario(0, ground_img.height-10)



@game.event
def on_draw():
    game.clear()
    sky.draw()
    ground.draw()
    menu.draw()
    mario.draw()

@game.event
def on_key_press(symbol, modifiers):
    mario.animation(symbol)

@game.event
def on_key_release(symbol, modifiers):
    mario.animation_end(symbol)

def update(dt):
    global delay
    menu.fade_update(dt)
    mario.move(dt)
    if mario.x >= 700:
        helper.run()
    if mario.x <= 0:
        mario.x = 0
    helper.move(mario, ground, dt=dt)



@game.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        if menu.is_clicked(x, y):
            menu.fade()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 60)
    pyglet.app.run()
