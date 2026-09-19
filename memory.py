"""Memory, puzzle game of number pairs.

Modified for the final project by Miguel Huizache Vazquez, A01713936.

Changes:

1. The board went from 8x8 down to 4x4.
2. The pairs that have been found are counted and shown on screen.
3. The game notices when every tile has been turned over.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')  # picture hidden behind the tiles

# the original board was 8x8 with 50 pixel tiles, this one is 4x4 with
# 100 pixel tiles so it still covers the whole 400x400 image
COLS = 4
SIZE = 100
TOTAL = COLS * COLS
PAIRS = TOTAL // 2
HALF = COLS * SIZE // 2

tiles = list(range(PAIRS)) * 2  # every number shows up twice to make a pair
state = {'mark': None, 'pairs': 0}  # 'mark' is the tile waiting for its match
hide = [True] * TOTAL  # hide[i] stays True while tile i is face down


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(SIZE)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + HALF) // SIZE + ((y + HALF) // SIZE) * COLS)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % COLS) * SIZE - HALF, (count // COLS) * SIZE - HALF


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    # the window is larger than the board now, so a click outside of it
    # would fall out of the tiles list
    if not (-HALF <= x < HALF and -HALF <= y < HALF):
        return

    spot = index(x, y)

    # a tile that is already face up should not count as a new pair
    if not hide[spot]:
        return

    mark = state['mark']

    # with nothing to match against, or with two different numbers, the
    # tile just becomes the new mark
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # the two numbers match, so both tiles stay face up
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['pairs'] += 1


def draw():
    """Draw image and tiles."""
    clear()
    up()  # keeps the move to the center from leaving a line behind
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(TOTAL):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # the marked tile is the only one showing its number
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + SIZE / 2, y + SIZE / 2 - 22)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align='center')

    # pairs found so far, written above the board
    up()
    goto(-HALF, HALF + 15)
    color('black')
    write('Pairs: {} of {}'.format(state['pairs'], PAIRS), font=('Arial', 16, 'bold'))

    # no tile is left face down once every pair has been found
    if state['pairs'] == PAIRS:
        up()
        goto(0, -HALF - 45)
        color('red')
        write('You found them all!', font=('Arial', 14, 'bold'), align='center')

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(COLS * SIZE + 120, COLS * SIZE + 120, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
