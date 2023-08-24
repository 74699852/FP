
num1 = int( input("Primer número : ") )
num2 = int( input("Segundo número : ") )

resultado = 0
for _ in range(num2):
    resultado += num1

print( f"Resultado = { format(resultado, '.2f') }" )