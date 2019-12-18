# Ejercicio 05
import os
import libreria

# Calcula calor de la masa
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
v_temperatura=int(os.sys.argv[2])
c_especifico=int(os.sys.argv[2])
calor=libreria.calor(masa,c_especifico,v_temperatura)

#output
print("El calor dinal del cuerpo es:",calor)
