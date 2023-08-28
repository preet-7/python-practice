# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def mov_forward():
#     tim.forward(10)
#
#
# screen.listen()
# screen.onkey(key="space", fun=mov_forward)
# screen.exitonclick()
import random
import turtle
# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
#
# def mov_forward():
#     tim.forward(10)
#
#
# def mov_backward():
#     tim.backward(10)
#
#
# def mov_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def mov_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#
#
# screen.listen()
# screen.onkey(mov_forward, "w")
# screen.onkey(mov_backward, "s")
# screen.onkey(mov_left, "a")
# screen.onkey(mov_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()








from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner! ")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()




