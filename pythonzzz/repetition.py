from turtle import *
side_length = 50
angle = input("What shape?")
if angle == "square":
    angle = 90
    side = 4
if angle == "triangle":
        angle = 120
        side = 3
pendown()
for i in range(side):
    pencolor("red")
    forward(side_length)
    left(angle)
penup()
forward(60)
for i in range(side):
    pendown()
    pencolor("blue")
    forward(side_length)
    left(angle)
penup()
forward(60)
for i in range(side):
    pendown()
    pencolor("purple")
    forward(side_length)
    left(angle)
