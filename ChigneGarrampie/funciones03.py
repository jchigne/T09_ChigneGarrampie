# Ejercicio 03
import os
import libreria

# Calcula el costo total de produccion
# Declaracion de datos

#imput
fijo=int(os.sys.argv[1])
variable=int(os.sys.argv[2])
total=libreria.total(fijo,variable)

#output
print("El costo total de produccion es:",total)
