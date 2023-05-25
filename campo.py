from turtle import Turtle

class Campo(Turtle):
    def __init__(self, x, y):
        super(Campo, self).__init__()
        self.penup()
        self.pensize(4)
        self.goto(x, y)
        self.pendown()
        self.goto(x, -y)
        self.goto(-x, -y)
        self.goto(-x, y)
        self.goto(x, y)
        self.hideturtle()