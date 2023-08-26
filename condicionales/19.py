sexo = input("Ingrese el sexo : ")
edad = int( input("Ingrese la edad : ") )

if sexo == "F":
    if edad < 23:
        categoria = "FA"
    else:
        categoria = "FB"
elif sexo == "M":
    if edad < 25:
        categoria = "MA"
    else:
        categoria = "MB"
else:
    print("Sexo no válido.")
    exit()

print( f"Categoría del postulante: {categoria}")