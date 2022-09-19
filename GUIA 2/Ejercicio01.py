#Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado). Desarrollar un programa que 
# permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide: 
# a) Determinar y mostrar el nombre del ganador de la carrera.
# b) Ingresar por teclado el tiempo record registrado para dicha carrera. 
# Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje. 
# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.



#Variables
cant_comp=0
nombre_comp=""
tiempo_record=0.0
tiempo_carrera=0.0
maximo=0
minimo=999
tiempo_promedio=0.0
nombre_minimo=""
sumatoria_tiempo=0.0

#  Inicio del programa

print("          **  Carrera de ciclista  ** \n")
cant_comp=int(input("Ingrese la cantidad de competidores:"))#Ingrresamos la cantidad de competidores
tiempo_record=float(input("Ingrese el tiempo record:"))#Ingresamos el record de la carrera

print("         ** Ingreso de datos de los "+ str(cant_comp)+" ciclista ** \n")

for i in range(1,cant_comp+1):
    #Ingresamos el nombre del cada ciclista
    nombre_comp=str(input("Ingrese el nombre del ciclista:"))
    #Ingresamos el tiempo recorrido de los ciclista 
    tiempo_carrera=float(input("Tiempo del recorrido del ciclista:"))
    #sumamo los tiempos de cada cimpetidor para porde sacar un promedio
    sumatoria_tiempo+= tiempo_carrera
    
    #Hallamos a el competidor con menos tiempo de recorrido 
    if (tiempo_carrera < minimo):
        minimo=tiempo_carrera
        nombre_minimo=nombre_comp

tiempo_promedio = sumatoria_tiempo / cant_comp

if (minimo < tiempo_record):
    print("        ***  F E L I C I D A D E S  ***")
    print(nombre_minimo+" Por romper el record")
    print("Nuevo record:"+str(minimo))
else:
    print("El tiempo minimo es de: "+ str(minimo) +" del competidor: "+ nombre_minimo)
    print("Tiempo promedio:"+ str(tiempo_promedio))

#****************************************************************************************************************************************************
#                                                      P R U E B A    D E      E S C R I T O R I O 
#****************************************************************************************************************************************************
#  cant_comp      tiempo_record      nombre_comp     tiempo_carrera       sumatoria_tiempo      tiempo_promedio      minimo     nombre_minimo       
#      3               2.1               jhon              3.0                 3.0                 ---------          ----       -----------              
#                                        nico              2.2                 5.2                 ---------          ----       ----------- 
#                                        nick              1.7                 6.9                   2.3               1.7          nick
# 
# 
# 
# 
#







