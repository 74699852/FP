
cadena = "Arriba Perú."
subcadena = "ejemplo"

indice = cadena.find(subcadena)

if indice != -1:
    print( f"La subcadena '{subcadena}' se encontró en el índice {indice}.")
else:
    print( f"La subcadena '{subcadena}' no se encontró en la cadena.")