
dividendo = int( input("Dividendo : ") )
divisor = int( input("Divisor : ") )

cociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    cociente += 1
resto = dividendo

print( f"Cociente = { format(cociente, '.2f') }" )
print( f"Resto = { format(resto, '.2f') }" )