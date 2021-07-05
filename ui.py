# Basic Idea:
#      ▄▄█▄▄              █                █
#     ▄▄▄█▄▄▄             █                █
#    ▄▄▄▄█▄▄▄▄            █                █
#   ▄▄▄▄▄█▄▄▄▄▄           █                █
#  ▄▄▄▄▄▄█▄▄▄▄▄▄          █                █
# ▄▄▄▄▄▄▄█▄▄▄▄▄▄▄         █                █
#▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄

import curses
from gm import Gm

SPACECH = " "
TILECH = "▄"
POLECH = "█"
'''
scr = curses.initscr()
curses.noecho()
curses.cbreak()
scr.keypad(True)
'''
def tile(num,max_num):
    radius = num + 2
    max_radius = max_num + 2
    empty = max_radius - radius
    first_half = ""
    for ch in range(max_radius):
        if ch < empty:
            first_half += SPACECH
        else:
            first_half += TILECH
    tile_string = first_half + POLECH + first_half[::-1]
    return tile_string

def drawBoard(board):
    
'''
curses.nocbreak()
scr.keypad(False)
curses.echo()
curses.endwin()
'''