import pyglet
from pyglet.window import Window, mouse
from sprites import *
from audio import theme
from utils.paths import ASSETS_PATH

game = Window(800, 600)
frame = pyglet.graphics.Batch()
sky = Sprite(sky_img, 0, 0, batch=frame)
clouds = Base(clouds_img, 0, 300, frame)
ground = Ground(0, 0, frame)
mountains = Base(mountains_img, 0, ground.height, batch=frame)
mario = Mario(0, ground.height - 10, frame)

coins = Coins(0, ground.height, frame)
coins.create(30, 400, 8000)

brick_pattern = ['________',
                 '______',
                 '____________',
                 '_____',
                 '____'
                 '______',
                 '_________',
                 '_____',
                 '_________'
                 ]

brick_x = [400, 1200, 2400, 3200, 4000, 5500, 6000, 6700, 7500]

bricks = Bricks(brick_pattern, brick_x, [200] * len(brick_pattern), frame)
bricks.create()

enemies = Enemy([900, 1800, 2700, 3600, 4500, 5400, 6300], 83, frame)

theme.play()

points = 0

score_label = pyglet.text.Label(font_name='Arial',
                                font_size=18,
                                color=(0, 0, 0, 255),
                                x=10, y=game.height - 30)

lose_label = pyglet.text.Label("YOU \n LOST",
                               font_name='Typeface Mario 64',
                               font_size=40,
                               color=(255, 255, 255, 255),
                               x=380, y=300, width=100,
                               anchor_x='center', anchor_y="center",
                               multiline=True
                               )

lose_label.visible = False

is_lose = False

@game.event
def on_draw():
    game.clear()
    if not is_lose:
        frame.draw()
    score_label.draw()
    lose_label.draw()


@game.event
def on_key_press(symbol, modifiers):
    mario.start(symbol)
    ground.run(symbol)


@game.event
def on_key_release(symbol, modifiers):
    mario.stop(symbol)
    ground.stop(symbol)


@game.event
def on_close():
    print(points)


def update(dt):
    global points, is_lose
    mario.jump(dt)
    ground.attach(mountains, True)
    ground.attach(clouds, False)
    mario.move(dt)
    bricks.set(ground, mario)
    points += coins.collected(mario, ground)
    score_label.text = f'{points}'
    enemies.move(50 * dt)
    if mario.x >= 300.1:
        mario.x = 300
        ground.move(dt)
        enemies.move(250 * dt)
    elif mario.x <= 0:
        mario.x = 0.1
        mario.move(dt)
    if mario.is_dead(enemies.get()):
        lose_label.visible = True
        is_lose = True



@game.event
def on_mouse_press(x, y, button, modifiers):
    pass
    # if button == mouse.LEFT:
    #     if menu.is_clicked(x, y):
    #         menu.fade()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
