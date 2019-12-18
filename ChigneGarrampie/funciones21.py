# Ejercicio 21
import os
import libreria

# Compra total de futas
# Declaracion de datos

# imput
mansanas=int(os.sys.argv[1])
peras=int(os.sys.argv[2])
mangos=int(os.sys.argv[3])
platanos=int(os.sys.argv[4])
futas=libreria.frutas(mansanas,peras,platanos,mangos)


# output
print("############################################")
print("#             FRUTERIA FERNANDO            #")
print("############################################")
print("# Mansanas:",mansanas,"$")
print("# Peras:",peras,"$")
print("# Platanos:",platanos,"$")
print("# Mangos",mangos,"$")
print(" ############################################")
print("El total a pagar es:",futas)
print("#############################################")

# si la compra es de mas de 200$ accede al descuento de 10%
if (futas>=200):
    print("Felicidades por la compra de otros 100$\n se le descontaran 20$")
else:
    print("Gracias por su compra")
