numero = float(input("Ingrese un número: "))

if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

print( f"El número es {signo}.")