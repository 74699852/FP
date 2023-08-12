metros = int( input("Metros : ") )

centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print( f"centimetros = { format(centimetros, '.2f') }" )
print( f"pulgadas = { format(pulgadas, '.2f') }" )
print( f"pies = { format(pies, '.2f') }" )
print( f"yardas = { format(yardas, '.2f') }" )