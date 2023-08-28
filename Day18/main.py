# from turtle import Turtle, Screen
#
# tinny_the_turtle = Turtle()
# tinny_the_turtle.shape("turtle")
# tinny_the_turtle.color("red")
#
# tinny_the_turtle.forward(100)
# tinny_the_turtle.right(90)
#
# screen = Screen()
# screen.exitonclick()
import random
# from turtle import Turtle, Screen
#
# tinny_the_turtle = Turtle()
# tinny_the_turtle.shape("turtle")
# tinny_the_turtle.color("red")
#
# for _ in range(0,4):
#     tinny_the_turtle.forward(100)
#     tinny_the_turtle.left(90)
#
# screen = Screen()
# screen.exitonclick()

# from turtle import *
# tim = Turtle()
#
# import turtle as t
# tim = t.Turtle()

# import heroes
# print(heroes.gen())


# from turtle import Turtle, Screen
#
# tinny_the_turtle = Turtle()
#
# for _ in range(15):
#     tinny_the_turtle.forward(10)
#     tinny_the_turtle.penup()
#     tinny_the_turtle.forward(10)
#     tinny_the_turtle.pendown()
#
# screen = Screen()
# screen.exitonclick()



# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3,10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)


# from turtle import Turtle
#
# tim = Turtle()
#
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# direction = [0,90,180,270]
# tim.pensize(17)
# tim.speed(0)
#
# for _ in range(0, 200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# mytouple = (1,5,2,5,8)
# print(mytouple[2])
# #mytouple[2] = 10


# import turtle as t
#
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color =  (r, g, b)
#     return random_color
#
# direction = [0,90,180,270]
# tim.pensize(17)
# tim.speed(0)
#
# for _ in range(0, 200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))







# import turtle as t
#
# tim = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# tim.speed("fastest")
#
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# draw_spirograph(5)
# screen = t.Screen()
# screen.exitonclick()


#import colorgram
# colours = colorgram.extract("image.jpg", 30)
# rgb_colours = []
# for color in colours:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colours.append(new_color)
#
# print(rgb_colours)









import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed('fastest')
tim.penup()
tim.hideturtle()
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()








