
numeros = []
for i in range(5):
    numero = int(input("Ingresa el número " + str(i + 1) + ": "))
    numeros.append(numero)
    
numeros.sort(reverse=True)  # Ordenar en orden descendente
    
suma_mayores = sum(numeros[:3])
promedio = suma_mayores / 3

print( f"Promedio de los 3 números mayores = { format(promedio, '.2f') }" )