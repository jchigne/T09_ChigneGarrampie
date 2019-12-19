# Ejercicio 19
import os
import libreria

# Calcular el peso de un cuerpo
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])
peso=libreria.peso(masa,gravedad)

#output
print("el peso del cuerpo es de :",peso)
