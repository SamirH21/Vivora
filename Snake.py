"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
import random
from freegames import square, vector
#Se importan todas las librerías necesarias


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
#Define la posición inicial de cada uno


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
#Cambia la dirección en que se mueve la serpiente


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190
#Te muestra que la serpiente está en el rango de tablero


def move():
    "Move snake forward one segment."
#Esta función avanza a la serpiente una posición
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
#Marca sí la serpiente salió del rango
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
#Indica si la serpiente comió
    clear()

    for body in snake:
        square(body.x, body.y, 9, colorv)

    square(food.x, food.y, 9, colorc)
    update()
    ontimer(move, 100)
#Define el cuerpo de la serpiente


setup(420, 420, 370, 0) #Define dimensiones del tablero
hideturtle() #Esconde el cursor
tracer(False) #Maneja la animación
listen()# Activda y desactiva la tortuga
colors=["orange","green", "blue", "violet", "pink"] #Se define lista de colores
colorv=random.choice(colors) #color vibora
colorc=random.choice(colors) #color comida, ambos aleatorios.
if colorv==colorc: #Esta función evita, que los colores salgan igual.
    colorc=random.choice(colors)

onkey(lambda: change(10, 0), 'Right')#Hacen que al presiona la tecla, se cumpla una función
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')


move()
done()
