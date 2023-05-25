from turtle import Turtle
from random import randint, randrange

class Maca(Turtle):
    def __init__(self):
        super(Maca, self).__init__()        
        self.color('red')
        self.shape('circle') 
        self.penup()       
        self.nova_maca()
        
        
    def nova_maca(self):
        x = randrange(-260, 260, 20)
        y = randrange(-260, 260, 20)
        self.goto(x, y)
        self.penup()
        
        
    