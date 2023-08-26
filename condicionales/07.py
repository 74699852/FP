numero1 = int( input("Ingrese el primer número : ") )
numero2 = int( input("Ingrese el segundo número : ") )
numero3 = int( input("Ingrese el tercer número : ") )

suma_total = numero1 + numero2 + numero3

numero_intermedio = suma_total - max(numero1, numero2, numero3) - min(numero1, numero2, numero3)

print(f"El número intermedio es: {numero_intermedio}")
