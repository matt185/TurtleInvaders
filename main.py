from turtle import Screen
from components.player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Invaders")
screen.tracer(0)

# create components
player = Player()

# set up key event
screen.listen()
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

game_over = False

while not game_over:
    screen.update()

screen.exitonclick()
