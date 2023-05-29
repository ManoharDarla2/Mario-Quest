import glob
from PIL import Image
from utils.paths import *


run_path = glob.glob(pathname=f'{MARIO_PATH}/run/run*.png')
run_path = [path.replace('\\', '/') for path in run_path]
run_path.sort(key=len)
images = [Image.open(path) for path in run_path]

for i, image in enumerate(images, start=1):
    mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored_image.save(f'{MARIO_PATH}/run/left/run{i}.png')


print("Image mirrored and saved successfully.")
