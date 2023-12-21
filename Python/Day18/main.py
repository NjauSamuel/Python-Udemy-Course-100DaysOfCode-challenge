from turtle import Turtle, Screen
import turtle

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

# for n in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy_the_turtle.color(c)
        timmy_the_turtle.forward(steps)
        timmy_the_turtle.right(30)

screen = Screen()
screen.exitonclick()
