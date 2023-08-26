unidades = int( input("Ingresar cantidad : ") )

importe = 20 * unidades

if importe > 700:
    descuento = importe * 0.16
elif importe >= 501 and importe <= 700:
    descuento = importe * 0.14
elif importe <= 500:
    descuento = importe * 0.12

total = importe - descuento

if unidades <= 50:
    caramelos = 5
elif unidades > 50 and unidades <= 100:
    caramelos = 10
elif unidades > 100:
    caramelos = 15

print(f"Importe de la compra: S/. {importe:.2f}")
print(f"Descuento aplicado: S/. {descuento:.2f}")
print(f"Total a pagar: S/. {total:.2f}")
print(f"Número de caramelos de obsequio: {caramelos}")
