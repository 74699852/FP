precio = float( input("Ingrese el precio por docena del producto: "))
cantidad = int( input("Ingrese la cantidad de docenas a comprar: "))

if cantidad >= 6:
    descuento = precio * cantidad * 0.15
else:
    descuento = precio * cantidad * 0.10

if cantidad >= 30:
    lapiceros_obsequio = (cantidad // 3) * 2
else:
    lapiceros_obsequio = 0

monto = precio * cantidad
total = monto - descuento

print(f"Monto de la compra: S/. {monto:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total:.2f}")
print(f"Cantidad de lapiceros de obsequio: {lapiceros_obsequio}")