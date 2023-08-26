
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]

def contar_capicuas():
    contador = 0
    for num in range(100, 1000):
        if es_capicua(num):
            contador += 1
    return contador

cantidad_capicuas = contar_capicuas()

print(f"Hay {cantidad_capicuas} números capicúa de 3 cifras.")
