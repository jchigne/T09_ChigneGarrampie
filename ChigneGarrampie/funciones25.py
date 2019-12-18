# Ejercicio 20
import os
import libreria

# Compra utiles escolares
# Declaracion de datos

# imput
cuadernos=int(os.sys.argv[1])
lapices=int(os.sys.argv[2])
colores=int(os.sys.argv[3])
libros=int(os.sys.argv[4])
utiles=libreria.utiles(cuadernos,lapices,colores,libros)

# output
print("############################################")
print("#               LIBRERIA                   #")
print("############################################")
print("# Cuadernos:",cuadernos,"$")
print("# Lapices:",lapices,"$")
print("# Colores:",colores,"$")
print("# Libros",libros,"$")
print(" ############################################")
print("El total a pagar es:",utiles)
print("#############################################")
