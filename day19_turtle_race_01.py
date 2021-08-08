
from turtle import Turtle , Screen
import random


screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the rave? Enter the colour:..\n'blue', 'red', 'green', 'brown', 'yellow', 'LightSeaGreen'")
print(user_bet)

color_list = ['blue', 'red', 'green', 'brown', 'yellow', 'LightSeaGreen' ]
# screen.colormode(1)


turtle_objects =[]
pos_y = -100
for name in color_list:
    set_color = name
    name = Turtle(shape="turtle")
    name.color(set_color)
    name.penup()
    name.goto(x=-280 , y=pos_y)
    pos_y += 50
    turtle_objects.append(name)


for _ in range(150):
    for name in turtle_objects:
        if random.randint(1 , 2) == 1:
            name.forward(random.randint(0,7))
        else:
            name.backward(random.randint(0, 1))


screen.exitonclick()

