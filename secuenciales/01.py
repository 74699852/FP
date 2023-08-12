varones = int( input("varones : ") )
mujeres = int( input("mujeres : ") )

total = varones + mujeres 
pVarones = varones * 100 / total
pMujeres = mujeres * 100 / total

print( f" varones = { format(pVarones, '.2f') } %" )
print( f" mujeres = { format(pMujeres, '.2f') } %" )