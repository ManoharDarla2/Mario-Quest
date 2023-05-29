import glob
from PIL import Image
from utils.paths import *


def mirror(image, output):
    mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored_image.save(output)


run_path = glob.glob(pathname=f'{MARIO_PATH}/run/run*.png')
run_path = [path.replace('\\', '/') for path in run_path]
run_path.sort(key=len)
images = [Image.open(path) for path in run_path]

for i, image in enumerate(images, start=1):
    mirror(image, f'{MARIO_PATH}/run/left/run{i}.png')

s1 = Image.open(f'{MARIO_PATH}/stand/stand1.png')
s2 = Image.open(f'{MARIO_PATH}/stand/stand2.png')
mirror(s1, f'{MARIO_PATH}/stand/left/stand1.png')
mirror(s2, f'{MARIO_PATH}/stand/left/stand2.png')



print("Image mirrored and saved successfully.")
