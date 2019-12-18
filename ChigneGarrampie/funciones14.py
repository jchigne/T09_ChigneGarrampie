# Ejercicio 14
import os
import libreria

# Calcular el volteje
# Declaracion de datos

#imput
intensidad=int(os.sys.argv[1])
resistencia=int(os.sys.argv[2])
voltaje=libreria.voltaje(intensidad,resistencia)

if (voltaje>=200):                                        # Si el volteje supera los 200v
    print("Puede que haga corte circuito")
else:                                                     # Si el voltaje no supera los 200v
    print("No hay peligro de corte")
#fin_if

#output
print("El volteje de corriente electrica es:",voltaje)
