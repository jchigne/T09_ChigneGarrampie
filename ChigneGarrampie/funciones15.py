# Ejercicio 15
import os
import libreria

# Calcular la energia del reactor
# Declaracion de datos

#imput
masa=int(os.sys.argv[1])
velocidad=int(os.sys.argv[2])
energia=libreria.energia(masa,velocidad)

if (energia>=10000):                                          # Si el energia supera los 10000
    print("Se recomeindo apagar el reactor")

else:                                                         # Si el energia no supera los 10000
    print("El sistema es seguro")
#fin_if

#output
print("La energia del reactor es:",energia)
