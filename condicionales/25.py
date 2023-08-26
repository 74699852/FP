sueldo = int( input("Sueldo : ") )
hijos = int( input("Hijos : ") )

if hijos > 0:
    bonificacion = (sueldo * 0.125) + (40 * hijos)
else:
    bonificacion = sueldo * 0.10

total = sueldo + bonificacion

print( f"Bonificación por fiestas patrias = S/. {bonificacion:.2f}")
print( f"Sueldo neto a pagar = S/. {total:.2f}")