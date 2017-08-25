import turtle
import math

def fractal(turtle, length, order, first):
    global colors
    global originalOrder
    if first:
        height = int(math.sqrt((length**2)-((length/2.0)**2)))
        turtle.penup()
        turtle.goto(0, height/2.0)
        turtle.pendown()

    color = colors[order%6]
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(60)
    turtle.end_fill()

    if order > 1:
        newLength = length/2
        fractal(turtle, newLength, order-1, False)
        turtle.penup()
        turtle.right(60)
        turtle.forward(newLength)
        turtle.left(60)
        turtle.pendown()

        fractal(turtle, newLength, order-1, False)
        turtle.penup()
        turtle.right(180)
        turtle.forward(newLength)
        turtle.right(180)
        turtle.pendown()

        fractal(turtle, newLength, order-1, False)
        turtle.penup()
        turtle.left(60)
        turtle.forward(newLength)
        turtle.right(60)
        turtle.pendown()

#--------------------------
# def draw_initials(turtle, length):
#     turtle.speed(10)
#     height = int(math.sqrt((length**2)-((length/2.0)**2)))
#     newLength = int(height/2)
#     turtle.penup()
#     turtle.home()
#     turtle.right(90)
#     turtle.forward(newLength/8)
#     turtle.pensize(newLength/32)
#
#     # the T
#     turtle.pendown()
#     turtle.color('yellow')
#     turtle.right(90)
#     turtle.forward(newLength/4)
#     turtle.right(180)
#     turtle.forward(newLength/8)
#     turtle.right(90)
#     turtle.forward(newLength/4)
#
#     # to the S
#     turtle.penup()
#     turtle.home()
#     turtle.right(90)
#     turtle.forward(newLength/8)
#     turtle.left(90)
#     turtle.forward(3*(newLength/16))
#
#     # the S
#     turtle.pendown()
#     turtle.right(180)
#     turtle.forward(newLength/8)
#     turtle.left(45)
#     turtle.forward(3*(newLength/64))
#     turtle.left(45)
#     turtle.forward(2*(newLength/64))
#     turtle.left(45)
#     turtle.forward(3*(newLength/64))
#     turtle.left(45)
#
#     turtle.forward(3*(newLength/32))
#     turtle.right(45)
#     turtle.forward(newLength/16)
#     turtle.right(45)
#     turtle.forward(newLength/16)
#     turtle.right(45)
#     turtle.forward(newLength/16)
#     turtle.right(45)
#     turtle.forward(newLength/8)

#--------------------------

side_length = int(input("Enter the desired side length > "))
originalOrder = int(input("Enter the order number > "))
window = turtle.Screen()
window.bgcolor('#993300')

bud = turtle.Turtle()
bud.color("black")
bud.shape("classic")
bud.speed(10)
colors = ['#003366', '#003300', '#663300', '#993333', '#660066', '#000066']
#colors = ['#66ccff', '#cc0099', '#ffff66', '#ff00ff', '#33cccc', '#ffff99']
#colors = ['#66ccff', '#66ccff']  #ff6600

fractal(bud, side_length, originalOrder, True)
draw_initials(bud, side_length)

window.exitonclick()
