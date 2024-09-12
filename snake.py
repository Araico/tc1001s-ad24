"Snake Game - Jaime Zayat"
from random import randrange, choice
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Definir lista de colores excluyendo el rojo
colors = ['blue', 'green', 'purple', 'yellow', 'orange']

# Seleccionar colores diferentes para la serpiente y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])


def change(x, y):
    aim.x = x
    aim.y = y


def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = choice(directions)
    new_food_pos = food + move_direction

    if inside(new_food_pos):
        food.move(move_direction)


def move():
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red")
        update()
        return

    snake.append(head)

    if head == food:
        print("Snake:", len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    move_food()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "Down")
move()
done()
