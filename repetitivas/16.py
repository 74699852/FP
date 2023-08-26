
texto = input("Ingrese una cadena de texto : ")

def invertir_cadena(cadena):
    cadena_invertida = cadena[::-1]
    return cadena_invertida

texto_invertido = invertir_cadena(texto)

print("Cadena invertida :", texto_invertido)
