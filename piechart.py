# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 2
# Author: Truong Thanh Long (s3818775)
# Created date: 08/08/2020
# Last modified date: 09/08/2020

import turtle
from itertools import cycle


a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = float(input('d: '))


# first setup
colors = cycle(['yellow', 'green', 'red', 'cyan'])
radius = 200
label_percent = radius * 0.4 
fontsize = 18
fonts = ("Ariel", fontsize)
total = a + b + c + d
percennt = ((round((a / total) * 100),2), (round((b / total) * 100),2), (round((c / total) * 100),2), (round((d / total) * 100),2))

#draw piechart
s = turtle.Turtle()
s.penup()
s.sety(-radius)
s.pendown()

for p in a, b, c, d:
    s.fillcolor(next(colors))
    s.begin_fill()
    s.circle(radius, p * 360 / total)
    position = s.position()
    s.goto(0, 0)
    s.end_fill()
    s.setposition(position)


# The labels
s.penup()
s.goto(0,-100)

for label in percennt:
    s.circle(label_percent, p * 360 / total * 2 )
    s.write(label, align="center", font=fonts)
    s.circle(label_percent, p * 360 / total * 2 )


win = turtle.Screen()

win.exitonclick()