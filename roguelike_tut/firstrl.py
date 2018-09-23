# -*- coding: utf-8 -*-
import libtcodpy as tcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

font_path = 'arial10x10.png'
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)

window_title = 'Python 3 libtcod tutorial'
fullscreen = False
tcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, window_title, fullscreen)

con = tcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

def handle_keys():
    global player_x, player_y

    # movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        player_y -= 1

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        player_y += 1

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        player_x -= 1

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        player_x += 1

    key = tcod.console_wait_for_keypress(True)
    if key.vk == tcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    elif key.vk == tcod.KEY_ESCAPE:
        return True #exit game

while not tcod.console_is_window_closed():
    tcod.console_set_default_foreground(con, tcod.white)
    tcod.console_put_char(con, player_x, player_y, '@', tcod.BKGND_NONE)

    tcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

    tcod.console_flush()

    #handle keys and exit game if needed
    tcod.console_put_char(con, player_x, player_y, ' ', tcod.BKGND_NONE)
    exit = handle_keys()
    if exit:
        break