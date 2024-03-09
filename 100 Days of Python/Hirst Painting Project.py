import turtle as turtle_module
import random

# import colorgram
#
# # Extract 50 colors from an image.
# colors = colorgram.extract('Hirst.jpg', 50)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(249, 248, 245), (250, 246, 248), (241, 248, 245), (239, 244, 249), (236, 225, 83), (202, 5, 72),
              (198, 164, 10), (235, 51, 129), (206, 76, 11), (108, 179, 218), (219, 162, 103), (234, 225, 6),
              (30, 188, 108), (23, 106, 173), (13, 23, 64), (17, 28, 175), (213, 135, 176), (9, 185, 214),
              (205, 29, 142), (229, 168, 197), (125, 189, 162), (8, 49, 28), (37, 132, 73), (125, 219, 233),
              (67, 22, 8), (61, 11, 26), (111, 89, 211), (142, 216, 201), (190, 15, 5), (238, 63, 31), (10, 97, 52),
              (167, 183, 232), (236, 171, 158), (8, 85, 102), (253, 5, 44), (25, 44, 244), (61, 95, 10), (250, 10, 8)]

# Requirements
# 10 * 10 frame
# Distance btw each dots 50
# size of dots = 20

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

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
