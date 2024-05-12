from turtle import Screen
import turtle as t
import random

tim=t.Turtle()
t.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    col=(r,g,b)
    return col
tim.pensize(20)
tim.speed(10)
x=int(input("Enter the value of push"))
while True:
    dice= random.randint(1,2)
    tim.color(random_color())
    tim.forward(25)
    tim.left(90)
    tim.forward(25+x)
    x=x+5
Screen().exitonclick()
