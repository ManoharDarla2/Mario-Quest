from pyglet.window import Window, mouse
from sprites import *
from audio import theme

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
                 ]

brick_x = [300, 700, 1300, 2400, 3000]

bricks = Bricks(brick_pattern, brick_x, [200] * 5, frame)
bricks.create()

theme.play()

points = 0

@game.event
def on_draw():
    game.clear()
    frame.draw()

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
    global points
    mario.jump(dt)
    ground.attach(mountains, True)
    ground.attach(clouds, False)
    mario.move(dt)
    bricks.set(ground, mario)
    points += coins.collected(mario, ground)
    # for i in cns:
    #     ground.attach_coin(i)
    #     if i.x + (i.width // 2) >= mario.x >= i.x - (mario.width // 2) and mario.y <= i.y + i.height and i.visible:
    #         i.visible = False
    #         coin_sfx.play()
    # for i in bks:
    #     ground.attach_pos(i)
    # if bks[0].is_on_block(len(bks), mario):
    #     mario.y = bks[0].y + bks[0].height
    #     mario.velocity_y = 0
    if mario.x >= 300.1:
        mario.x = 300
        ground.move(dt)
    elif mario.x <= 0:
        mario.x = 0.1
        mario.move(dt)




@game.event
def on_mouse_press(x, y, button, modifiers):
    pass
    # if button == mouse.LEFT:
    #     if menu.is_clicked(x, y):
    #         menu.fade()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
