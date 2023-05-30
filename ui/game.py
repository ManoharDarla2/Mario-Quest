import pyglet
import time
from pyglet.window import Window, mouse
from sprites import *

game = Window(800, 600)
sky = Sprite(sky_img)
g_frame = GroundFrame()
ground = Ground(0, 0, g_frame)
mario = Mario(0, ground.height - 10, g_frame) #ground.height - 10



@game.event
def on_draw():
    game.clear()
    sky.draw()
    g_frame.draw()

@game.event
def on_key_press(symbol, modifiers):
    if symbol == RIGHT:
        mario.is_jump_on_key = True
    mario.animation(symbol)
    ground.run(symbol)

@game.event
def on_key_release(symbol, modifiers):
    if symbol == SPACE:
        mario.is_jump_on_key = True
    if symbol == RIGHT:
        mario.is_jump_on_key = False
    mario.animation_end(symbol)
    ground.stop(symbol)

def update(dt):
    # menu.fade_update(dt)
    mario.on_jump(dt)
    mario.move(dt)
    if mario.x >= 300.1:
        mario.x = 300
        ground.move(dt)
    elif mario.x <= 0:
        mario.x = 0.1




@game.event
def on_mouse_press(x, y, button, modifiers):
    pass
    # if button == mouse.LEFT:
    #     if menu.is_clicked(x, y):
    #         menu.fade()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
