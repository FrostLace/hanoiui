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

scr = curses.initscr()
curses.noecho()
curses.cbreak()
scr.keypad(True)

def tileString(num,max_num):
    if num is not None:
        radius = num + 2
    else:
        radius = 0
    max_radius = max_num + 3
    empty = max_radius - radius
    first_half = ""
    for ch in range(max_radius):
        if ch < empty:
            first_half += SPACECH
        else:
            first_half += TILECH
    tile_string = first_half + POLECH + first_half[::-1]
    return tile_string

def drawBoard(x,y,board,max_tile):
    for l in range(max_tile+1):
        line = ""
        for p in board:
            line += tileString(list(reversed(p))[l],max_tile)
        scr.addstr(y+l,x,line)
    line = ""
    for i in board:
        line += tileString(max_tile+1,max_tile)
    scr.addstr(y+1+l,x,line)

drawBoard(0,0,[[2,1,0],[None,None,None],[None,None,None]],2)

curses.nocbreak()
scr.keypad(False)
curses.echo()
curses.endwin()
