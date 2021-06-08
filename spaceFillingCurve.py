from turtle import *

# set start position
penup()
goto(-250, 0)
pendown()

# set settings variables
pensize(2)
color("blue")
order = 3
size = 10


# func to draw the Koch curve
def koch_curve(order):
    if order > 0:
        for angle in [60, -120, 60, 0]:
            koch_curve(order - 1)
            left(angle)
    else:
        forward(size)


# Run the draw function
koch_curve(order)
done()
