import math

cateto1 = int( input("Primer cateto: "))
cateto2 = int( input("Segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
   
print( f"Hipotenusa del triángulo = { format(hipotenusa, '.2f') }" )