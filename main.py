from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Invaders")
screen.tracer(0)

game_over = False

while not game_over:
    screen.update()

screen.exitonclick()
