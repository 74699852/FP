
cantidad = int(input("Ingrese la cantidad de dinero en soles: "))

billetes = [200, 100, 50, 20, 10]
monedas = [5, 2, 1]

for billete in billetes:
    cantidad_billetes = cantidad // billete
    if cantidad_billetes > 0:
        print(cantidad_billetes, "billete(s) de", billete, "soles")
        cantidad %= billete
    
for moneda in monedas:
    cantidad_monedas = cantidad // moneda
    if cantidad_monedas > 0:
        print(cantidad_monedas, "moneda(s) de", moneda, "nuevos soles")
        cantidad %= moneda