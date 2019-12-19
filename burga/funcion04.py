# Ejercicio 04
import os
import libreria

# Calcular la potencia entregada
# Declaracion de datos

#imput
potencia_util=int(os.sys.argv[1])
potencia_perdida=int(os.sys.argv[2])
potencia_entregada=libreria.potencia_entregada(potencia_util,potencia_perdida)

#output
print("la potencia entregada de una maquina es :",potencia_entregada)
