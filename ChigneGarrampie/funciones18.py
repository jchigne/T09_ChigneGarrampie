# Ejercicio 18
import os
import libreria

# Calcula el volumen de una esfera
# Declaracion de datos

# imput
pi=int(os.sys.argv[1])
radio=int(os.sys.argv[2])
esfera=libreria.esfera(pi,radio)

# output
# si la esfera esgrande
if (esfera>100 or esfera<=300):
    print("La esfera es grande")
# si la esfera es pequeña
if (esfera<=100):
    print("La esfera  es pequeña")
# si la esfera es extragrande
if (esfera>=300 ):
    print("La esfera es ExtraGrabde")
#fin_if

print("El volumen de la esfera es:",esfera)
