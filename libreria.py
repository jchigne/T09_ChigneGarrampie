# EJERCICIO 01
def fuerza (masa,aceleracion):
    fuerza=(masa*aceleracion)
    return fuerza
# fin fuerza


# EJERCICIO 02
def distancia (velocidad,tiempo):
    distancia=(velocidad*tiempo)
    return distancia
# fin distancia


# EJERCICIO 03
def total (fijo,variable):
    total=(fijo+variable)
    return total
# fin costo total


# EJERCICIO 04
def medio(fijo,produccion):
    medio=(fijo/produccion)
    return medio
# fin costo fijo medio


# EJERCICIO 05
def calor(masa,v_temperatura,c_especifico):
    calor=(masa*v_temperatura*c_especifico)
    return calor
# fin calor


# EJERCICIO 06
def promedio(nota01,nota02,nota03):
    promedio=(nota01+nota02+nota03)/3
    return promedio
# fin promedio


# EJERCICIO 07
def p_final(precio,descuento):
    p_final=precio-((precio*descuento)/100)
    return p_final
# fin precio final


# EJERCICIO 08
def monto(a,b,c):
    monto=(a+b+c)
    return monto
# fin monto


# EJERCICIO 09
def monto2(precio01,precio02,precio03):
    monto2=(precio01+precio02+precio03)
    return monto2
# fin compras


# EJERCICIO 10
def sueldo(horas,p_horas):
    sueldo=(horas*p_horas)
    return sueldo
# fin sueldo por horas de trabajo


# EJERCICIO 11
def pintado(paredes,p_paredes):
    pintado=(paredes*p_paredes)
    return pintado
# fin pintado de interiores


# EJERCICIO 12
def soles(dolares,cambio):
    soles=(dolares*cambio)
    return soles
# fin cambio de dolares


# EJERCICIO 13
def animales(patas):
    animales=(patas)/4
    return animales
# fin animeles cuadrupedo


# EJERCICIO 14
def voltaje(intensidad,resistencia):
    voltaje=(intensidad*resistencia)
    return voltaje
# fin volteje


# EJERCICIO 15
def energia(masa,velocidad):
    energia=(masa*velocidad*velocidad)
    return energia
# fin energia


# EJERCICIO 16
def volumen(largo,ancho,altura):
    volumen=(largo*ancho*altura)
    return volumen
# fin volumen de la picina


# EJERCICIO 17
def final(nota01,nota02,nota03,nota04):
    final=(nota01+nota02+nota03+nota04)/4
    return final
# fin promedio final con sustitutorio


# EJERCICIO 18
def esfera(pi,radio):
    esfera=(pi*radio*radio*radio)*4/3
    return esfera
# fin Volumen esfera


# EJERCICIO 19
def comida(entrada,almuerzo,postre,refresco):
    comida=(entrada+almuerzo+postre+refresco)
    return comida
# fin total a pagar en el restaurante


# EJERCICIO 20
def repuestos(llantas,parachoke,ventanas,espejos):
    repuestos=((llantas)*4+(parachoke)*2+ventanas+(espejos)*2)
    return repuestos
# fin total a pagar por los repuestos

# EJERCICIO 21
def frutas(mansanas,peras,mangos,platanos):
    frutas=(mansanas+mangos+peras+platanos)
    return frutas
# fin total a pagar por frutas


# EJERCICIO 22
def a_angular(v_angular,radio):
    a_angular=((v_angular*v_angular)*radio)
    return a_angular
# fin aceleracion angular

# EJERCICIO 23
def centripeta(a_centripeta,masa):
    centripeta=(masa*a_centripeta)
    return centripeta
# fin Fuerza centripeta


# EJERCICIO 24
def piramide(pi,radio,generatris):
    piramide=(pi*radio*generatris)
    return piramide
# fin Area lateral de una piramide


# EJERCICIO 25
def utiles(cuadernos,lapices,colores,libros):
    utiles=(cuadernos+lapices+colores+libros)
    return utiles
# fin utiles escolares


"""" #####################################################################
     #                   Libreria de Burga Muñoz                         #
     #####################################################################  """


#EJERCICIO 01
def precio_total(producto01,produco02,producto03):
    precio_total=(producto01+produco02+producto03)
    return precio_total
#fin del precio_total


