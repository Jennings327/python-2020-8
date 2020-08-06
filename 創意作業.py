import turtle,random
w = turtle.Turtle()
w.speed(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999)


#w.penup()
#step = 20
#for i in range(100):
 #   w.forward(step)
  #  w.left(90)
  #  w.stamp()
   # step = step + 3
 
while True:
    num = random.randint(1,6)
    if num==1:
        w.forward(30)
    elif num==2:
        w.back(30)
    elif num==3:
        w.left(90)
    elif num==4:
        w.right(90)
    elif num==5:
        w.penup()
    elif num==6:
        w.pendown()
    
    

turtle .done