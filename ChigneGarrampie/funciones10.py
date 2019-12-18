# Ejercicio 10
import os
import libreria

# sueldo
# Declaracion de datos

#imput
horas=int(os.sys.argv[1])
p_horas=int(os.sys.argv[2])
sueldo=libreria.sueldo(horas,p_horas)

if (sueldo>=1000):                                        # si el empleador cobro mas de 1000$
    print("Gracias por su Trabajo")
    print("Felicidades se gano una semana de descanso")
else:                                                     # si el empleador no cobro mas de 1000$
    print("Gracias por su Trabajo")

#output
print("El sueldo total es:",sueldo)
