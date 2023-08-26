mensual = int( input("Cuota mensual : "))
dia = int( input("Día de pago (1-31) : "))

if dia <= 10:
    descuento = max(5, 0.02 * mensual)
    total = mensual - descuento
elif dia <= 20:
    descuento = 0
    total = mensual
else:
    recargo = max(10, 0.03 * mensual)
    total = mensual + recargo

print( f"Cuota mensual = ${mensual:.2f}")
print( f"Total a pagar = ${total:.2f}")