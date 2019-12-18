# Ejercicio 23
import os
import libreria

# Calcular la fuerza centripeta
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
a_centripeta=int(os.sys.argv[2])
centripeta=libreria.centripeta(masa,a_centripeta)

if (centripeta>=2000):                                         # Si la Fuerza centripeta supera los 2000
    print("La fuerza ejercida es demasiada")
else:                                                         # Si la Fuerza centripeta no supera los 2000
    print("La fuerza ejercida es la ideal")
#fin_if

#output
print("La fuerza centripeta es:",centripeta)
