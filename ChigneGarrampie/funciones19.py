# Ejercicio 19
import os
import libreria

# Calcula el total a pagar en el restaurante
# Declaracion de datos

# imput
entrada=int(os.sys.argv[1])
almuerzo=int(os.sys.argv[2])
postre=int(os.sys.argv[3])
refresco=int(os.sys.argv[4])
comida=libreria.comida(entrada,almuerzo,postre,refresco)

# output
# Si le sobro o no dinero para el pasaje
if (comida>=50):
    print("Me quede sin pasage , me toca ir en pedrito")
else:
    print("El almuerzo estubo delicioso ")
#fin_if
print("############################################")
print("#      Reustaurante Diaz Sanchez           #")
print("############################################")
print("# Entrada:",entrada,"$")
print("# Amuerzo:",almuerzo,"$")
print("# Postre:",postre,"$")
print("# Refresco",refresco,"$")
print(" ############################################")
print("El total a pagar por el almuerzo es:",comida)
print("#############################################")
