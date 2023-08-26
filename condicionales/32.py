categoria = input("Ingrese la categoría del estudiante (A/B/C/D): ")
pension_actual = 0

if categoria == 'A':
    pension_actual = 550.00
elif categoria == 'B':
    pension_actual = 500.00
elif categoria == 'C':
    pension_actual = 450.00
elif categoria == 'D':
    pension_actual = 400.00
else:
    print("Categoría inválida")
    exit()

promedio_ponderado = float(input("Ingrese el promedio ponderado del ciclo anterior: "))

if promedio_ponderado >= 0 and promedio_ponderado < 14:
    descuento = 0
elif promedio_ponderado < 16:
    descuento = pension_actual * 0.10
elif promedio_ponderado < 18:
    descuento = pension_actual * 0.12
else:
    descuento = pension_actual * 0.15

nueva_pension = pension_actual - descuento

print(f"Pensión actual: S/. {pension_actual:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Nueva pensión: S/. {nueva_pension:.2f}")