vendido = int( input("Monto total vendido : "))

sueldo = vendido * 0.10
monto_exceso = max(vendido - 5000, 0)
sueldo_exceso = (monto_exceso // 500) * 25

total = sueldo + sueldo_exceso

print( f"Sueldo base = S/. {sueldo:.2f}")
print( f"Sueldo por exceso de ventas = S/. {sueldo_exceso:.2f}")
print( f"Sueldo total del vendedor = S/. {total:.2f}")