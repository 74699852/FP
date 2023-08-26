numero = int( input("Ingrese un número : ") )

cifra_centenas = numero // 100
cifra_decenas = (numero // 10) % 10
cifra_unidades = numero % 10

if (cifra_decenas == cifra_centenas + 1 and cifra_unidades == cifra_decenas + 1) or \
   (cifra_decenas == cifra_centenas - 1 and cifra_unidades == cifra_decenas - 1):
    mensaje = "Las cifras son consecutivas."
else:
    mensaje = "Las cifras no son consecutivas."

print(mensaje)