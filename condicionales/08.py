
examenes_aprobados = int( input("Ingrese la cantidad de exámenes aprobados : ") ) 

total = 20 + (5 * examenes_aprobados)

print( f"El monto total de la propina es = S/. { format(total, '.2f') }" )