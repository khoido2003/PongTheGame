from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 5
        self.y_move = 5

        # Control ball spped in the game
        self.move_speed = 0.06

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

        # Faster the ball after each bounce
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)

        # Reset the ball speed to original when one player lost the game
        self.move_speed = 0.06
        self.bounce_x()
