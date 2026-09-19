"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
# the original board was 8x8 with 50 pixel tiles, this one is 4x4 with
# 100 pixel tiles so it still covers the whole 400x400 image
COLS = 4
SIZE = 100
TOTAL = COLS * COLS
PAIRS = TOTAL // 2
HALF = COLS * SIZE // 2

tiles = list(range(PAIRS)) * 2
state = {'mark': None, 'pairs': 0}
hide = [True] * TOTAL


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

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
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
