import turtle


def draw_square(turtle, turn):
    global colors
    for a in range(0, int(360/turn)):
        color = colors[a%6]
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.right(turn)
        for i in range(0,4):
            bud.forward(200)
            bud.right(90)
            i = i + 1
        turtle.end_fill()
        a = a + turn
        print(a)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("red")
    angie.circle(100)

def draw_triangle():
    angle = turtle.Turtle()
    angle.shape("arrow")
    angle.color("blue")
    angle.left(180)
    angle.forward(200)
    angle.left(120)
    angle.forward(200)
    angle.left(120)
    angle.forward(200)


window = turtle.Screen()
window.bgcolor("gray")

bud = turtle.Turtle()
bud.shape("turtle")
bud.color("black")
bud.speed(50)
colors = ['#003366', '#003300', '#663300', '#993333', '#660066', '#000066']
draw_square(bud, 6)
#draw_circle()
#draw_triangle()

window.exitonclick()
