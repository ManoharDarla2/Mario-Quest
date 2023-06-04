import pyglet
from pyglet.window import Window, mouse
from sprites import *
from audio import theme
from helper import *

game = Window(800, 600)

menu = Menu(200, 150)

frame = pyglet.graphics.Batch()
sky = Sprite(sky_img, 0, 0, batch=frame)
clouds = Base(clouds_img, 0, 300, frame)
ground = Ground(0, 0, frame)
ground2 = Ground(7500, 0, frame)
castle = Base(castle_img, 8000, 93, batch=frame)
door = Sprite(door_img, 8000, 93)
mountains = Base(mountains_img, 0, ground.height, batch=frame)
mario = Mario(0, ground.height - 10, frame)

coins = Coins(ground.height, frame)
coins.create(random.randint(20, 30), 400, 7300)

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

brick_x = [800, 1500, 2400, 3200, 4000, 5500, 6000, 6700, 7500]

bricks = Bricks(brick_pattern, brick_x, [200] * len(brick_pattern), frame)
bricks.create()

enemy_x = [400, 1000, 1500, 1800, 1900, 2500, 2800, 3200, 3600, 4000, 4500, 5000,
           5300, 5700, 6000, 6400, 6900, 7300, 7700, 8000, 8300, 8600, 9000, 9100]
enemies = Enemy([2000], 83, frame)

theme.volume = 0.3
theme.play()

points = 0

score_label = pyglet.text.Label('0',
                                font_name='Arial',
                                font_size=24,
                                color=(0, 0, 0, 255),
                                x=10, y=game.height - 32.5)

score_img = Sprite(coin_img, 33, y=game.height - 40)

end_label = pyglet.text.Label("YOU \n LOST",
                              font_name='Typeface Mario 64',
                              font_size=40,
                              color=(255, 255, 255, 255),
                              x=380, y=300, width=100,
                              anchor_x='center', anchor_y="center",
                              multiline=True
                              )

end_label.visible = False
door.visible = False

is_lose = False
is_win = False
is_stopped = False
is_started = False

@game.event
def on_draw():
    global is_stopped
    game.clear()
    if not is_lose:
        frame.draw()
    score_label.draw()
    score_img.draw()
    end_label.draw()
    door.draw()
    menu.draw()
    if is_stopped:
        mario.image = stand(0.35)[0]


@game.event
def on_key_press(symbol, modifiers):
    mario.start(symbol)
    ground.run(symbol)


@game.event
def on_key_release(symbol, modifiers):
    mario.stop(symbol)
    ground.stop(symbol)
    if not is_stopped and ground2.x <= 400:
        mario.image = run(0.06)[0]


def update(dt):
    global points, is_lose, is_win, is_stopped, is_started
    fade_menu(menu, 0.5, dt)
    if is_started:
        door.x = castle.x
        door.y = castle.y
        if ground2.x <= 400:
            if not is_stopped:
                mario.x += 10 * dt
                ground.x -= 170 * dt
                ground2.x -= 170 * dt
                castle.x -= 170 * dt
                clouds.x -= 170 * dt
                mountains.x -= 170 * dt
        else:
            mario.jump(dt)
            ground.attach(mountains, True)
            ground.attach(clouds, False)
            ground.attach(ground2, False)
            ground.attach(castle, False)
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

            is_alive = True
            is_win = False
            for enemy in enemies.get():
                if mario.is_dead(enemy):
                    is_alive = False

            if not is_alive:
                death_sfx.play()
                end_label.visible = True
                is_lose = True

        if is_win:
            end_label.text = "You \n Win"
            end_label.visible = True
            mario.y = 93
            door.visible = True

        if mario.x + mario.width >= castle.x + (castle.width // 2) + 35:
            is_stopped = True
            is_win = True

        if int(score_label.text) == 10:
            score_img.x = 55


@game.event
def on_mouse_press(x, y, button, modifiers):
    global is_started
    if button == mouse.LEFT:
        if menu.is_clicked(x, y):
            is_started = True
            menu_click()


if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1 / 120)
    pyglet.app.run()
