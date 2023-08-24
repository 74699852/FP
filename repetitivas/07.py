
numero = int( input("Número : ") )

factorial = 1
for i in range(1, numero + 1):
    factorial *= i

print( f"Factorial = { format(factorial, '.2f') }" )