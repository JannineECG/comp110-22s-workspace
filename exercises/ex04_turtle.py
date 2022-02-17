"""Valentines Flower."""

__author__ = "730470181"

from turtle import Turtle, colormode, tracer, update, done 

colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    flower: Turtle = Turtle()
    colormode(255)
    flower.speed(0)
    tracer(0, 0)
    draw_petal(flower, -50, 10, 100)
    draw_petal(flower, -60, -10, 120)
    draw_core(flower, -85, 50, 170)
    draw_core(flower, -75, 60, 150)
    draw_core(flower, -65, 70, 130)
    draw_core(flower, -55, 80, 110)
    draw_core(flower, -45, 90, 90)
    draw_core(flower, -35, 100, 70)
    draw_core(flower, -25, 110, 50)
    draw_core(flower, -15, 120, 30)
    draw_core(flower, -5, 130, 10)
    draw_stem(flower, -20, -10, 50, 300)
    draw_leaf(flower, 30, -100, 100)
    draw_leaf(flower, 15, -250, 100)
    update()
    done()


def draw_petal(a_petal: Turtle, x: float, y: float, width: float) -> None:
    """The main componenet of a flower, the petals."""
    a_petal.penup()
    a_petal.goto(x, y)
    a_petal.setheading(0.0)
    a_petal.pendown()
    i: int = 0
    while i < 8:
        a_petal.begin_fill()
        a_petal.pencolor('red')
        a_petal.fillcolor('red')
        a_petal.forward(width)
        a_petal.left(45)
        i += 1
        a_petal.end_fill()


def draw_core(a_core: Turtle, x: float, y: float, width: float) -> None:
    """The core, where pollen is located."""
    a_core.penup()
    a_core.goto(x, y)
    a_core.setheading(0.0)
    a_core.pendown()
    i: int = 0
    while i < 4:
        a_core.begin_fill()
        a_core.pencolor('brown')
        a_core.fillcolor('brown')
        a_core.forward(width)
        a_core.left(90)
        a_core.end_fill()
        i += 1


def draw_stem(a_stem: Turtle, x: float, y: float, width: float, length: float) -> None:
    """The stem of the flower."""
    a_stem.penup()
    a_stem.goto(x, y)
    a_stem.setheading(0.0)
    a_stem.pendown()
    i: int = 0
    while i < 2:
        a_stem.begin_fill()
        a_stem.pencolor('green')
        a_stem.fillcolor('green')
        a_stem.forward(width)
        a_stem.right(90)
        a_stem.forward(length)
        a_stem.right(90)
        a_stem.end_fill()
        i += 1


def draw_leaf(a_leaf: Turtle, x: float, y: float, width: float) -> None:
    """The leaves that connect to the stem."""
    a_leaf.penup()
    a_leaf.goto(x, y)
    a_leaf.setheading(0.0)
    a_leaf.pendown()
    i: int = 0
    while i < 2:
        a_leaf.begin_fill()
        a_leaf.pencolor('green')
        a_leaf.fillcolor('green')
        a_leaf.circle(width, 70)
        a_leaf.left(110)
        a_leaf.end_fill()
        i += 1


if __name__ == "__main__":
    main()
