from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

R_paddle = Paddle((370, 0))
L_paddle = Paddle((-370, 0))
ball = Ball()
score = Scoreboard()

screen.listen()

screen.onkey(R_paddle.go_up, "Up")
screen.onkey(R_paddle.go_down, "Down")

screen.onkey(L_paddle.go_up, "w")
screen.onkey(L_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with the wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the paddle.
    if ball.distance(R_paddle) < 50 and ball.xcor() > 350 or ball.distance(L_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    #Score for L_paddle.
    if ball.xcor() > 400:
        score.increase_L_score()
        ball.reset_the_ball()

    #Score for R_paddle.
    if ball.xcor() < -400:
        score.increase_R_score()
        ball.reset_the_ball()

screen.exitonclick()