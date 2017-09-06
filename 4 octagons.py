# Elena Thornton
# 9/05/17
# 4 octagons.py
# This program draws four octagons in turtle.

import turtle

# draws an octagon
def draw_a_octagon(color):
    turtle.begin_fill()
    turtle.fillcolor(color)
    for x in range(8):
        turtle.forward(90)
        turtle.left(45)
    turtle.end_fill()


def move_turtle():
    turtle.up()
    turtle.right(90)
    turtle.forward(150)
    turtle.down()

draw_a_octagon("red")

move_turtle()


draw_a_octagon("blue")

move_turtle()


draw_a_octagon("purple")

move_turtle()

draw_a_octagon("green")

# make turtle invisible
turtle.color("white")
turtle.up()


turtle.exitonclick()