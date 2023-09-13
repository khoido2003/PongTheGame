from turtle import Turtle


class Separator(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -300)  # Adjust the Y-coordinate to the desired position
        self.pendown()
        self.setheading(90)  # Set the heading to draw a vertical line
        self.pensize(5)  # Adjust the line thickness if needed
        self.forward(600)  # Adjust the length of the line as needed
        self.hideturtle()
