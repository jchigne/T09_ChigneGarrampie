# Ejercicio 09
import os
import libreria

# Calcular la potencia instantane de un cuerpo
# Declaracion de datos

#imput
fuerza=int(os.sys.argv[1])
velocidad=int(os.sys.argv[2])
potencia_instantanea=libreria.potencia_intantanea(fuerza,velocidad)

#output
print("la potencia instantanea es de :",potencia_instantanea)
