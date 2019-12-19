# Ejercicio 17
import os
import libreria

# Calcular la velocidad tangencial
# Declaracion de datos

#imput
longitud_arco=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
velocidad_tangencial=libreria.velocidad_tangencial(longitud_arco,tiempo)

#output
print("la velocidad tangencial es de :",velocidad_tangencial)
