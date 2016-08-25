# START WRITING YOUR CODE HERE
from turtle import *
side_length = 100
pendown()
pencolor("purple")
def square():
    for i in range(4):
        forward(side_length)
        right(90)
def triangle():
    for i in range(3):
        forward(side_length)
        right(120)
def circ():
        circle(50)
def idk():
    for i in range(43):
        forward(side_length)
        right(59)
        forward(side_length)
        left(34)
        forward(side_length)
        left(231)
choose = input("choose shape")
if choose == "triangle":
    triangle()
elif choose == "square":
    square()
elif choose == "circle":
    circ()
else:
    idk()
