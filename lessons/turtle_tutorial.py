"""Turtle tutorial."""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-150, -90)
leo.pendown()

colormode(255)
leo.color(99, 204, 250)

leo.begin_fill()
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")
leo.end_fill()


i: int = 0 
while (i < 6):
    leo.forward(300)
    leo.left(120)
    i = i + 1

bob: Turtle = Turtle()

bob.penup()
bob.goto(45, 60)
bob.pendown()

bob.color(99, 204, 250)

bob.begin_fill()
bob.pencolor("red")
bob.fillcolor(140, 37, 37)
bob.color("brown", "yellow")
bob.end_fill()


bob.speed(20)
bob.hideturtle()

side_length: int = 300
side_length = int(side_length * 0.97)
i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

done()
