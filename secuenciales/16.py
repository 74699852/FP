
tarifa_horaria = int ( input("Ingrese la tarifa horaria: "))
horas_trabajadas = int ( input("Ingrese el número total de horas trabajadas: "))
    
sueldo_basico = tarifa_horaria * horas_trabajadas
bonificacion = sueldo_basico * 0.20
sueldo_bruto = sueldo_basico + bonificacion
descuento = sueldo_bruto * 0.10
sueldo_neto = sueldo_bruto - descuento

print( f"Sueldo básico = { format(sueldo_basico, '.2f') }" )
print( f"Sueldo bruto = { format(sueldo_bruto, '.2f') }" )
print( f"Sueldo neto = { format(sueldo_neto, '.2f') }" )