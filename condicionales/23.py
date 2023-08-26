nota_matematicas = float( input("Ingrese la nota en Matemáticas : ") )
nota_fisica = float( input("Ingrese la nota en Física : ") )

propina_matematicas = 3 if nota_matematicas > 17 else nota_matematicas
propina_fisica = 2 if nota_fisica > 15 else 0.50

promedio_notas = (nota_matematicas + nota_fisica) / 2

if promedio_notas > 16:
    obsequio = "reloj"
else:
    obsequio = "ninguno"

print(f"Propina por Matemáticas: S/. {propina_matematicas:.2f}")
print(f"Propina por Física: S/. {propina_fisica:.2f}")
print(f"Promedio de notas: {promedio_notas:.2f}")
print(f"Obsequio: {obsequio}")