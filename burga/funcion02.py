# Ejercicio 02
import os
import libreria

# Calcular la energia potencial
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])
altura=int(os.sys.argv[3])
energia_potencial=libreria.energia_potencial(masa,gravedad,altura)

#output
print("la energia potencial de un cuerpo es:",energia_potencial)
