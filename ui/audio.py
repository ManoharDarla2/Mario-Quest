from pyglet.media import load, Player
from utils.resources import SFX_PATH

# Main Theme
main_sfx = load(f'{SFX_PATH}/main_theme.mp3')
theme = Player()
theme.queue(main_sfx)

# Other SFX sounds
coin_sfx = load(f'{SFX_PATH}/coin.mp3')
death_sfx = load(f'{SFX_PATH}/death.mp3')
jump_sfx = load(f'{SFX_PATH}/jump.mp3')
