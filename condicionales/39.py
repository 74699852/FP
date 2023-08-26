horas_ausencia = float( input("Ingrese la cantidad de horas de ausencia al trabajo: ") )
tornillos_defectuosos = int( input("Ingrese la cantidad de tornillos defectuosos producidos: ") ) 
tornillos_no_defectuosos = int( input("Ingrese la cantidad de tornillos no defectuosos producidos: ") )

grado_eficiencia = 5  

if horas_ausencia <= 1.5:
    grado_eficiencia = 7  
    
if tornillos_defectuosos < 300:
    if grado_eficiencia == 7:
        grado_eficiencia = 12 
    else:
        grado_eficiencia = 8  
        
if tornillos_no_defectuosos > 10000:
    if grado_eficiencia == 7:
        grado_eficiencia = 13  
    elif grado_eficiencia == 8:
        grado_eficiencia = 15  
    elif grado_eficiencia == 12:
        grado_eficiencia = 20  
    else:
        grado_eficiencia = 9 

print(f"El grado de eficiencia del operario de torno es: {grado_eficiencia}")