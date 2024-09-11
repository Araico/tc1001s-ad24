from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Ajustar la velocidad del proyectil para que sea más rápida
        speed.x = (x + 200) / 15  # Cambiar el divisor a 15 para mayor velocidad
        speed.y = (y + 200) / 15  # Cambiar el divisor a 15 para mayor velocidad

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, "blue")

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, "red")

    update()

def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # Reposicionar los balones al salir de la ventana
    for target in targets:
        if not inside(target):
            target.x = 200  # Reposicionar el balón a la derecha de la pantalla
            target.y = randrange(-150, 150)  # Cambiar la posición vertical aleatoriamente

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
