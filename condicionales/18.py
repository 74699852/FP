donacion = float( input("Ingrese el monto de la donación : ") )

if donacion >= 10000:
    salud = donacion * 0.30
    comedor = donacion * 0.50
else:
    salud = donacion * 0.25
    comedor = donacion * 0.60

bolsa = donacion - (salud + comedor)

print(f"Monto destinado al centro de salud: $ {salud:.2f}")
print(f"Monto destinado al comedor de niños: $ {comedor:.2f}")
print(f"Monto invertido en la bolsa: $ {bolsa:.2f}")