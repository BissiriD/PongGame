from turtle import Screen, Turtle
from paddle_game import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

sc = Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(800, 600)
sc.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

sc.listen()
sc.onkey(r_paddle.go_up, "Up")
sc.onkey(r_paddle.go_down, "Down")
sc.onkey(l_paddle.go_up, "w")
sc.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball out of bounds
    if ball.xcor() > 380:
        ball.goto(0, 0)  # Reset the ball's position to the center
        ball.bounce_x()
        score.l_score()

    if ball.xcor() < -380:
        ball.goto(0, 0)  # Reset the ball's position to the center
        ball.bounce_x()
        score.r_score()

sc.exitonclick()


