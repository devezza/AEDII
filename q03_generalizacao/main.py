import turtle as t

def retangulo():
    r.begin_fill()
    r.fillcolor('blue')
    r.forward(100)
    r.left(90)
    r.forward(10)
    r.left(90)
    r.forward(100)
    r.left(90)
    r.forward(10)
    r.end_fill()

if __name__ == '__main__':
    n = int(input())
    r = t.Turtle()
    for i in range(n):
        retangulo()
        r.pu()
        r.forward(30)
        r.left(90)
        r.pd()
    t.mainloop()
