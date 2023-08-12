import math

radio = int( input("Radio : ") )
altura = int( input("Altura : ") )

areaBase = math.pi * math.pow(radio,2) 
areaLateral = 2 * math.pi * radio * altura 
areaTotal = 2 * areaBase * areaLateral

print( f"Area Base = { format(areaBase, '.2f')} u2" )
print( f"Area Lateral = { format(areaLateral, '.2f')} u2" )
print( f"Area Total = { format(areaTotal, '.2f')} u2" )