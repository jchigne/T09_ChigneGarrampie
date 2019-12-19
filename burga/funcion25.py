# Ejercicio 25
import os
import libreria

# Calcular el perimetro de un triangulo
# Declaracion de datos

#imput
lado1=int(os.sys.argv[1])
lado2=int(os.sys.argv[2])
lado3=int(os.sys.argv[3])
perimetro=libreria.perimetro(lado1,lado2,lado3)
#output
print("el perimetro del triangulo es de :",perimetro)
