import random
import turtle as test_mode

test_mode.colormode(255)

mich = test_mode.Turtle()
mich.shape('turtle')


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_spiral(deviation):
    set_head = 0
    mich.speed('fastest')
    mich.width(1)
    for _ in range(int(360/ deviation)):
        mich.pencolor(random_color())
        mich.setheading(set_head)
        mich.circle(100)
        set_head += deviation



# set_head = 0
# mich.speed('fastest')
# mich.width(1)
# for i in range(0, 36):
#     mich.pencolor(random_color())
#     mich.setheading(set_head)
#     mich.circle(100)
#     set_head += 10


draw_spiral(5)

screen = test_mode.Screen()
screen.exitonclick()
