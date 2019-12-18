# Ejercicio 12
import os
import libreria

# Calcular el cambio de monedas
# Declaracion de datos

#imput
dolares=int(os.sys.argv[1])
cambio=int(os.sys.argv[2])
soles=libreria.soles(cambio,dolares)

if (soles>=500):                                        # Si el monto supera los 500
    print("El cambio fue beneficioso")
else:                                                   # Si el monto no supera los 500
    print("El cambio no fue beneficioso")

#output
print("El precio total de combio es:",soles," soles")
