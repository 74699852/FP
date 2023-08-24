  
monto_vendido = int ( input("Ingrese el monto total vendido por el vendedor: "))
    
comision = monto_vendido * 0.09
sueldo_bruto = 500 + comision
descuento = sueldo_bruto * 0.11
sueldo_neto = sueldo_bruto - descuento

print( f"Comisión = { format(comision, '.2f') }" )
print( f"Sueldo bruto = { format(sueldo_bruto, '.2f') }" )
print( f"Descuento = { format(descuento, '.2f') }" )
print( f"Sueldo neto = { format(sueldo_neto, '.2f') }" )