import turtle

#   following Python Turtle Graphics Tutorial #1 - Introduction
#   https://www.youtube.com/watch?v=p7CiFhiTdvY

# basic turtle.Turtle() methods

tim = turtle.Turtle()   #creates new turtle object based on Turtle class
tim.color('red')
tim.pensize(5)          #changes thickness of line
tim.shape('turtle')     #multiple different options for shapes, look it up

#   weird note: turtle GUI closes automatically after running in Visual Studio but not in Idle?

tim.forward(100)
tim.left(90)
tim.penup()
tim.forward(100)
tim.right(90)
tim.pendown()
tim.color('green')
tim.forward(100)

dave = turtle.Turtle()
dave.color('blue')
dave.pensize(5)
dave.shape('turtle')

dave.backward(100)
dave.speed(1)

for i in range(0,10):
    dave.forward(100)
    dave.backward(100)

richard=turtle.Turtle()