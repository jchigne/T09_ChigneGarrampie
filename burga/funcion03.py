# Ejercicio 03
import os
import libreria

# Calcular la energia mecanica
# Declaracion de datos

#imput
energia_cinetica=int(os.sys.argv[1])
energia_potencial=int(os.sys.argv[2])
energia_mecanica=libreria.energia_mecanica(energia_cinetica,energia_potencial)

#output
print("la energia mecanica total es de : ",energia_mecanica)
