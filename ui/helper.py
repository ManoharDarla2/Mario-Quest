import pyglet

is_moving = False
move_elapsed = 0
last_x = 0


def move(player, sprite, duration=3, dt=0, window_width=800):
    width = window_width - 150
    global move_elapsed, is_moving, last_x
    if is_moving:
        move_elapsed += dt
        if move_elapsed >= duration:
            last_x = int((-((move_elapsed / duration) * (width+350)) + last_x))
            print(last_x)
            is_moving = False
        else:
            player.x = int((1 - (move_elapsed / duration)) * width)
            sprite.x = int((-((move_elapsed / duration) * (width+250)) + last_x))
            print(sprite.x)



def run():
    global is_moving, move_elapsed
    is_moving = True
    move_elapsed = 0


def stop():
    global is_moving, move_elapsed
    is_moving = False
    move_elapsed = 0