#EJERCICIO 02
def energia_potencial(masa,gravedad,altura):
    energia_potencial(masa*gravedad*altura)
    return energia_potencial
#fin de la energia potencial


#EJERCICIO 03
def energia_mecanica(energia_cinetica,energia_potencial):
    energia_mecanica=(energia_cinetica+energia_potencial)
    return energia_mecanica
#fin de la energia mecanica


#EJERCICIO 04
def potencia_entregada(potencia_util,potencia_perdida):
    potencia_entregada=(potencia_util+potencia_perdida)
    return potencia_entregada
#fin de la potencia entregada



#EJERCICIO 05
def presion_hidrostatica(densidad_liquido,gravedad,altura):
    presion_hidrostatica=(densidad_liquido*gravedad*altura)
    return presion_hidrostatica
#fin de la presion hidrostatica



#EJERCICIO 06
def densidad(masa,volumen):
    densidad=(masa/volumen)
    return densidad
#fin de la densidad


#EJERCICIO 07
def densidad_sustancia(densidad_relativa,densidad_agua):
    densidad_sustancia=(densidad_relativa*densidad_agua)
    return densidad_sustancia
#fin de la densidad de la sustancia




#EJERCICIO 08
def energia_calorifica(trabajo,energia_interna ):
    energia_calorifica=(trabajo+energia_interna)
    return energia_calorifica
#fin de la energia calorifica de un cuerpo


#EJERCICIO 09
def potencia_instantanea(fuerza,velocida):
    potencia_instantanea=(fuerza*velocida)
    return potencia_instantanea
#fin de la potencia instantanea



#EJERCICIO 10
def modulo(fuerza,distancia):
    modulo=(fuerza*distancia)
    return modulo
#fin del modulo



#EJERCICIO 11
def carga(intensidad_corriente,tiempo):
    carga=(intensidad_corriente*tiempo)
    return carga
#fin de la carga



#EJERCICIO 12
def area(base,altura):
    area=(base*altura)
    return area
#fin del area


#EJERCICIC 13
def cantidad_sustancia(masa,masa_molecular):
    cantidad_sustancia=(masa/masa_molecular)
    return cantidad_sustancia
#fin de la cantidad de sustancia


#EJERCICIO 14
def total_precio(libro1,libro2):
    total_precio(libro1+libro2)
    return total_precio
#fin del precio total de los libros


#EJERCICIO 15
def eficiencia(trabajo,foco_caliente):
    eficiencia(trabajo/foco_caliente)
    return eficiencia
#fin de la eficiencia del foco caliente



#EJERCICIO 16
def promedio(nota1,nota2,nota3):
    promedio(nota1+nota2+nota3/3)
    return promedio
#fin del promedio de las notas



#EJERCICIO 17
def velocidad_tangencial(longitud_arco,tiempo):
    velocidad_tangencial=(longitud_arco/tiempo)
    return velocidad_tangencial
#fin de la velocidad tangencial



#EJERCICIO 18
def velocidad_angular(distancia_angular,tiempo):
    velocidad_angular(distancia_angular/tiempo)
    return velocidad_angular
#fin de la velocidad angular


#EJERCICIO 19
def peso(masa,gravedad):
    peso(masa*gravedad)
    return peso
#fin del peso



#EJERCICIO 20
def fuerza_razonamiento(constante,normal):
    fuerza_razonamiento(constante*normal)
    return fuerza_razonamiento
#fin de l afuerza de razonamiento



#EJERCICIO 21
def potencia(joule,segundos):
    potencia=(joule/segundos)
    return potencia
#fin de la potencia


#EJERCICIO 22
def conductividad_electrica(intensdad_corriente,resistencia):
    conductividad_electrica=(intensdad_corriente*resistencia)
    return conductividad_electrica
#fin de la conductividad electrica


#EJERCICIO 23
def variacion_velocidad(velocidad_final,velocidad_inicial):
    variacion_velocidad=(velocidad_final-velocidad_inicial)
    return variacion_velocidad
#fin de la variacion de la velocidad


#EJERCICIO 24
def presion(fuerza,area):
    presion=(fuerza/area)
    return presion
#fin de la presion


#EJERCICIO 25
def perimetro(lado1,lado2,lado3):
    perimetro=(lado1+lado2+lado3)
    return perimetro
#fin del perimetro
