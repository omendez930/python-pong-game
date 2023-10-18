from turtle import Turtle

COLOR = 'white'
class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.speed(0)
        self.color(COLOR)
        self.shapesize(stretch_wid=5, stretch_len= 1)
        self.penup()
        self.goto(x,y)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

