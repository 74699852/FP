
numero_limite = int( input("Ingrese el valor de n : ") )

def suma_multiplos_de_tres_no_cinco(n):
    suma = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 != 0:
            suma += i
    return suma

resultado = suma_multiplos_de_tres_no_cinco(numero_limite)

print( f"La suma de los múltiplos de 3 (pero no de 5) menores o iguales a {numero_limite} es: {resultado}")
