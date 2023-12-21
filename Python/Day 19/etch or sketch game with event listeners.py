from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_up():
    tim.right(90)
    tim.forward(10)


def move_down():
    tim.right(180)
    tim.forward(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_up, "w")
screen.onkey(move_left, "a")
screen.onkey(move_down, "s")
screen.onkey(move_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
