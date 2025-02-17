from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 4
        self.y_move = 4

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_the_ball(self):
        self.goto(x=0, y=0)
        self.bounce_x()


    #THIS ONE DOESNT WORK.
    #def increase_ball_speed(self):
        # self.x_move *= 1.2
        # self.y_move *= 1.2