# Ejercicio 07
import os
import libreria

# Calcula descuento del:
# Declaracion de datos

#imput
precio=int(os.sys.argv[1])
descuento=int(os.sys.argv[2])
p_final=libreria.p_final(precio,descuento)

#output
print("El descuento es:",p_final)
