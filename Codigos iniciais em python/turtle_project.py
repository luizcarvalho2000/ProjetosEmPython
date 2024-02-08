import turtle as t
import colorsys

t.bgcolor("black")
t.tracer(100)
t.speed(5)
h = 0.0


for i in range(250):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.01
    t.fillcolor(c)
    t.begin_fill()
    t.fd(i)
    t.lt(100)
    t.circle(30)
    for j in range(2):
        t.fd(i*j)
        t.lt(109)
    t.end_fill()
t.done()