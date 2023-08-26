def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_dias_mes(mes, anio):
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    elif mes in meses_31_dias:
        return 31
    else:
        return 30

def obtener_nombre_mes(mes):
    nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                     "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    return nombres_meses[mes - 1]

def obtener_dias_transcurridos(dia, mes, anio):
    meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
    dias_transcurridos = dia
    for m in range(1, mes):
        if m in meses_31_dias:
            dias_transcurridos += 31
        elif m == 2:
            dias_transcurridos += 28 if not es_bisiesto(anio) else 29
        else:
            dias_transcurridos += 30
    return dias_transcurridos

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes (número): "))
anio = int(input("Ingrese el año: "))

dias_mes = obtener_dias_mes(mes, anio)
nombre_mes = obtener_nombre_mes(mes)
dias_transcurridos = obtener_dias_transcurridos(dia, mes, anio)

print(f"Días del mes: {dias_mes}")
print(f"Mes: {nombre_mes}")
print(f"Días transcurridos desde el 01 de enero: {dias_transcurridos}")