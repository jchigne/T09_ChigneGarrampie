# Ejercicio 17
import os
import libreria

# Calcula los alumnos que aprueban el curso
# Declaracion de datos

# imput
nota01=int(os.sys.argv[1])
nota02=int(os.sys.argv[2])
nota03=int(os.sys.argv[3])
nota04=int(os.sys.argv[4])
final=libreria.final(nota01,nota02,nota03,nota04)

# output
# si el alumno tiene mas de 12, aprobo
if (final>=12):
    print("El alumno aprobo el curso")
# si el alumno tiene menos de 10, tendra que rendir sustitutorio
if (final<=10):
    print("El alumno tendra que dar sustitutorio")
# si el alumno tiene menos de 7, desaprobo el curso T.T
if (final<=7):
    print("El alumno desaprobo el curso \n y no tiene acceso al sutitutorio")
#fin_if

print("Promedio final:",final)
