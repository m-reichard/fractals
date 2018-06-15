"Sierpinski Triangle"

import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor("ivory")

COLORS = ["#ffccb3", "#ffbb99", "#ffaa80", "#ff9966", "#ff884d"]


def init_turtle(t):
    t.hideturtle()
    t.speed(30)
    t.up()
    t.goto(-200,-100)
    t.down()

def triangle(length):
    t.fillcolor(random.choice(COLORS))
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()

def sierpinski(depth, length):
    if depth == 0:
        triangle(length)
        return
    else:
        for i in range(3):
            t.forward(length)
            t.left(120)
            sierpinski(depth-1, length/2)

init_turtle(t)   
sierpinski(5, 400)
wn.exitonclick()