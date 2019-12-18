# Ejercicio 04
import os
import libreria

# Calcula el costo fijo medio de la produccion
# Declaracion de datos

#imput
fijo=int(os.sys.argv[1])
produccion=int(os.sys.argv[2])
medio=libreria.medio(fijo,produccion)

#output
print("El costo fijo medio de produccion es:",medio)
