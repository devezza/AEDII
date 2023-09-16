import turtle as t

## Criando nosso objeto
tartaruga = t.Turtle()
tartaruga.shape('turtle')
tartaruga.color('purple')
tartaruga.begin_fill()
tartaruga.fillcolor('purple')


tartaruga.forward(200)
tartaruga.left(120)
tartaruga.forward(200)
tartaruga.left(120)
tartaruga.forward(200)

tartaruga.end_fill()

t.mainloop()