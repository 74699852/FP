
altura = int( input("Altura del rectángulo : ") )

def imprimir_rectangulo(n):
    if n < 4:
        print("El valor de n debe ser igual o mayor a 4.")
        return

    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * (2 * n))
        else:
            print("*" + " " * (2 * n - 2) + "*")

imprimir_rectangulo(altura)
