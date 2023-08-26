cuadernos = int( input("Cantidad de cuadernos : ") )
lapiceros_lucas = 0
lapiceros_faber = 0
lapiceros_pilot = 0

if cuadernos >= 12:
    lapiceros_lucas = cuadernos // 4
    if cuadernos >= 24:
        lapiceros_faber = cuadernos // 4
        if cuadernos >= 36:
            lapiceros_pilot = cuadernos // 4
            lapiceros_faber += cuadernos // 6
            lapiceros_lucas += cuadernos // 12

total_lapiceros = lapiceros_lucas + lapiceros_faber + lapiceros_pilot

print(f"Lapiceros Lucas obsequiados: {lapiceros_lucas}")
print(f"Lapiceros Faber obsequiados: {lapiceros_faber}")
print(f"Lapiceros Pilot obsequiados: {lapiceros_pilot}")
print(f"Total de lapiceros obsequiados: {total_lapiceros}")