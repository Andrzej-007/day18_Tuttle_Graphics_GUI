

from turtle import Turtle, Screen

mich = Turtle()
mich.shape("turtle")
mich.color('red')
mich.penup()
# mich.setx(-200)
mich.sety(-50)


jag = Turtle()
jag.shape("turtle")
jag.color('green')

screen = Screen()

def move_forwarde():
    mich.forward(10)

def move_backwars():
    mich.backward(10)

def turn_clockwise():
    mich.right(10)

def turn_anticlockwise():
    mich.left(10)

def clear_removal():
    mich.reset()

screen.listen()
screen.onkey(fun = move_forwarde, key = "w")  # <---- without brackets in the function
screen.onkey(fun = turn_clockwise, key = "d")
screen.onkey(fun = move_backwars, key = "s")
screen.onkey(fun = turn_anticlockwise, key = "a")
screen.onkey(fun = clear_removal, key = "r")
screen.exitonclick()




# W = Forward
# S = Backwars
# A = Counter-Clockwise
# D = Clockwise
# C = Clear drawing