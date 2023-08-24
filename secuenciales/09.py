numero = int( input("Numero entero de 4 cifras :"))

suma = 0
while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    
print( f"Suma de las cifras = { format(suma, '.2f') }" )