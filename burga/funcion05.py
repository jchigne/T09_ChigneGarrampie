# Ejercicio 05
import os
import libreria

# Calcular la resion hidrostatica
# Declaracion de datos

#imput
densidad_liquido=int(os.sys.argv[1])
gravedad=int(os.sys.argv[2])
altura=int(os.sys.argv[3])
presion_hidrostatica=libreria.presion_hidrostatica(densidad_liquido,gravedad,altura)

#output
print("la presion hidrostatica que ejerce hacia el cuerpo es:",presion_hidrostatica)
