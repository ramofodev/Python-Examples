'''
Introducir edad del perro
'''

strEdad = ""

while strEdad == "":
    strEdad = input("Edad del gato: ")
    if not strEdad.isdigit():
        print("La edad del gato ha de ser un número entero")
        strEdad = ""
        
edad = int(strEdad)
'''
Calcular edad humana del gato
'''
edadHumana = edad * 4
'''
Mostrar edad del gato
'''
print("Su gato tiene %d años humanos" % edadHumana)