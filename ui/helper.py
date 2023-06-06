menu_fade = False
fade_elapsed = 0.0


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


def menu_click():
    global menu_fade, fade_elapsed
    menu_fade = True
    fade_elapsed = 0.0


def fade_menu(menu, duration, dt):
    global menu_fade
    fade_out(menu, duration, dt, menu_fade)
