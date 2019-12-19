# Ejercicio 16
import os
import libreria

# Calcular el promedio de las notas de un alumno
# Declaracion de datos

#imput
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
promedio=libreria.promedio(nota1,nota2,nota3)

#output
print("el promedio de las notas es de:",promedio)
