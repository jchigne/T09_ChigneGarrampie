# Ejercicio 01
import os
import libreria

# Calcular la cantidad de sustancia
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
masa_molecular=int(os.sys.argv[2])
cantidad_sustancia=libreria.cantidad_sustancia(masa,masa_molecular)

#output
print("la cantidad de sustancia es de :",cantidad_sustancia)
