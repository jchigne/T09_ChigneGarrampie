# Ejercicio 08
import os
import libreria

# Calcular la energia calorifica
# Declaracion de datos

#imput
trabajo=int(os.sys.argv[1])
energia_interna=int(os.sys.argv[2])
energia_calorifica=libreria.energia_calorifica(trabajo,energia_interna)

#output
print("la energia calorifica es de:",energia_calorifica)
