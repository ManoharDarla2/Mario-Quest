import pyglet
import time
from pyglet.window import Window, mouse
from sprites import *

game = Window(800, 600)
frame = pyglet.graphics.Batch()
sky = Sprite(sky_img, batch=frame)
clouds = Sprite(clouds_img, batch=frame)
ground = Ground(0, 0, frame)
mountains = Sprite(mountains_img, batch=frame)
mario = Mario(0, ground.height - 10, frame)

def coins(n, batch):
    cs = []
    for i in range(n):
        coin_x = random.randint(400, 7800)
        c = Coin(coin_x, batch)
        cs.append(c)
    return cs

cns = coins(30, frame)

clouds.y = 300
is_cloud_movement = False



@game.event
def on_draw():
    game.clear()
    frame.draw()

@game.event
def on_key_press(symbol, modifiers):
    global is_cloud_movement
    if symbol == RIGHT and mario.x >= 300:
        is_cloud_movement = True
    mario.animation(symbol)
    ground.run(symbol)

@game.event
def on_key_release(symbol, modifiers):
    global is_cloud_movement
    if symbol == RIGHT:
        is_cloud_movement = False
    mario.animation_end(symbol)
    ground.stop(symbol)

def update(dt):
    global is_cloud_movement
    mario.on_jump(dt)
    ground.attach(mountains)
    clouds.x -= 220 * dt if is_cloud_movement else 10 * dt
    mario.move(dt)
    for i in cns:
        ground.attach_coin(i)
        if i.x + i.width >= mario.x >= i.x and mario.y <= i.y + i.height:
            i.visible = False
    if mario.x + mario.width >= 300.1:
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
