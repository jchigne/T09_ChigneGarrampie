# Ejercicio 07
import os
import libreria

# Calcular la densidad de la sustancia
# Declaracion de datos

#imput
densidad_relativa=int(os.sys.argv[1])
densidad_agua=int(os.sys.argv[2])
densidad_sustancia=libreria.densidad_sustancia(densidad_relativa,densidad_agua)

#output
print("la densidad de la sustancia es de ",densidad_sustancia)
