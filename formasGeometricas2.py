import turtle
theTurtle = turtle.Turtle()

def drawTriangle(origin, size):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    theTurtle.fd(size)
    theTurtle.left(120)
    theTurtle.fd(size)
    theTurtle.left(120)
    theTurtle.fd(size)
    theTurtle.left(120)

def drawSquare(origin, size):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    theTurtle.fd(size)
    theTurtle.left(90)
    theTurtle.fd(size)
    theTurtle.left(90)
    theTurtle.fd(size)
    theTurtle.left(90)
    theTurtle.fd(size)
    theTurtle.left(90)

def drawPentagon(origin, size):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)
    theTurtle.fd(size)
    theTurtle.left(72)

'''
    Abstracción de los procesos de dibujar Triangulo, cuadrado y pentagono
'''

drawTriangle((0,0), 50)
drawSquare((0,0), 50)
drawPentagon((0,0), 50)