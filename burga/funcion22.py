# Ejercicio 22
import os
import libreria

# Calcular la contuctividad electrica
# Declaracion de datos

#imput
intensidad_corriente=int(os.sys.argv[1])
resistencia=int(os.sys.argv[2])
conductividad_electrica=libreria.conductividad_electrica(intensidad_corriente,resistencia)

#output
print("la condutividad electrica es de :",conductividad_electrica)
