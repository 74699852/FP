km = int( input("Primer Tramo : ") )
pies = int( input("Segundo Tramo : ") )
millas = int( input("Tercer Tramo : ") )

metros = km * 1000 + pies / 3.2808 + millas * 1609
yardas = metros / 0.9144
    
 
print("Longitud total recorrida:")
print( f"metros = { format(metros, '.2f') }" )
print( f"yardas = { format(yardas, '.2f') }" )
