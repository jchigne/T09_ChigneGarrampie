# Ejercicio 09
import os
import libreria

# El precio fianl de compras:
# Declaracion de datos

#imput
precio01=int(os.sys.argv[1])
precio02=int(os.sys.argv[2])
precio03=int(os.sys.argv[3])
monto2=libreria.monto(precio01,precio02,precio03)
if (monto2>=100):                                             #si el monto supera los 100, descuento del 10%
    print("Felicidades acedio al descuento del 10%")
else:
    print("Gracias por su compra")                           #si el monto no supera los 100, "Gracias por su compra"

if (monto2==500):
    print("Felicidades se gano un descuento del 25%")        #si supera los 500, descuento del 25%


#output
print("El monto toal es:",monto2)
