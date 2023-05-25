from turtle import Screen, write

from campo import Campo
from cobra import Cobra
from maca import Maca
from pontuacao import Pontuacao
import time

tela = Screen()

tela.title('Jogo da Cobrinha')
tela.setup(600, 620)
tela.tracer(0)
#tela.bgcolor('beige')

campo = Campo(280, 280)
cobra = Cobra()
maca = Maca()
pontuacao = Pontuacao()

tela.listen()
tela.onkey(cobra.mover_direita, 'Right')
tela.onkey(cobra.mover_esquerda, 'Left')
tela.onkey(cobra.mover_cima, 'Up')
tela.onkey(cobra.mover_baixo, 'Down')

jogo_on = True

while jogo_on:
    time.sleep(0.2)
    cobra.mover()
    #print(f'Cx {cobra.cabeca.xcor()} / Mx {maca.xcor()}')
    #print(f'Cy {cobra.cabeca.ycor()} / My {maca.ycor()}')
    
    # comendo a maça
    if abs(cobra.cabeca.xcor() - maca.xcor()) < 10 and abs(cobra.cabeca.ycor() - maca.ycor()) < 10:
        cobra.novo_seguimento((cobra.corpo[-1].xcor(), cobra.corpo[-1].ycor()))
        maca.nova_maca()
        pontuacao.nova_pontuacao()
        
        
    # GAME OVER
    if abs(cobra.cabeca.xcor()) >= 280 or abs(cobra.cabeca.ycor()) >= 280:
        jogo_on =False
        write(arg='GAME OVER', align='center', font=('arial', 40, 'bold'))
    
    
    tela.update()

tela.exitonclick()