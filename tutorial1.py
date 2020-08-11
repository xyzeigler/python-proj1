import turtle
import random
from turtle import *

#   Key Presses & Events
#   tutorial 3: https://www.youtube.com/watch?v=hPnZqWSRNZI
#   Tim working in PyCharm this time, instead of IDLE

tim = turtle.Turtle()
tim.speed(0)
tim.width(5)

colors = ['red','blue','green','purple','yellow','orange','black']

def up():
    tim.setheading(90)  #points tim upwards
    tim.forward(100)    #goes forward 100 (pixels?)

def down():
    tim.setheading(270) #points tim downwards
    tim.forward(100)    #goes forward 100 (pixels?)

def left():
    tim.setheading(180) #points tim left
    tim.forward(100)    #goes forward 100 (pixels?)

def right():
    tim.setheading(0)   #points tim right
    tim.forward(100)    #goes forward 100 (pixels?)

turtle.listen()         #listens for events

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()       #continues to look for keypresses

'''
#   tutorial 2: https://www.youtube.com/watch?v=KmziL1djFkQ

tim = turtle.Turtle()
colors = ['red','blue','green','purple','yellow','orange','black']

#   set colors for turtle
tim.color(colors[5],colors[4])  # .color(outline color, fill-in color)

#   set pen width
tim.width(5)                    # not pensize(5)?

#   fill in shape with color
tim.begin_fill()
tim.circle(50)
tim.end_fill()

tim.penup()
tim.forward(150)
tim.pendown()

tim.color('black','yellow')

tim.begin_fill()
for x in range(4):              # draw square
    tim.forward(100)
    tim.right(90)
tim.end_fill()

for x in range(5):
    randColor=random.randrange(0,len(colors))
    tim.color(colors[randColor],colors[random.randrange(0,len(colors))])
    rand1=random.randrange(-300,300)
    rand2=random.randrange(-300,300)
    tim.penup()
    tim.setpos(rand1,rand2)                   # cartesian plane
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0,80))
    tim.end_fill()

#   we could probably define our own functions for triangles, squares, etc.
#   so that we don't have to keep defining a new for-loop every time we want
#   a non-circle shape to fill

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
'''