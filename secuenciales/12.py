import math

a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

def calcular_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz_unica = -b / (2*a)
        return raiz_unica
    else:
        return "No tiene soluciones reales"

soluciones = calcular_ecuacion_cuadratica(a, b, c)
    
print("Las soluciones de la ecuación son:", soluciones)