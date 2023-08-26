numero_tarjeta = int( input("Ingrese el número : "))
monto_compra = float( input("Ingrese el monto : "))

if numero_tarjeta % 2 == 0 and numero_tarjeta >= 100:
    descuento = monto_compra * 0.15
    mensaje_descuento = "15 %"
else:
    descuento = monto_compra * 0.05
    mensaje_descuento = "5 %"

total_a_pagar = monto_compra - descuento

print( f"Número de tarjeta : {numero_tarjeta}")
print( f"Monto de la compra = S/. { format(monto_compra, '.2f') }" )
print( f"Descuento aplicado : {mensaje_descuento}")
print( f"Total a pagar = S/. { format(total_a_pagar, '.2f') }" )