import turtle
import figures
pen = turtle.Turtle()
def draw_square(length):
    for i in range(4):
        pen.forward(length)
        pen.right(90)