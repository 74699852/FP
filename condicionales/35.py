codigo = int( input("Ingrese el código del empleado : "))

if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0:
    tipo_empleado = "Administrativo"
elif codigo % 3 == 0 and codigo % 5 == 0:
    tipo_empleado = "Directivo"
elif codigo % 2 == 0:
    tipo_empleado = "Vendedor"
else:
    tipo_empleado = "Seguridad"

print( f"Tipo de empleado: {tipo_empleado}")