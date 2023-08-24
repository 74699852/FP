numero = int( input("Numero natural de 4 cifras :"))

reves = 0
while numero > 0:
        digito = numero % 10
        reves = reves * 10 + digito
        numero //= 10
    
print( f"Número al revés = { format(reves, '.2f') }" )