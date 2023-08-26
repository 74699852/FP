nota1 = int( input("Ingrese la nota de la primera práctica : ") )
nota2 = int( input("Ingrese la nota de la segunda práctica : ") )
nota3 = int( input("Ingrese la nota de la tercera práctica : ") )

def calcular_promedio_final(nota1, nota2, nota3):
    if nota3 < 10:
        promedio_final = (nota1 + nota2 + nota3) / 3
    else:
        promedio_final = (nota1 + nota2 + (nota3 + 2)) / 3
    return promedio_final

promedio = calcular_promedio_final(nota1, nota2, nota3)

print( f"El promedio final del alumno es = { format(promedio, '.2f') }" )