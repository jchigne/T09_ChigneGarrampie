# Ejercicio 01
import os
import libreria

# Calcular la carga que pasa por un conductor electrico
# Declaracion de datos

#imput
intensidad_corriente=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
carga=libreria.carga(intensidad_corriente,tiempo)

#output
print("lacarga del conductor es: ",carga)
