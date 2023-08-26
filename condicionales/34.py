peso = float( input("Ingrese el peso en kg: ") )
estatura = float( input("Ingrese la estatura en metros: ") )

imc = peso / (estatura ** 2)

grado_obesidad = ""
if imc < 20:
    grado_obesidad = "Delgado"
elif 20 <= imc < 25:
    grado_obesidad = "Normal"
elif 25 <= imc < 27:
    grado_obesidad = "Sobrepeso"
else:
    grado_obesidad = "Obesidad"

print(f"El IMC es: {imc:.2f}")
print(f"Grado de Obesidad: {grado_obesidad}")