from turtle import Turtle

class Pontuacao(Turtle):    
    def __init__(self) -> None:
        super(Pontuacao, self).__init__()
        self.penup()
        self.goto(-280, 290)
        self.pontuacao = 0
        self.mostrar_pontuacao()
    
    
    def nova_pontuacao(self):
        self.pontuacao += 1
        self.mostrar_pontuacao()
        
    def mostrar_pontuacao(self):
        self.clear()
        self.write(f'PONTUAÇÃO: {self.pontuacao}', align='left', font=('arial', 10, 'bold'))