# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 2
# Author: Truong Thanh Long (s3818775)
# Created date: 30/07/2020
# Last modified date: 09/08/2020

import turtle

#draw UK flag
def UKK():
    ##UK

    win = turtle.Screen()
    win.bgcolor("blue")
    win.setup(600, 300)

    uk = turtle.Turtle()
    uk.speed(0)

    ## X LINE
    # x line (1)
    uk.up()
    uk.goto(-300, 150)
    uk.down()
    uk.width(60)
    uk.color("white")

    uk.right(25)
    uk.forward(670)
    uk.left(25)

    # x line (2)
    uk.penup()
    uk.goto(300, 150)
    uk.pendown()

    uk.right(155)
    uk.forward(670)
    uk.left(155)

    # x red line(top)
    uk.up()
    uk.goto(-300, 140)
    uk.down()
    uk.color('red')
    uk.width(20)

    uk.right(25)
    uk.forward(320)
    uk.left(25)

    uk.up()
    uk.goto(300, 160)
    uk.down()

    uk.right(155)
    uk.forward(320)
    uk.left(155)

    # x red line(bot)
    uk.up()
    uk.goto(-300, -140)
    uk.down()

    uk.right(-25)
    uk.forward(320)
    uk.left(-25)

    uk.up()
    uk.goto(300, -120)
    uk.down()

    uk.right(-155)
    uk.forward(320)
    uk.left(-155)

    ## + LINE
    # + line(1)
    uk.up()
    uk.goto(0, 160)
    uk.down()
    uk.color('white')
    uk.width(100)

    uk.right(90)
    uk.forward(300)
    uk.left(90)

    # + line(2)
    uk.up()
    uk.goto(-300, 10)
    uk.pendown()

    uk.forward(600)

    # + red line(1)
    uk.up()
    uk.goto(0, 160)
    uk.down()
    uk.color('red')
    uk.width(60)

    uk.right(90)
    uk.forward(300)
    uk.left(90)

    # + red line(2)
    uk.up()
    uk.goto(-300, 10)
    uk.pendown()

    uk.forward(600)

    win.exitonclick()



    # Draw Australia flag
def auu():
    wn = turtle.Screen()
    wn.setup(800, 400)
#setup seven star
    def draw7star(x, y, size, color): 
        t = turtle.Turtle()
        t.speed(0)
        t.color(color)
        count = 0
        angle = 155
        t.ht()
        t.pu()
        t.setposition(x, y)
        t.pd()
        t.ht()
        t.right(25)
        t.begin_fill()
        t.speed(0)
        while count <= 5:
            t.forward(size)
            t.right(angle)
            count += 1
        t.end_fill()
        t.ht()
#setup five star
    def draw_star(x, y, size, color):
        t = turtle.Turtle()
        t.speed(0)
        t.color(color)
        count = 0
        angle = 144
        t.ht()
        t.pu()
        t.setposition(x, y)
        t.pd()
        t.ht()
        t.begin_fill()
        t.speed(0)
        while count <= 5:
            t.forward(size)
            t.right(angle)
            count += 1
        t.end_fill()

    def makeRect(x, y, width, height, color):
        t = turtle.Turtle()
        t.speed(0)  
        t.ht()
        t.pu()
        t.setposition(x, y)
        t.color(color)
        t.pd()
        t.begin_fill()
        for i in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
#start draw
    def start():
        makeRect(-400, 0, 400, 200, 'navy')

        t3 = turtle.Turtle()
        t3.ht()
        t3.pu()
        t3.pensize(40)
        t3.goto(-400, 200)
        t3.pd()
        t3.color('white')
        t3.right(26.5)
        t3.forward(500)

        t3a = turtle.Turtle()
        t3a.ht()
        t3a.pu()
        t3a.pensize(13)
        t3a.goto(-400, 194)
        t3a.pd()
        t3a.color('red')
        t3a.right(26.5)
        t3a.forward(250)

        t3b = turtle.Turtle()
        t3b.ht()
        t3b.pu()
        t3b.pensize(13)
        t3b.goto(-200, 107)
        t3b.pd()
        t3b.color('red')
        t3b.right(26.5)
        t3b.forward(250)

        t4 = turtle.Turtle()
        t4.ht()
        t4.pu()
        t4.pensize(40)
        t4.goto(-400, 0)
        t4.pd()
        t4.color('white')
        t4.left(26.5)
        t4.forward(500)

        t4a = turtle.Turtle()
        t4a.ht()
        t4a.pu()
        t4a.pensize(13)
        t4a.goto(-395, 0)
        t4a.pd()
        t4a.color('red')
        t4a.left(26.5)
        t4a.forward(250)

        t4b = turtle.Turtle()
        t4b.ht()
        t4b.pu()
        t4b.pensize(13)
        t4b.goto(-190, 110)
        t4b.pd()
        t4b.color('red')
        t4b.left(26.5)
        t4b.forward(250)

    start()
    makeRect(-400, -200, 800, 200, 'navy')
    makeRect(0, 0, 400, 200, 'navy')
    makeRect(-240, 0, 80, 210, 'white')
    makeRect(-400, 67.5, 400, 67.5, 'white')
    makeRect(-420, -220, 20, 420, 'white')
    makeRect(-420, 202, 460, 40, 'white')

        # UK flag(red line)
    makeRect(-400, 78, 400, 45, 'red')
    makeRect(-222, 0, 45, 200, 'red')
    # 5 star
    draw_star(225, 0, 30, 'white')
    # 7 star(big = 100, small = 50)(left to right)
    draw7star(-250, -50, 100, 'white')

    draw7star(70, 40, 50, 'white')

    draw7star(170, 160, 50, 'white')

    draw7star(250, 100, 50, 'white')
    # star at bottom
    draw7star(170, -140, 50, 'white')

    wn.exitonclick()



# user input
while True:
    flagg = int(input("***************************\n1. Draw UK flag\n2. Draw Australia flag\n3. Exit\nEnter an option (1/2/3): "))
    print()

    if flagg == 1:
        UKK()
    elif flagg == 2:
        auu()
    elif flagg == 3:
        print("Program exits. Have a nice night!")
        break
    else:
        print('the fuck')



