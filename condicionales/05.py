numero = int( input("Ingrese un número de 4 cifras : ") )

cifras = [int(d) for d in str(numero)]

mayor_cifra = max(cifras)
menor_cifra = min(cifras)

mayor_numero_dos_cifras = mayor_cifra * 10 + menor_cifra

print( f"El mayor número de dos cifras posible es: {mayor_numero_dos_cifras}")