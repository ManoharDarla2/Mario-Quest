import glob
from pyglet.image import animation
from pyglet.image import load
from utils.paths import *

# Props and Backgrounds
sky_img = load(f'{MAIN_PATH}/sky.png')
ground_img = load(f'{MAIN_PATH}/ground_pattern.png')
menu = load(f'{MENU_PATH}/menu.png')

# Mario Image Paths
run_path = glob.glob(pathname=f'{MARIO_PATH}/run/run*.png')
run_path = sorted(run_path, key=len)
run_right_path = [path.replace('\\', '/') for path in run_path]
run_left_path = [path.replace('/run\\', '/run/left/') for path in run_path]
stand_right_path = [f'{MARIO_PATH}/stand/stand1.png', f'{MARIO_PATH}/stand/stand2.png']
stand_left_path = [f'{MARIO_PATH}/stand/left/stand1.png', f'{MARIO_PATH}/stand/left/stand2.png']

run_right = [load(path) for path in run_right_path]
run_left = [load(path) for path in run_left_path]
stand_right = [load(path) for path in stand_right_path]
stand_left = [load(path) for path in stand_left_path]


def run(duration):
    right = animation.Animation.from_image_sequence(run_right, duration)
    left = animation.Animation.from_image_sequence(run_left, duration)
    return right, left


def stand(duration):
    right = animation.Animation.from_image_sequence(stand_right, duration)
    left = animation.Animation.from_image_sequence(stand_left, duration)
    return right, left