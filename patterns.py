"randomized patterns"

import turtle
import random

t = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor("ivory")

COLORS = ["#ffccb3", "#ffbb99", "#ffaa80", "#ff9966", "#ff884d"]


def init_turtle(t):
    t.hideturtle()
    t.speed(10)
    t.up()
    t.goto(0,0)
    t.down()

def triangle(length):
    t.fillcolor(random.choice(COLORS))
    t.begin_fill()
    t.forward(length)
    t.left(120)
    for i in range(3):
        t.left(90)
        triangle(length-2)
    t.end_fill()


init_turtle(t)   
triangle(20)
wn.exitonclick()