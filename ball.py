from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        ball = Turtle()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 15
        self.y_move = 15
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move = self.y_move * -1
        self.move_speed *= 0.95

    def bounce_x(self):
        self.x_move = self.x_move * -1
        self.move_speed *= 0.95

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
