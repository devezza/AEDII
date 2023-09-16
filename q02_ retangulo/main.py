import turtle as t

r = t.Turtle()

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


r.pu()
r.forward(20)
r.pd()

r.begin_fill()
r.fillcolor('green')
r.left(90)
r.forward(100)
r.left(90)
r.forward(10)
r.left(90)
r.forward(100)
r.left(90)
r.forward(10)
r.end_fill()



t.mainloop()