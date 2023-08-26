numero = int( input("Número del empleado : "))

estado = numero // 1000
edad = (numero // 10) % 100
género = numero % 10

if estado == 1:
    estado_civil = "soltero"
elif estado == 2:
    estado_civil = "casado"
elif estado == 3:
    estado_civil = "divorciado"
elif estado == 4:
    estado_civil = "viudo"
else:
    estado_civil = "desconocido"

if género == 1:
    genero = "masculino"
elif género == 2:
    genero = "femenino"
else:
    genero = "desconocido"

print( f"Estado civil : {estado_civil}")
print( f"Edad : {edad} años")
print( f"Género : {genero}")
