
base = int( input("Base : ") )
exponente = int( input("Exponente : ") )

def calcular_potencia(base, exponente):
    potencia = 1
    for _ in range(exponente):
        potencia *= base
    return potencia

resultado = calcular_potencia(base, exponente)

print( f"Resultado = { format(resultado, '.2f') }" )