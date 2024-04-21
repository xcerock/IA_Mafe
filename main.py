import turtle

def setup_board(board_size):
    """ Configura el tablero de juego con un tamaño de casilla especificado. """
    turtle.setup(board_size * 8, board_size * 8)
    turtle.screensize(board_size * 8, board_size * 8)
    turtle.bgcolor("white")
    turtle.up()
    turtle.speed('fastest')  # Configura la velocidad de dibujo a la más rápida

def draw_square(color, start_x, start_y, size):
    """ Dibuja un cuadrado de un color y tamaño especificados. """
    turtle.goto(start_x, start_y)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    turtle.up()

def draw_board(size):
    """ Dibuja un tablero de damas de 8x8. """
    start_x = -size * 4
    start_y = -size * 4
    for row in range(8):
        for col in range(8):
            color = "black" if (row + col) % 2 == 0 else "red"
            draw_square(color, start_x + col * size, start_y + row * size, size)

def draw_piece(x, y, color):
    """ Dibuja una pieza de damas en la posición y color especificados. """
    turtle.goto(x + size/2, y + size/2 - 20)
    turtle.down()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(20)  # Radio de la pieza
    turtle.end_fill()
    turtle.up()

def setup_pieces(size):
    """ Configura las piezas en el tablero inicialmente. """
    start_x = -size * 4
    start_y = -size * 4
    for row in range(3):  # Piezas negras
        for col in range(8):
            if (row + col) % 2 == 1:
                draw_piece(start_x + col * size, start_y + row * size, "black")
    for row in range(5, 8):  # Piezas rojas
        for col in range(8):
            if (row + col) % 2 == 1:
                draw_piece(start_x + col * size, start_y + row * size, "red")

# Inicializa el juego
size = 50  # Tamaño de cada cuadrado del tablero
setup_board(size)
draw_board(size)
setup_pieces(size)
turtle.done()
