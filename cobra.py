from turtle import Turtle
import random

class Cobra:
    POS_INICIAL = [(0,0), (0, 20)]
    VEL = 20
    DIREITA = 0
    ESQUERDA = 180
    CIMA = 90
    BAIXO = 270
    
    def __init__(self):
        self.corpo = []
        self.inicializar_cobra()
        self.cabeca = self.corpo[0]
        
    def inicializar_cobra(self):
        for pos in self.POS_INICIAL:
            self.novo_seguimento(pos)
            
    def novo_seguimento(self, pos):
        nova_cobra = Turtle()
        nova_cobra.shape('square')
        nova_cobra.color(self.sorteia_cores())
        nova_cobra.penup()
        nova_cobra.goto(pos)
        self.corpo.append(nova_cobra)

    def mover(self):
        for index in range(len(self.corpo)-1, 0, -1):
            novo_x = self.corpo[index - 1].xcor()
            novo_y = self.corpo[index - 1].ycor()
            self.corpo[index].goto(novo_x, novo_y)
        self.cabeca.forward(self.VEL)
        
    def sorteia_cores(self):
        cores = ['brown', 'black', 'blue', 'purple','pink', 'green', 'yellow', 'orange', 'gray']        
        return random.choice(cores)
        
    def mover_direita(self):
        if self.cabeca.heading() != self.ESQUERDA:
            self.cabeca.setheading(self.DIREITA)
            
    def mover_esquerda(self):
        if self.cabeca.heading() != self.DIREITA:
            self.cabeca.setheading(self.ESQUERDA)
            
    def mover_cima(self):
        if self.cabeca.heading() != self.BAIXO:
            self.cabeca.setheading(self.CIMA)
            
    def mover_baixo(self):
        if self.cabeca.heading() != self.CIMA:
            self.cabeca.setheading(self.BAIXO)