from utils.utils import image_scale
from utils.paths import MAIN_PATH
from run_images import scale_path

image_scale(f'{scale_path}/mountains.png', f'{MAIN_PATH}/mountains.png', scale=0.25)