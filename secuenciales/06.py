import math

radio = int( input("Radio : ") )
altura = int( input("Altura : ") )

total = 2 * math.pi * radio * (radio +altura)
volumen = math.pi * math.pow(radio,2) * altura

print( f"Área Total = { format(total, '.2f')} u2" )
print( f"Volumen = { format(volumen, '.2f')} u2" )
