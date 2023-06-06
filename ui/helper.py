# Required Variables for Menu Fade
menu_fade = False
fade_elapsed = 0.0


# Fade Out animation for menu
def fade_out(sprite, duration, dt, fading):
    global fade_elapsed
    if fading:
        fade_elapsed += dt
        if fade_elapsed >= duration:
            sprite.opacity = 0
            fade_elapsed = 0.0
            sprite.visible = False
        else:
            sprite.opacity = int((1 - (fade_elapsed / duration)) * 255)


# Helper function to start menu fade
def menu_click():
    global menu_fade, fade_elapsed
    menu_fade = True
    fade_elapsed = 0.0


# Helper function to start menu fade out animation
def fade_menu(menu, duration, dt):
    global menu_fade
    fade_out(menu, duration, dt, menu_fade)
