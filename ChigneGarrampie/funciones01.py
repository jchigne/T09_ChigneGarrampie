# Ejercicio 01
import os
import libreria

# Calcular la fuerzas de las masas
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
fuerza=libreria.fuerza(masa,aceleracion)

#output
print("fuerza del cuerpo es:",fuerza)
