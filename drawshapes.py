from turtle import *
import math

# Name your Turtle.
t = Turtle()

usercolor = input('Enter a simple color: ')



# Set Up your screen and starting position.

setup(500,300)
x_pos = 0
y_pos = 0
t.penup()
t.setposition(x_pos, y_pos)

### Write your code below:

t.pendown()
t.pencolor(usercolor)


for loop in range(4):
    t.right(90)
    t.forward(100)



# Name your Turtle.




# Set Up your screen and starting position.

x_pos = 50
y_pos = -100
t.penup()
t.setposition(x_pos, y_pos)

### Write your code below:

t.pendown()

for loop in range(3):
    t.right(120)
    t.back(100)

x_pos= 100
y_pos=100
t.penup()
t.setposition(x_pos, y_pos)

sides=input('Enter and amount of sides: ')

t.pendown()

x=int(sides)

for loop in range(x):
    t.right(360/x)
    t.forward(100)



exitonclick()
