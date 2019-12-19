# Ejercicio 01
import os
import libreria

# Calcular la fuerzas de las masas
# Declaracion de datos

#imput
trabajo=int(os.sys.argv[1])
foco_caliente=int(os.sys.argv[2])
eficiencia=libreria.eficiencia(trabajo,foco_caliente)

#output
print("la eficiencia del foco caliente es de :",eficiencia)
