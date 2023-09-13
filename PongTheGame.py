# FINAL VERSION USING CLASS

import time
from turtle import Screen
from Separator import Separator
from Paddle import Paddle
from Ball import Ball
from ScoreBoard import ScoreBoard

# SET UP THE SCREEN
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turn off the animation in initial


############################

# Create instances from imported Class
separator = Separator()

# Create a separator between two players

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create ball
ball = Ball()

# Create ScoreBoard
score_board = ScoreBoard()

###############################

# Event listener
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


################################

# Acvtive the game
game_is_on = True
while game_is_on:
    # Slow down the ball on initial but faster later on
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Ball need to bounce back
        ball.bounce_y()

    # Detect collision with r_paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect when right paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # Detect when left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()
#################################

# Prevent screen exit
screen.exitonclick()

####################################################


# FIRST VERSION CREATE PADDLE WITHOUT USING CLASS

# from turtle import Screen, Turtle

# # SET UP THE SCREEN
# screen = Screen()
# screen.bgcolor("black")
# screen.setup(width=800, height=600)
# screen.title("Pong")
# screen.tracer(0)  # Turn off the animation in initial

# # Create a line separator
# separator = Turtle()
# separator.color("white")
# separator.penup()
# separator.goto(0, -300)  # Adjust the Y-coordinate to the desired position
# separator.pendown()
# separator.setheading(90)  # Set the heading to draw a vertical line
# separator.pensize(5)  # Adjust the line thickness if needed
# separator.forward(600)  # Adjust the length of the line as needed
# separator.hideturtle()


# # SET UP PADDLE
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)


# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)


# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")

# game_is_on = True
# while game_is_on:
#     screen.update()

# screen.exitonclick()
