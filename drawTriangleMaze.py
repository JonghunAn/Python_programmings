import turtle
from random import *

color = ["red","blue","green","black"]
k=0

turtle.setup(500,500)
t = turtle.Pen()
t.width(3)
t.speed(8)
t.shape("turtle")

for i in range(0,200,8):
    t.pencolor(color[k%4])
    k+=1
    t.forward(i)
    t.left(120)