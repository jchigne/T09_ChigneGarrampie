# Ejercicio 13
import os
import libreria

# Calcular  la cantidad de animales cuadrupedos
# Declaracion de datos

#imput
patas=int(os.sys.argv[1])
animales=libreria.animales(patas)

#output
print("El numero de animales cuadrupedos es:",animales)
