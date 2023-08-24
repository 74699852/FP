
donacion_anual = int ( input("Ingrese el monto de la donación anual: "))
    
centro_salud = donacion_anual * 0.25
comedor_infantil = donacion_anual * 0.35
escuela_infantil = donacion_anual * 0.25
asilo_ancianos = donacion_anual - (centro_salud + comedor_infantil + escuela_infantil)

print( f"Centro de salud = { format(centro_salud, '.2f') }" )
print( f"Comedor infantil = { format(comedor_infantil, '.2f') }" )
print( f"Escuela infantil = { format(escuela_infantil, '.2f') }" )
print( f"Asilo de ancianos = { format(centro_salud, '.2f') }" )