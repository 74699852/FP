
n = int ( input("Número : ") )
m = int ( input("Cantidad de múltiplos : ") )

print(f"Los primeros {m} múltiplos de {n} son:")

for i in range(1, m + 1):
    multiplo = n * i
    print(multiplo)