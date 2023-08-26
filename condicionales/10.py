def calcular_promedio_aprobatorio(notas):
    notas_ordenadas = sorted(notas)
    notas_ordenadas = notas_ordenadas[1:-1]
    promedio = sum(notas_ordenadas) / len(notas_ordenadas)
    return promedio

notas = []

for i in range(5):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

promedio_aprobatorio = calcular_promedio_aprobatorio(notas)

print("Notas eliminadas:", notas[notas.index(max(notas))], "y", notas[notas.index(min(notas))])
print(f"Promedio aprobatorio: {promedio_aprobatorio:.2f}")