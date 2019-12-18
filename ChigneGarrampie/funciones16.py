# Ejercicio 16
import os
import libreria

# Calcular el volumen de una picina
# Declaracion de datos

#imput
largo=int(os.sys.argv[1])
ancho=int(os.sys.argv[2])
altura=int(os.sys.argv[3])
volumen=libreria.volumen(largo,ancho,altura)

if (volumen>=500):                                           # Si el volumen supera los 1000
    print("La picina es para adultos")
else:                                                         # Si el volumenno  no supera los 1000
    print("La picina es para niños")
#fin_if

#output
print("El volumen de la picina es:",volumen)
