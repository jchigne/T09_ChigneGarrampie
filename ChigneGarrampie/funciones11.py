# Ejercicio 11
import os
import libreria

# Calcular el costo total del pintado de interiores
# Declaracion de datos

#imput
paredes=int(os.sys.argv[1])
p_paredes=int(os.sys.argv[2])
pintado=libreria.pintado(paredes,p_paredes)

if (pintado>=900):                                        # Si el monto es de 900 se pinton bien
    print("Gracias por su trabajo")
else:                                                     # Si el monto no es de 900 falto
    print("Falto pintar un cuarto")

#output
print("El costo total del pintado de \n interiores es:",pintado)
