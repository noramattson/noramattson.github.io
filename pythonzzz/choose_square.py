from turtle import *
choose_shape = input("Choose shape")
while choose_shape.upper() != "SQUARE" and choose_shape.upper() != "CIRCLE" and choose_shape.upper() != "TRIANGLE":
    choose_shape = input("Choose shape")
side_length = int(input("Choose side length"))
pen_color = input("Choose pen color")
move_shape = input("move shape?")
def square(pen_color):
    pencolor(pen_color.lower())
    for i in range(4):
        forward(side_length)
        right(90)
def triangle(pen_color):
    pencolor(pen_color.lower())
    for i in range(3):
        forward(side_length)
        right(120)
def circ(pen_color):
    pencolor(pen_color.lower())
    circle(side_length)
def move_it():
    while move_shape == "yes" and choose_shape.upper() == "SQUARE":
        for i in range(300):
            square(pen_color)
            speed(300)
            right(5)
    while move_shape == "yes" and choose_shape.upper() == "TRIANGLE":
        for i in range(300):
            triangle(pen_color)
            speed(300)
            right(5)
    while move_shape == "yes" and choose_shape.upper() == "CIRCLE":
        for i in range(300):
            circle(pen_color)
            speed(300)
            right(5)

pendown()
if choose_shape.upper() == "SQUARE":
    while move_shape == "no":
        square(pen_color)
    move_it()
elif choose_shape.upper() == "TRIANGLE":
    while move_shape == "no":
        triangle(pen_color)
    move_it()
else:
    while move_shape == "no":
        circ(pen_color)
    move_it()
