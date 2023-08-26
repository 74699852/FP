categoria = input("Categoría del trabajador (A/B/C/D) : ")
horas = int( input("Horas trabajadas : ") )

if categoria == 'A':
    pago = 21.00
elif categoria == 'B':
    pago = 19.50
elif categoria == 'C':
    pago = 17.00
elif categoria == 'D':
    pago = 15.50
else:
    print("Categoría inválida")
    exit()

sueldo = horas * pago

if sueldo > 2500:
    descuento = sueldo * 0.20
else:
    descuento = sueldo * 0.15

total = sueldo - descuento

print(f"Sueldo bruto: S/. {sueldo:.2f}")
print(f"Descuento: S/. {descuento:.2f}")
print(f"Sueldo neto: S/. {total:.2f}")