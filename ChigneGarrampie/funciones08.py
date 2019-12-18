# Ejercicio 08
import os
import libreria

# Calcula monto para el viaje:
# Declaracion de datos

#imput
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])
monto=libreria.monto(a,b,c)
if (monto>=100):                                             #si el monto supera los 100 abra viaje
    print("Si llegamos al monto requerido viajaremos")
else:
    print("No se llego al monto T.T")                        #si el monto no supera los 100 no viaje

if (monto>=300):
    print("Superamos los 300, abra almuerzo gratis")         # si supera los 300, almuerzos gratis


#output
print("El monto toal es:",monto)
