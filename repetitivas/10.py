
def suma_cifras(numero):
    suma_pares = 0
    suma_impares = 0
    for cifra in str(numero):
        cifra_int = int(cifra)
        if cifra_int % 2 == 0:
            suma_pares += cifra_int
        else:
            suma_impares += cifra_int
    return suma_pares, suma_impares

def encontrar_numeros():
    cantidad_encontrados = 0
    for num in range(1000, 10000):
        suma_pares, suma_impares = suma_cifras(num)
        if suma_pares == suma_impares:
            print(num)
            cantidad_encontrados += 1

    return cantidad_encontrados

cantidad_encontrados = encontrar_numeros()
print(f"Se encontraron {cantidad_encontrados} números que cumplen la condición.")