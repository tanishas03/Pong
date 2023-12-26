from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.move_speed *= 0.9
    #collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        ball.move_speed *= 0.9

    #ball misses R_paddle
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        ball.move_speed = 0.1

    # ball misses L_paddle
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
        ball.move_speed = 0.1

    if scoreboard.r_score == 1 or scoreboard.l_score == 1:
        scoreboard.clear()
        scoreboard.write("GAME OVER", align="center", font=("Courier", 60, "normal"))
        game_is_on = False

screen.exitonclick()
