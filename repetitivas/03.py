
numero = int( input("Número entero : ") )

divisores = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

print( f"Cantidad de divisores = { format(divisores, '.2f') }" )