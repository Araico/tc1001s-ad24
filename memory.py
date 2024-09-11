from random import *
from turtle import *

# Inicialización de recursos
from freegames import path

car = path("car.gif")

# Crear una lista de letras y números (pares asegurados)
elements = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")[
    :32
]  # Usamos las primeras 32 letras/números para asegurar pares
tiles = elements * 2  # Crear pares de fichas
state = {"mark": None}  # Estado del juego para las fichas seleccionadas
hide = [True] * 64  # Todas las fichas están ocultas al inicio
tap_count = 0  # Contador de taps

# Lista de colores y asignación de colores a las letras/números
colors = [
    "red",
    "green",
    "blue",
    "orange",
    "purple",
    "cyan",
    "magenta",
    "darkslategray",
] * 8  # Colores repetidos
color_map = {}  # Mapa de colores para las letras
for i, tile in enumerate(set(tiles)):  # Asigna un color único por letra/número
    color_map[tile] = colors[i % len(colors)]  # Colores iguales para letras iguales


def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro en las coordenadas (x, y)."""
    up()
    goto(x, y)
    down()
    color("black", "white")
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte coordenadas (x, y) en un índice de la lista de fichas."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)  # Para cuadrícula 8x8


def xy(count):
    """Convierte el índice de la ficha en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (
        count // 8
    ) * 50 - 200  # Coordenadas ajustadas para cuadrícula 8x8


def tap(x, y):
    """Actualiza el estado de las fichas cuando se hace clic."""
    global tap_count  # Usamos el contador global de taps
    spot = index(x, y)
    mark = state["mark"]

    tap_count += 1  # Incrementa el contador de taps

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state["mark"] = spot
    else:
        hide[spot] = False  # Revela las fichas si son iguales
        hide[mark] = False
        state["mark"] = None

    # Detectar si todas las fichas han sido reveladas
    if all(not hidden for hidden in hide):
        print("¡Todas las fichas han sido reveladas!")


def draw():
    """Dibuja las fichas y muestra el número de taps."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibujar las fichas ocultas
    for count in range(64):  # Para la cuadrícula 8x8
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    # Dibujar las letras o números revelados
    mark = state["mark"]
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 25, y + 10)  # Ajustar para centrar el texto
        color(color_map[tiles[mark]])  # Usar el color correspondiente a la letra
        write(tiles[mark], font=("Arial", 30, "normal"), align="center")

    # Mostrar el contador de taps en la parte superior izquierda
    up()
    goto(-190, 180)  # Posición del contador de taps
    color("black")
    write(f"Taps: {tap_count}", font=("Arial", 20, "normal"))

    update()
    ontimer(draw, 100)  # Redibuja cada 100ms


# Mezclar las fichas
shuffle(tiles)

# Configuración de la pantalla
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)  # Detectar los clics del usuario
draw()
done()
