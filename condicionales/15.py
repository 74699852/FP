
monto_vendido = int( input("Ingrese el monto total vendido : ") )

if monto_vendido <= 5000:
    porcentaje_comision = 0.05
elif monto_vendido <= 10000:
    porcentaje_comision = 0.08
elif monto_vendido <= 20000:
    porcentaje_comision = 0.10
else:
    porcentaje_comision = 0.15

comision = monto_vendido * porcentaje_comision
sueldo_bruto = 250 + comision

if sueldo_bruto > 3500:
    descuento = sueldo_bruto * 0.15
else:
    descuento = sueldo_bruto * 0.08

sueldo_neto = sueldo_bruto - descuento

print(f"Comisión aplicada: S/. {comision:.2f}")
print(f"Sueldo bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {sueldo_neto:.2f}")
