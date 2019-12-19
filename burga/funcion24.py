# Ejercicio 24
import os
import libreria

# Calcular la presion que ejerce un cuerpo
# Declaracion de datos

#imput
fuerza=int(os.sys.argv[1])
area=int(os.sys.argv[2])
presion=libreria.fuerza(fuerza,area)

#output
print("la presion es de :",presion)
