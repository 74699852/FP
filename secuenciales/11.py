num1 = int( input("Primer número de 3 cifras : ") )
num2 = int( input("Segundo número de 3 cifras : ") )

cifra1_num1 = num1 // 100
cifra3_num1 = num1 % 10
cifra1_num2 = num2 // 100
cifra3_num2 = num2 % 10
        
nuevo_num1 = cifra3_num2 * 100 + num1 % 100
nuevo_num2 = cifra3_num1 * 100 + num2 % 100

print( f"Primer número intercambiado = { format(nuevo_num1, '.2f') }" )
print( f"Segundo número intercambiado = { format(nuevo_num2, '.2f') }" )