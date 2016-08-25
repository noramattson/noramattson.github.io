from turtle import *
def all(side_number, side_length, pen_color):
    pencolor(pen_color.lower())
    pendown()
    if side_number == "circle":
        circle(side_length)
    for i in range (side_number):
        forward(side_length)
        right(180-((side_number-2)*180/side_number))
all(74, 50, "purple")
# side_number = int(input("How many sides?"))
# side_length = int(input("Choose side length?"))
# pen_color = input("Choose pen color.")
