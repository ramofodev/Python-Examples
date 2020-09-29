import turtle
theTurtle = turtle.Turtle()

'''
Definición de funciones
'''

def dibujaGeometrias(origin, size, sides):
    theTurtle.goto(origin[0], origin[1])
    theTurtle.seth(0)
    angle = 360/sides
    for i in range (0, sides):
        theTurtle.fd(size)
        theTurtle.left(angle)
        
        
'''
Introducir datos
'''

strSize = ""

while strSize == "":
    strSize = input("Tamaño de la figura geométrica (px): ")
    if not strSize.isdigit():
        print("El tamaño debe ser un número entero")
        strSize = ""
    
    size = int(strSize)
        
strSides = ""

while strSides == "":
    strSides = input("Defina los lados de la figura geométrica: ")
    if not strSides.isdigit():
        print("Los lados de la figura geométrica deben ser un número entero")
        strSides = ""
        
    sides = int(strSides)
    
'''
Confirmación del estado de las variables
'''

print("Size contiene: " + strSize)
print("Sides contiene: " + strSides)


'''
Ejecución de la función
'''

dibujaGeometrias((0,0), size, sides)
