import turtle
w = turtle.Turtle()
w.penup()
step = 20
for i in range(30):
    w.forward(step)
    w.left(24)
    w.stamp()
    step = step + 3
    
turtle.done()