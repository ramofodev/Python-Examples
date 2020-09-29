name = input("¿Cómo te llamas? ")
print("Hola,", name)

'''
Dos opciones de realizar la variable como entero:

a) Estableciendo una variable intermedia y transformando luego el str en int. Mejor control de errores
b) Poniéndolo antes el int en la introducción de la variable, ya que se van ejecutar en cadena
'''

'''
Inicializamos variables edad, año actual, cumpleaños ya pasado en el año
'''

strAge = ""
strYear = ""
strBirthdayPast = ""
age = 0
year = 0
birthdayPast = False

'''
Analizamos inputs
'''

while strAge == "":
    strAge = input("¿Cuántos años tienes? ")
    if not strAge.isdigit():
        print("La edad debe ser un número entero")
        strAge = ""
        
    
while strYear == "":
    strYear = input("¿En qué año estamos? ")
    if not strYear.isdigit():
        print("El año actual debe ser un número")
        strYear = ""

while strBirthdayPast == "":
    strBirthdayPast = input("¿Has cumplido años este año? (S/N) ")
    if not strBirthdayPast == ("S"):
        print("Debes responder S o N")
        strBirthdayPast = ""
        
'''
Paso a variables
'''
age = int(strAge)
year = int(strYear)

if strBirthdayPast == "S":
    birthYear = year - age
else:
    birthdayPast = False
    birthYear = year - age - 1
    
print(name, "naciste en", birthYear)