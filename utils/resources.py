import glob
from pyglet.image import animation
from pyglet.image import load
from paths import *

# Mario Image Paths
run_path = glob.glob(pathname=f'{MARIO_PATH}/run/run*.png')
run_path = [path.replace('\\', '/') for path in run_path]
run_path.sort(key=len)
stand_path = [f'{MARIO_PATH}/stand/stand1.png', f'{MARIO_PATH}/stand/stand2.png']

run_images = [load(path) for path in run_path]
stand_images = [load(path) for path in stand_path]
run_imagesL = [run.get_texture().get_transform(flip_x=True) for run in run_images]
stand_imagesL = [stand.get_texture().get_transform(flip_x=True) for stand in stand_images]


def run(duration):
    run_r = animation.Animation.from_image_sequence(run_images, duration)
    run_l = animation.Animation.from_image_sequence(run_imagesL, duration)
    return run_r, run_l


def stand(duration):
    stand_r = animation.Animation.from_image_sequence(stand_images, duration)
    stand_l = animation.Animation.from_image_sequence(stand_imagesL, duration)
    return stand_r, stand_l


