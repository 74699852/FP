numero = int( input("Ingrese un número : ") )

if numero == 1:
    dia = "lunes"
elif numero == 2:
    dia = "martes"
elif numero == 3:
    dia = "miércoles"
elif numero == 4:
    dia = "jueves"
elif numero == 5:
    dia = "viernes"
elif numero == 6:
    dia = "sábado"
elif numero == 7:
    dia = "domingo"
else:
    dia = "inválido"

if dia != "inválido":
    print(f"El número {numero} corresponde al día {dia}.")
else:
    print("Número inválido. Por favor, ingrese un número del 1 al 7.")
