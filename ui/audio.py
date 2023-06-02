from pyglet.media import load, Player
from utils.resources import SFX_PATH

main_sfx = load(f'{SFX_PATH}/main_theme.mp3')
theme = Player()
theme.queue(main_sfx)

coin_sfx = load(f'{SFX_PATH}/coin.mp3')