cantidad_producto_a = int( input("Ingrese la cantidad de unidades del producto A a comprar: "))
cantidad_producto_b = int( input("Ingrese la cantidad de unidades del producto B a comprar: "))

precio_producto_a = 25
precio_producto_b = 30

importe_bruto_a = cantidad_producto_a * precio_producto_a
importe_bruto_b = cantidad_producto_b * precio_producto_b

if cantidad_producto_a > 50:
    descuento_a = importe_bruto_a * 0.15
else:
    descuento_a = 0

if cantidad_producto_b > 60:
    descuento_b = importe_bruto_b * 0.10
else:
    descuento_b = 0

total_a_pagar_a = importe_bruto_a - descuento_a
total_a_pagar_b = importe_bruto_b - descuento_b

total_general = total_a_pagar_a + total_a_pagar_b

print(f"Importe bruto del producto A: S/. {importe_bruto_a:.2f}")
print(f"Descuento aplicado al producto A: S/. {descuento_a:.2f}")
print(f"Total a pagar por el producto A: S/. {total_a_pagar_a:.2f}")
print()
print(f"Importe bruto del producto B: S/. {importe_bruto_b:.2f}")
print(f"Descuento aplicado al producto B: S/. {descuento_b:.2f}")
print(f"Total a pagar por el producto B: S/. {total_a_pagar_b:.2f}")
print()
print(f"Total general a pagar: S/. {total_general:.2f}")