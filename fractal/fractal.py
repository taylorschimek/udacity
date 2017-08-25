import turtle
import math

trips = 0

def fractal(turtle, length, order, first):
    global trips
    trips += 1
    print("trips = {}, length = {}".format(trips, length))
    #print("fractal called {} {}".format(first, order))
    if first:
        height = int(math.sqrt((length**2)-((length/2.0)**2)))
        turtle.penup()
        turtle.goto(0, height/2.0)
        turtle.pendown()
    print('-'*30)
    turtle.right(60)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(60)



    #if (order > 1):
    if (first):
        x = 2
    else:
        x = order
    for i in range(1, x):
        newLength = length/(2**i)
        print("{} first on {}-{}".format(trips,order,i))
        fractal(turtle, newLength, order-i, False)
        turtle.penup()
        turtle.right(60)
        turtle.forward(newLength)
        turtle.left(60)
        turtle.pendown()
        print("{} second on {}-{}".format(trips,order,i))
        fractal(turtle, newLength, order-i, False)
        turtle.penup()
        turtle.right(180)
        turtle.forward(newLength)
        turtle.right(180)
        turtle.pendown()
        print("{} third on {}-{}".format(trips,order,i))
        fractal(turtle, newLength, order-i, False)
        turtle.left(60)
        turtle.forward(newLength)
        turtle.right(60)







            # for j in range(1, 3**i):
            #     fractal(turtle, newLength, 1, False)
            #     turtle.penup()
            #     turtle.right(60)
            #     turtle.forward(newLength)
            #     turtle.left(60)
            #     turtle.pendown()

window = turtle.Screen()
window.bgcolor("brown")

bud = turtle.Turtle()
bud.color("lightblue")
bud.shape("classic")
bud.speed(10)

fractal(bud, 400, 4, True)

window.exitonclick()
