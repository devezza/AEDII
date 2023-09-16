import turtle as t

if __name__ == '__main__':

    W = 600
    N = 4
    L = 100

    janela = t.Screen()
    janela.setup(W,W)

    r = t.Turtle()
    r.pu()
    r.setpos(-(W/2),0)
    r.pd()
    r.pensize(5)

    seg = W/(N+1)

    r.forward(seg-L/2)
    r.left(60)
    r.forward(L)
    r.right(120)
    r.forward(L)
    r.left(60)
    for i in range(N-2):
        r.forward(seg-L)
        r.left(60)
        r.forward(L)
        r.right(120)
        r.forward(L)
        r.left(60)
    r.forward(seg-L)
    r.left(60)
    r.forward(L)
    r.right(120)
    r.forward(L)
    r.left(60)
    r.forward(seg-L/2)


    
    janela.mainloop()

    # n = int(input())
