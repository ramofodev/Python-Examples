import turtle
theTurtle = turtle.Turtle()

'''
    Polygon
'''

def drawPolygon(origin, size, sides):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    angle = 360/sides
    for i in range(0, sides):
        theTurtle.fd(size)
        theTurtle.left(angle)    


def drawTriangle(origin, size):
    drawPolygon(origin, size, 3)

def drawSquare(origin, size):
    drawPolygon(origin, size, 4)

def drawPentagon(origin, size):
    drawPolygon(origin, size, 5)
    
drawTriangle((0,0), 50)
drawSquare((0,0), 50)
drawPentagon((0,0),50)


'''
    Abstraccion que permite dibujar un poligono con n lados
   Aquí n = 6
'''

drawPolygon((0,0), 50, 6)

