from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            if data:
                self.high_score = data.read()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    def add_point(self):
        self.score += 1
        if self.score >= int(self.high_score):
            self.high_score = self.score
            with open("../data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_scoreboard()
