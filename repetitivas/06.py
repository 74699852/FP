
numero = int( input("Número : ") )
inicio = int( input("Número inicial de tabla : ") )
fin = int( input("Número final de tabla : ") )

def tabla_de_multiplicar(n, x, y):
    for i in range(x, y + 1):
        print(f"Tabla de multiplicar del {n} x {i}:")
        for j in range(1, 11):
            resultado = n * i * j
            print(f"{n} x {i} x {j} = {resultado}")
        print("\n")

tabla_de_multiplicar(numero, inicio, fin)