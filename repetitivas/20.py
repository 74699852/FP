def calcular_estadisticas(numeros):
    menor = min(numeros)
    mayor = max(numeros)
    promedio = sum(numeros) / len(numeros)
    return menor, mayor, promedio

numeros = []

for i in range(10):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

menor, mayor, promedio = calcular_estadisticas(numeros)

print( f"El menor número es = { format(menor, '.2f') }" )
print( f"El mayor número es = { format(mayor, '.2f') }" )
print( f"El promedio de los números es = { format(promedio, '.2f') }" )