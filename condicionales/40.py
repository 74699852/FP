def calcular_promedio_final(notas, pesos):
    suma_productos = sum(nota * peso for nota, peso in zip(notas, pesos))
    suma_pesos = sum(pesos)
    promedio_final = suma_productos / suma_pesos
    return promedio_final

def determinar_condicion(promedio):
    if promedio >= 13:
        return "Aprobado"
    else:
        return "Desaprobado"

pesos_matematica = [0.10, 0.20, 0.10, 0.30, 0.30]
pesos_fisica = [0.20, 0.20, 0.20, 0.20, 0.20]
pesos_quimica = [0.10, 0.30, 0.10, 0.25, 0.25]

notas_matematica = [float(input("Ingrese la nota para Matemática - PC1: ")),
                    float(input("Ingrese la nota para Matemática - PC2: ")),
                    float(input("Ingrese la nota para Matemática - PC3: ")),
                    float(input("Ingrese la nota para Matemática - EP: ")),
                    float(input("Ingrese la nota para Matemática - EF: "))]

notas_fisica = [float(input("Ingrese la nota para Física - PC1: ")),
                float(input("Ingrese la nota para Física - PC2: ")),
                float(input("Ingrese la nota para Física - PC3: ")),
                float(input("Ingrese la nota para Física - EP: ")),
                float(input("Ingrese la nota para Física - EF: "))]

notas_quimica = [float(input("Ingrese la nota para Química - PC1: ")),
                 float(input("Ingrese la nota para Química - PC2: ")),
                 float(input("Ingrese la nota para Química - PC3: ")),
                 float(input("Ingrese la nota para Química - EP: ")),
                 float(input("Ingrese la nota para Química - EF: "))]

promedio_final_matematica = calcular_promedio_final(notas_matematica, pesos_matematica)
promedio_final_fisica = calcular_promedio_final(notas_fisica, pesos_fisica)
promedio_final_quimica = calcular_promedio_final(notas_quimica, pesos_quimica)

condicion_matematica = determinar_condicion(promedio_final_matematica)
condicion_fisica = determinar_condicion(promedio_final_fisica)
condicion_quimica = determinar_condicion(promedio_final_quimica)

print( f"Promedio final Matemática : {promedio_final_matematica:.2f} - Condición: {condicion_matematica}")
print( f"Promedio final Física : {promedio_final_fisica:.2f} - Condición: {condicion_fisica}")
print( f"Promedio final Química : {promedio_final_quimica:.2f} - Condición: {condicion_quimica}")