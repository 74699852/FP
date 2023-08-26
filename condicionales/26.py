compra = int(input("Monto de la compra : "))

if compra > 5000:
    prestamo = compra * 0.30
else:
    prestamo = compra * 0.20

interes = prestamo * 0.10
dinero_propio = compra - prestamo

total = dinero_propio + prestamo + interes

print( f"Monto a pagar con dinero propio = $ {dinero_propio:.2f}")
print( f"Monto del préstamo del banco = $ {prestamo:.2f}")
print( f"Interés del banco = $ {interes:.2f}")
print( f"Total a pagar por la empresa = $ {total:.2f}")