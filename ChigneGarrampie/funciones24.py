# Ejercicio 23
import os
import libreria

# Calcular el area lateral de una piramide
# Declaracion de datos

#imput
pi=int(os.sys.argv[1])
radio=int(os.sys.argv[2])
generatris=int(os.sys.argv[3])
piramide=libreria.piramide(pi,radio,generatris)

if (piramide>=200):                                         # Si la piramide supera los 200
    print("La piramide es alta")
else:                                                         # Si la piramide no supera los 200
    print("La piramide es baja")
#fin_if

#output
print("El area lateral de la piramide es:",piramide)
