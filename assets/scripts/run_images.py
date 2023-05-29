import os

from utils.utils import rename_files, image_scale
from utils.paths import ASSETS_PATH, MARIO_PATH

run_path = f'{ASSETS_PATH}/raw/mario_run'
scale_path = f'{ASSETS_PATH}/raw/scaled'
out = f'{MARIO_PATH}/run'

if __name__ == '__main__':
    rename_files(run_path, f'{scale_path}/run', 'run')

    run_images = os.listdir(f'{scale_path}/run')
    run_images.sort()
    for image in run_images:
        image_scale(f'{scale_path}/run/{image}', f'{out}/{image}', scale=0.2)
