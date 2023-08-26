horas_trabajadas = int( input("Ingrese el número de horas trabajadas: "))
tarifa_normal = int( input("Ingrese la tarifa horaria normal: "))

if horas_trabajadas > 48:
    horas_extras = horas_trabajadas - 48
    tarifa_extra = tarifa_normal * 1.20
    pago_horas_extras = horas_extras * tarifa_extra
    pago_horas_normales = 48 * tarifa_normal
else:
    pago_horas_normales = horas_trabajadas * tarifa_normal
    pago_horas_extras = 0

sueldo_bruto = pago_horas_normales + pago_horas_extras

if sueldo_bruto > 1500:
    descuento = sueldo_bruto * 0.11
else:
    descuento = 0

sueldo_neto = sueldo_bruto - descuento

print( f"Horas trabajadas = {horas_trabajadas} horas")
print( f"Tarifa horaria normal = S/. {tarifa_normal:.2f}")
print( f"Pago por horas normales = S/. {pago_horas_normales:.2f}")
print( f"Pago por horas extras = S/. {pago_horas_extras:.2f}")
print( f"Sueldo bruto = S/. {sueldo_bruto:.2f}")
print( f"Descuento = S/. {descuento:.2f}")
print( f"Sueldo neto a pagar = S/. {sueldo_neto:.2f}")
