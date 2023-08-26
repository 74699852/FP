costo_casa = float( input("Ingrese el costo de la casa: "))
ingreso_mensual = float( input("Ingrese el ingreso mensual del comprador: "))

if ingreso_mensual < 1250:
    cuota_inicial = costo_casa * 0.15
    cuotas_restantes = 120
else:
    cuota_inicial = costo_casa * 0.30
    cuotas_restantes = 75

monto_cuota_mensual = (costo_casa - cuota_inicial) / cuotas_restantes

print(f"Cuota inicial: S/. {cuota_inicial:.2f}")
print(f"Monto de la cuota mensual: S/. {monto_cuota_mensual:.2f}")