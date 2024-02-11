import turtle

t = turtle.Pen()
t.speed(0)
t.shape("turtle")
turtle.bgcolor("black")

colors = ["red", "yellow", "green", "blue", "orange", "purple", "pink"]

for x in range(360):
    t.pencolor(colors[x%7])
    t.forward(50/ 2*4)
    t.left(10*5)

turtle.done()

