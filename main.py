import random
import turtle
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ")

outline_colors = ["red", "orange", "goldenrod", "green", "blue", "purple", "palevioletred"]
fill_colors = ["#FFB09F", "#FFE09F", "#EEFF9F", "#9FFFB0", "#9FEEFF", "#B09FFF", "#FF9FBE"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(outline_colors[turtle_index], fill_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost... The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
