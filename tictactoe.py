"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('firebrick')
    width(5)
    up()
    goto(x + 33, y + 33)
    down()
    goto(x + 100, y + 100)
    up()
    goto(x + 100, y + 33)
    down()
    goto(x + 33, y + 100)


def drawo(x, y):
    """Draw O player."""
    color('royal blue')
    width(5)
    up()
    goto(x + 67, y + 25)
    down()
    circle(42)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
occupied = {}

def check_game_over():
    """Verifica si hay un ganador o si el juego terminó en empate."""
    board = [
        occupied.get((-200, 66)), occupied.get((-67, 66)), occupied.get((66, 66)),
        occupied.get((-200, -67)), occupied.get((-67, -67)), occupied.get((66, -67)),
        occupied.get((-200, -200)), occupied.get((-67, -200)), occupied.get((66, -200)),
    ]
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Filas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columnas
        (0, 4, 8), (2, 4, 6),              # Diagonales
    ]
    for a, b, c in lines:
        if board[a] is not None and board[a] == board[b] == board[c]:
            winner = "O" if board[a] == 1 else "X"
            up()
            goto(0, 0)
            color('dark green')
            write(f"¡Ganó {winner}!", align='center', font=('Arial', 24, 'bold'))
            onscreenclick(None)
            return

    if len(occupied) == 9:
        up()
        goto(0, 0)
        color('dark red')
        write("¡Empate!", align='center', font=('Arial', 24, 'bold'))
        onscreenclick(None)

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    if (x, y) in occupied:
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    occupied[(x, y)] = player
    update()
    state['player'] = not player
    check_game_over()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
