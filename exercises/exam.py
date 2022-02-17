from turtle import Turtle, colormode, done 


def draw_square(a_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y."""
    a_turtle.penup()
    a_turtle.goto(x, y) 
    a_turtle.setheading(0.0)
    a_turtle.pendown()
    i: int = 0
    while i < 4:
        a_turtle.forward(width)
        a_turtle.right(90)
        i += 1

        
draw_petals(flower, -20, 20, 100)


def main() -> None:
    """The entrypoint of my scene."""
    ertle: Turtle = Turtle()
    draw_square(ertle, -5, 5, 10)
    draw_square(ertle, -10, 10, 20)
    draw_square(ertle, -15, 15, 30)
    draw_square(ertle, -20, 20, 40)
    done()