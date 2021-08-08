import random
import turtle as test_mod   # test_mod is a free name whatever I chose
# from turtle import Turtle

test_mod.colormode(255) # - > colormode is not in Tutle(0 class it is in tutle modul this is huge difference

jag = test_mod.Turtle()
jag.shape("turtle")
jag.color('red')

# pen_color_list = ['red', 'blue', 'green', 'brown', 'yellow', 'LightSeaGreen' , 'medium violet red']
pen_color_list = [155, 255, 122,]
MOVE = [0, 90, 180, 270,]
pen_size = 10

def random_cloor():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_shape():
    # angle = 360 / n_side
    pen_size = 10
    jag.speed('fast')
    for _ in range(1,90):
        jag.pencolor(random_cloor())
        jag.forward(50)

        random_aqngle = random.choice(MOVE)
        jag.setheading(random_aqngle)

        # jag.pencolor(random.choice(pen_color_list))
        jag.pensize(pen_size)

        # jag.right(random_aqngle)  # <-- different way to randomize the move of turtle
        # pen_size += 1


draw_shape()

screen = test_mod.Screen()
# screen.exitonclick()