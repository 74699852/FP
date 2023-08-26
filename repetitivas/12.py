
def mostrar_numeros():
    for i in range(1, 101):
        print(i, end="\t")
        if i % 10 == 0:
            print()

mostrar_numeros()