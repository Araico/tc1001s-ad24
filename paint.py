from turtle import *
from freegames import vector

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def draw_circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    # Calculamos el radio usando la distancia entre el punto de inicio y el punto final
    radius = ((end.x - start.x) ** 2 + (end.y - start.y) ** 2) ** 0.5
    
    # Usamos un bucle para dibujar un círculo aproximadamente
    num_steps = 360
    step_length = 2 * 3.14 * radius / num_steps
    step_angle = 360 / num_steps

    for _ in range(num_steps):
        forward(step_length)
        left(step_angle)
    
    end_fill()

def draw_rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for _ in range(2):
        forward(end.x - start.x)  # Largo del rectángulo
        left(90)
        forward(end.y - start.y)  # Ancho del rectángulo
        left(90)

    end_fill()

def draw_triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calculamos la longitud de los lados
    for _ in range(3):
        forward(end.x - start.x)  # Longitud de los lados del triángulo
        left(120)  # Ángulo interno de 120 grados para un triángulo equilátero

    end_fill()

def tap(x, y):
    """Store starting point or draw shape."""
    start = state["start"]

    if start is None:
        state["start"] = vector(x, y)
    else:
        shape = state["shape"]
        end = vector(x, y)
        shape(start, end)
        state["start"] = None

def store(key, value):
    """Store value in state at key."""
    state[key] = value

# Estado inicial
state = {"start": None, "shape": line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, "u")

# Agregamos un nuevo color, amarillo
onkey(lambda: color("yellow"), "Y")

# Colores existentes
onkey(lambda: color("black"), "K")
onkey(lambda: color("white"), "W")
onkey(lambda: color("green"), "G")
onkey(lambda: color("blue"), "B")
onkey(lambda: color("red"), "R")

# Formas
onkey(lambda: store("shape", line), "l")
onkey(lambda: store("shape", square), "s")
onkey(lambda: store("shape", draw_circle), "c")
onkey(lambda: store("shape", draw_rectangle), "r")
onkey(lambda: store("shape", draw_triangle), "t")

done()
