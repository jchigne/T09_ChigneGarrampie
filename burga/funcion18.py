# Ejercicio 18
import os
import libreria

# Calcular la velocidad angular
# Declaracion de datos

#imput
distancia_angular=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
velocidad_angular=libreria.velocidad_angular(distancia_angular,tiempo)

#output
print("la velocidad angular es de :",velocidad_angular)
