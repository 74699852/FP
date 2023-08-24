    
aporte_juan_dolares = int ( input("Aporte de Juan en dólares: "))
aporte_rosa_dolares = int ( input("Aporte de Rosa en dólares: "))
aporte_daniel_soles = int ( input("Aporte de Daniel en nuevos soles: "))
    
capital_total_soles = (aporte_juan_dolares * 3) + (aporte_rosa_dolares * 3) + aporte_daniel_soles
capital_total_dolares = capital_total_soles / 3
    
porcentaje_juan = (aporte_juan_dolares * 3) / capital_total_soles * 100
porcentaje_rosa = (aporte_rosa_dolares * 3) / capital_total_soles * 100
porcentaje_daniel = (aporte_daniel_soles) / capital_total_soles * 100

print( f"Capital total en dólares = { format(capital_total_dolares, '.2f') }" )
print( f"Porcentaje de Juan = { format(porcentaje_juan, '.2f') } %" )
print( f"Porcentaje de Rosa = { format(porcentaje_rosa, '.2f') } %" )
print( f"Porcentaje de Daniel = { format(porcentaje_daniel, '.2f') } %" )