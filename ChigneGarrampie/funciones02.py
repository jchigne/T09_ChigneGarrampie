# Ejercicio 02
import os
import libreria

# Calcula la distancia recorrida
# Declaracion de datos

#imput
velocidad=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
distancia=libreria.distancia(velocidad,tiempo)

#output
print("La distancia recorrida es:",distancia)
