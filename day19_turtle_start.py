from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the rave? Enter the colour:..\n'blue', 'red', 'green', 'brown', 'yellow', 'LightSeaGreen'")
print(user_bet)

color_list = ['blue', 'red', 'green', 'brown', 'yellow', 'LightSeaGreen' ]
all_turtle =[]
pos_y = -100

if user_bet:
    is_race_on = True


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-280, y=pos_y)
    pos_y += 50
    all_turtle.append(new_turtle)

while is_race_on:

    for single_turtle in all_turtle:
        if single_turtle.xcor() > 260:
            is_race_on = False
            winning_color = single_turtle.pencolor()
            if winning_color == user_bet:
                print(f' you WIN  turtle color winner {winning_color} ')
            else:
                print(f' you LOST  turtle color winner {winning_color} ')

        single_turtle.forward(random.randint(0,10))


screen.exitonclick()