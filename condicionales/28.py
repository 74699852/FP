hora_24h = input("Ingrese la hora en formato de 24 horas (HH:MM): ")

try:
    horas, minutos = map(int, hora_24h.split(':'))
    
    if 0 <= horas <= 23 and 0 <= minutos <= 59:
        if horas < 12:
            meridiano = "AM"
            if horas == 0:
                horas = 12
        else:
            meridiano = "PM"
            if horas > 12:
                horas -= 12
        
        hora_12h = f"{horas:02d}:{minutos:02d} {meridiano}"
        print(f"Hora en formato de 12 horas: {hora_12h}")
    else:
        print("Error: Hora inválida")
        
except ValueError:
    print("Error: Formato de hora incorrecto")