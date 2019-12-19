# Ejercicio 01
import os
import libreria

# Calcular el total de la compra de libros
# Declaracion de datos

#imput
libro1=int(os.sys.argv[1])
libro2=int(os.sys.argv[2])
total_precio=libreria.total_precio(libro1,libro2)

#output
print("la compra tottal de los libro fue de :",total_precio)
