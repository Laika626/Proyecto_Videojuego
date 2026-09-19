"""Tres en Raya (Tic Tac Toe).

Juego interactivo de gato desarrollado con el módulo turtle.
"""

from turtle import *
from freegames import line


def grid():
    """Dibuja la cuadrícula del juego tres en raya."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja el símbolo del jugador X con color rojo y centrado."""
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
    """Dibuja el símbolo del jugador O con trazo azul grueso y centrado."""
    color('royal blue')
    width(5)
    up()
    goto(x + 67, y + 25)
    down()
    circle(42)


def floor(value):
    """Redondea el valor a la esquina inferior de la casilla correspondiente."""
    return ((value + 200) // 133) * 133 - 200


# Estado del turno actual (0 para X, 1 para O)
state = {'player': 0}
players = [drawx, drawo]

# Diccionario para registrar casillas ocupadas: {(x, y): jugador}
occupied = {}


def check_game_over():
    """Verifica si existe un ganador o si el tablero terminó en empate."""
    board = [
        occupied.get((-200, 66)), occupied.get((-67, 66)), occupied.get((66, 66)),
        occupied.get((-200, -67)), occupied.get((-67, -67)), occupied.get((66, -67)),
        occupied.get((-200, -200)), occupied.get((-67, -200)), occupied.get((66, -200)),
    ]
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Combinaciones horizontales
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Combinaciones verticales
        (0, 4, 8), (2, 4, 6),              # Combinaciones diagonales
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
    """Procesa el clic en pantalla, valida casilla disponible y alterna turno."""
    x = floor(x)
    y = floor(y)

    # Evita sobreescribir si la casilla ya fue seleccionada
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