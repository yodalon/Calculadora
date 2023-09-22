"""
Solicitar al usuario en un menu escoger una figura geometrica (cuadrado, triangulo, rectagunlo y ciruculo) el programa debe calcular el area de la figura escogida por el usuario
"""

import math
while True:   
    opcion = int(input("Selecciona una figura \n \t 1. Cuadrado\n \t 2. Triangulo \n \t 3. Rectangulo \n \t 4. Circulo\n \t 5. Salir \n"))

    if opcion == 1:
        lado = float(input("Ingresa la longitud del lado del cuadrado: "))
        area = lado * lado
        print(f"El área del cuadrado es: {area}")
        print ("********************************")
        
    elif opcion == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es: {area}")
        print ("********************************")
        
    elif opcion == 3:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area}")
        print ("********************************")
        
    elif opcion == 4:
        radio = float(input("Ingresa el radio del círculo: "))
        area = math.pi * (radio ** 2)
        print(f"El área del círculo es: {area}")
        print ("********************************")
        
    elif opcion == 5:
        print("Saliendo del programa.")
        break
