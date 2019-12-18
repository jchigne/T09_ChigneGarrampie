# Ejercicio 16
import os
import libreria

# Calcular la aceleracion angular
# Declaracion de datos

#imput
v_angular=int(os.sys.argv[1])
radio=int(os.sys.argv[2])
a_angular=libreria.a_angular(v_angular,radio)

if (a_angular>=100):                                           # Si la aceleracion angular supera los 100
    print("El movimiento es veloz")
else:                                                         # Si la aceleracion angular no supera los 1000
    print("El movimiento  no es veloz")
#fin_if

#output
print("La aceleracion angular es:",a_angular)
