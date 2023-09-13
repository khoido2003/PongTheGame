from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        # Players's scores
        self.l_score = 0
        self.r_score = 0

        # Create scoreboard when initial
        self.update_score_board()

    def update_score_board(self):
        # Clear the previous point
        self.clear()

        # Create/Update scroreboard of left player
        self.goto(-100, 210)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))

        # Create/Update scoreboard of right player
        self.goto(100, 210)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score_board()

    def r_point(self):
        self.r_score += 1
        self.update_score_board()
