
import random
import turtle as turt_mode

colour_list = [(248, 247, 246), (244, 238, 241), (238, 246, 241),
               (234, 241, 246), (225, 158, 58), (240, 41, 115),
               (136, 27, 62), (248, 229, 63), (240, 63, 45), (180, 36, 96),
               (24, 142, 72), (56, 203, 236), (34, 133, 202), (28, 174, 134), (134, 204, 86),
               (75, 20, 72), (181, 162, 52), (208, 133, 165), (200, 55, 37), (238, 163, 192)]

turt_mode.colormode(255)
screen = turt_mode.Screen()
screen.setup(width=1500, height=900, startx=0, starty=0)
screen.screensize(1500, 900)
mich = turt_mode.Turtle()


def draw_line():

    for _ in range(10):
        random_color = random.choice(colour_list)
        mich.dot(20,random_color )
        # mich.pencolor(random_color)
        # mich.width(20)
        # mich.pendown()
        # mich.forward(1)
        # mich.penup()
        mich.forward(50)

def main_board():
    pos_x = -200
    pos_y = -200
    mich.speed("fastest")
    mich.hideturtle()
    # y_pos = -200

    for _ in range(10):
        mich.penup()
        mich.setx(pos_x)
        mich.sety(pos_y)
        # mich.penup()
        # mich.goto(-200, y_pos)
        draw_line()
        pos_y += 50
        # y_pos += 50
        # mich.penup()
        # mich.goto(-200, y_pos)

main_board()
screen.exitonclick()

# for i in range(10):
#     random_color = random.choice(colour_list)
#     mich.pencolor(random_color)
#     mich.width(20)
#     mich.pendown()
#     mich.forward(1)
#     mich.penup()
#     mich.forward(50)
# mich.goto(-200, -150)
# for i in range(10):
#     random_color = random.choice(colour_list)
#     mich.pencolor(random_color)
#     mich.width(20)
#     mich.pendown()
#     mich.forward(1)
#     mich.penup()
#     mich.forward(50)










