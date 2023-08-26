edad1 = int( input("Ingrese la primera edad : "))
edad2 = int( input("Ingrese la segunda edad : "))
edad3 = int( input("Ingrese la tercera edad : "))

edades = [edad1, edad2, edad3]

edad_menor = min(edades)
edad_mayor = max(edades)

print(f"La edad menor es: {edad_menor}")
print(f"La edad mayor es: {edad_mayor}")