votos_pamela = int( input("Ingrese la cantidad de votos para Pamela : ") )
votos_carol = int( input("Ingrese la cantidad de votos para Carol : ") )
votos_fanny = int( input("Ingrese la cantidad de votos para Fanny : ") )

total_votos = votos_pamela + votos_carol + votos_fanny

if votos_pamela > total_votos / 2:
    puesto_pamela = "Ganadora"
    puesto_carol = "Perdedora"
    puesto_fanny = "Perdedora"
elif votos_carol > total_votos / 2:
    puesto_pamela = "Perdedora"
    puesto_carol = "Ganadora"
    puesto_fanny = "Perdedora"
elif votos_fanny > total_votos / 2:
    puesto_pamela = "Perdedora"
    puesto_carol = "Perdedora"
    puesto_fanny = "Ganadora"
else:
    # No hay ganador, pasan a segunda vuelta
    segundo_puesto = max(votos_pamela, votos_carol, votos_fanny)
    if segundo_puesto == votos_pamela:
        puesto_pamela = "Segunda vuelta"
        puesto_carol = "Segunda vuelta"
        puesto_fanny = "Ganadora"
    elif segundo_puesto == votos_carol:
        puesto_pamela = "Segunda vuelta"
        puesto_carol = "Ganadora"
        puesto_fanny = "Segunda vuelta"
    else:
        puesto_pamela = "Ganadora"
        puesto_carol = "Segunda vuelta"
        puesto_fanny = "Segunda vuelta"

print( f"Pamela : {puesto_pamela}")
print( f"Carol : {puesto_carol}")
print( f"Fanny : {puesto_fanny}")