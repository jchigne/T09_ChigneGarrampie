# Ejercicio 21
import os
import libreria

# Calcular la potencia
# Declaracion de datos

#imput
joule=int(os.sys.argv[1])
segundos=int(os.sys.argv[2])
potencia=libreria.potencia(joule,segundos)

#output
print("la potencia es de :",potencia)
