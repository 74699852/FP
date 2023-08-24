
cantidad = int ( input("Ingrese la cantidad de unidades adquiridas: "))
unidad = float ( input("Ingrese el precio unitario del artículo: "))
    
importe_compra = cantidad * unidad
primer_descuento = importe_compra * 0.15
importe_con_primer_descuento = importe_compra - primer_descuento
segundo_descuento = importe_con_primer_descuento * 0.15
importe_a_pagar = importe_con_primer_descuento - segundo_descuento

print( f"Importe de la compra = { format(importe_compra, '.2f') }" )
print( f"Descuento 1 (15%) = { format(primer_descuento, '.2f') }" )
print( f"Importe con primer descuento = { format(importe_con_primer_descuento, '.2f') }" )
print( f"Descuento 2 (15%) = { format(segundo_descuento, '.2f') }" )
print( f"Importe a pagar = { format(importe_a_pagar, '.2f') }" )