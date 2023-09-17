import turtle as t

def desenhar_retangulos(W,N):
    seg = W/(N+1)

    r.forward(seg-L/2)
    r.left(60)
    r.forward(L)
    r.right(120)
    r.forward(L)
    r.left(60)
    for i in range(N-1):
        r.forward(seg-L)
        r.left(60)
        r.forward(L)
        r.right(120)
        r.forward(L)
        r.left(60)
    r.forward(seg-L/2)

if __name__ == '__main__':

    W = int(input('Tamanho da tela:'))
    L = int(input('Tamanho do lado do triangulo:'))
    N = int(input('Quantidade:'))

    janela = t.Screen()
    janela.setup(W,W)

    r = t.Turtle()
    r.pu()
    r.setpos(-(W/2),0)
    r.pd()
    r.pensize(5)

    desenhar_retangulos(W,N)
    
    janela.mainloop()