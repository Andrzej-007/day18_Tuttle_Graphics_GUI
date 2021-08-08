from turtle import Turtle , Screen

jag = Turtle()
jag.shape("turtle")
jag.color("green", "red")


qw = range(3,8)
base_angle = 360
for n in qw:
    for i in range(n):
        jag.forward(100)
        calc_angle = base_angle / n
        jag.right(calc_angle)

# qw = range(3,8)
# base_angle = 360
#
# for i in qw:
#     print(i)

# for i in range(15):
#     jag.forward(5)
#     jag.penup()
#     jag.forward(20)
#     jag.pendown()

screen = Screen()
screen.exitonclick()


# import turtle
# tim = turtle.Turtle()