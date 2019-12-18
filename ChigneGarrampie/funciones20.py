# Ejercicio 20
import os
import libreria

# Compra de repuestos de autos
# Declaracion de datos

# imput
llantas=int(os.sys.argv[1])
parachoke=int(os.sys.argv[2])
ventanas=int(os.sys.argv[3])
espejos=int(os.sys.argv[4])
repuestos=libreria.repuestos(llantas,parachoke,ventanas,espejos)

# output
print("############################################")
print("#               TOYOTA                     #")
print("############################################")
print("# Llantas:",llantas,"$")
print("# Para choke:",parachoke,"$")
print("# Ventanas:",ventanas,"$")
print("# Espejos",espejos,"$")
print(" ############################################")
print("El total a pagar es:",repuestos)
print("#############################################")

# si la compra es de mas de 1000$ accede al sorteo de un auto 0 Km
if (repuestos>=1000):
    print("Felicidades accedio a un sorteo por un auto 0 Km")
else:
    print("Gracias por su compra")
