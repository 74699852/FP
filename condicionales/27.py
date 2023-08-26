monto = int( input("Monto total vendido : "))

comision = monto * 0.15
sueldo = 600 + comision

if sueldo > 1800:
    descuento = sueldo * 0.10
else:
    descuento = sueldo * 0.05

total = sueldo - descuento

if monto > 1000:
    obsequio = 3
else:
    obsequio = 1

print( f"Sueldo bruto = S/. {sueldo:.2f}")
print( f"Descuento = S/. {descuento:.2f}")
print( f"Sueldo neto = S/. {total:.2f}")
print( f"Número de polos obsequiados = {obsequio}")
