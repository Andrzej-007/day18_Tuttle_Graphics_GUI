import random
import turtle as test_mod   # test_mod is a free name whatever I chose
# from turtle import Turtle

jag = test_mod.Turtle()
jag.shape("turtle")
jag.color("green", "red")

pen_color_list = ['red', 'blue', 'green', 'brown', 'yellow', 'LightSeaGreen' , 'medium violet red']


def draw_shape(n_side):
    angle = 360 / n_side
    for _ in range(n_side):
        val = round(jag.heading(), 2)
        jag.forward(100)
        jag.write(str(val))
        jag.right(angle)

for n in range(3,11):
    jag.pencolor(random.choice(pen_color_list))
    draw_shape(n)

screen = test_mod.Screen()
screen.exitonclick()

# val = turtle.heading()
#
# # write it
# turtle.write(str(val))