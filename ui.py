# Basic Idea:
#      ▄▄█▄▄              █                █
#     ▄▄▄█▄▄▄             █                █
#    ▄▄▄▄█▄▄▄▄            █                █
#   ▄▄▄▄▄█▄▄▄▄▄           █                █
#  ▄▄▄▄▄▄█▄▄▄▄▄▄          █                █
# ▄▄▄▄▄▄▄█▄▄▄▄▄▄▄         █                █
#▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄▄▄▄▄▄▄▄

import curses,time,math
from gm import Gm

SPACECH = " "
TILECH = "▄"
POLECH = "█"

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

def drawBoard(x,y,board,max_tile,moves=None):
    for l in range(max_tile+1):
        line = ""
        for p in board:
            line += tileString(list(reversed(p))[l],max_tile)
        scr.addstr(y+l,x,line)
    line = ""
    for i in board:
        line += tileString(max_tile+1,max_tile)
    scr.addstr(y+1+l,x,line)
    if moves is not None:
        scr.addstr(y+3+l,x,"Moves: "+str(moves))

def debugStr(str):
    scr.addstr(10,10,str)
    scr.refresh()
#drawBoard(0,0,[[2,1,0],[None,None,None],[None,None,None]],2)
ntiles = input("Number of Tiles?[5]\n")
if ntiles == "":
    ntiles = 5
try:
    ntiles = int(ntiles)
except:
    print("not int")
    exit()

npoles = input("Number of Poles?[3]\n")
if npoles == "":
    npoles = 3
try:
    npoles = int(npoles)
except:
    print("not int")
    exit()

hanoi = Gm(ntiles,npoles)

scr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
curses.mousemask(1)
scr.keypad(True)

pole = None
moves = 0
while True:
    drawBoard(0,0,hanoi.board,ntiles-1,moves)
    scr.refresh()
    ch = scr.getch()
    if ch == ord("q"):
        break

    if ch == ord("r"):
        hanoi.restart()
        moves = 0
        scr.clear()
        drawBoard(0,0,hanoi.board,ntiles-1,moves)
        scr.refresh()

    if ch == ord("f"):
        pole_input = scr.getch()
        if pole_input == ord("q"):
            pass
        else:
            try:
                if (int(chr(pole_input)) <= npoles) and (int(chr(pole_input)) < 10):
                    pole = int(chr(pole_input)) - 1
            except ValueError:
                pass #error

    if (ch == ord("t")) and (pole is not None):
        pole_input = scr.getch()
        if pole_input == ord("q"):
            pass
        else:
            try:
                if (int(chr(pole_input)) <= npoles) and (int(chr(pole_input)) < 10):
                    moves += hanoi.move(pole,int(chr(pole_input)) - 1)
                    scr.clear()
                    drawBoard(0,0,hanoi.board,ntiles-1,moves)
                    scr.refresh()
                    pole = None
            except ValueError:
                pass #error

    if ch == curses.KEY_MOUSE:
        _,x,y,_,_ = curses.getmouse()
        if y <= ntiles + 1:
            if pole is None:
                pole = math.floor(x/((2*(ntiles+3))+1))
            else:
                moves += hanoi.move(pole,math.floor(x/((2*(ntiles+3))+1)))
                scr.clear()
                drawBoard(0,0,hanoi.board,ntiles-1,moves)
                scr.refresh()
                pole = None

        


curses.nocbreak()
scr.keypad(False)
curses.echo()
curses.endwin()
