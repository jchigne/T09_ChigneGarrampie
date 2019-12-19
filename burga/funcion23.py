# Ejercicio 23
import os
import libreria

# Calcular la variacion de velocidades
# Declaracion de datos

#imput
velocidad_final=int(os.sys.argv[1])
velocidad_inicial=int(os.sys.argv[2])
variacion_velocidad=libreria.variacion_velocidad(velocidad_final,velocidad_inicial)

#output
print("la variacion de la velocidad es de ",variacion_velocidad)
