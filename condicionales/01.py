cantidad_adquirida = int( input("Ingrese la cantidad de unidades adquiridas: ") )

def calcular_importe_cantidad(cantidad):
    if cantidad >= 1 and cantidad <= 25:
        precio_unitario = 27
    elif cantidad >= 26 and cantidad <= 50:
        precio_unitario = 25
    else:
        precio_unitario = 23
    importe = cantidad * precio_unitario
    return importe

def calcular_descuento(importe, cantidad):
    if cantidad > 50:
        descuento = importe * 0.15
    else:
        descuento = importe * 0.05
    return descuento

importe_compra = calcular_importe_cantidad(cantidad_adquirida)
descuento = calcular_descuento(importe_compra, cantidad_adquirida)
total_a_pagar = importe_compra - descuento

print( f"Importe de la compra: S/. {importe_compra:.2f}")
print( f"Descuento aplicado: S/. {descuento:.2f}")
print( f"Total a pagar: S/. {total_a_pagar:.2f}")