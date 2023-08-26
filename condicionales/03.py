angulo_grados = int( input("Ingrese el ángulo en grados : "))

def clasificar_angulo(angulo):
    if angulo == 0:
        return "Nulo"
    elif 0 < angulo < 90:
        return "Agudo"
    elif angulo == 90:
        return "Recto"
    elif 90 < angulo < 180:
        return "Obtuso"
    elif angulo == 180:
        return "Llano"
    elif 180 < angulo < 360:
        return "Cóncavo"
    elif angulo == 360:
        return "Completo"
    else:
        return "Ángulo inválido"

clasificacion = clasificar_angulo(angulo_grados)

print( f"La clasificación del ángulo es : {clasificacion}")
