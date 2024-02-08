from turtle import forward, left, right, circle, done, tracer, hideturtle, width, speed
import colorsys 
from turtle import Screen, Turtle
import colorsys 

speed(0)
hideturtle()
screen = Screen()
screen.bgcolor('black')
tracer(5)
width(2)
h = 0.001
from turtle import color
for i in range(90):
    right(240)
    forward(100)
    right(60)
    forward(100)
    left(2)
    h += 0.02
done()