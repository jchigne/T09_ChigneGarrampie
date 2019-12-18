# Ejercicio 06
import os
import libreria

# Calcula el promedio de 3 notas
# Declaracion de datos

#imput
nota01=int(os.sys.argv[1])
nota02=int(os.sys.argv[2])
nota03=int(os.sys.argv[2])
promedio=libreria.promedio(nota01,nota02,nota03)

#output
print("El promedio final es:",promedio)
