# EJERCICIO 17
# Galería de Arte 
# Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba con tres cuadros y por 
# cada uno se ingresa el año en que fue creado. El programa deberá verificar si todos los cuadros son anteriores al siglo XX 
# (El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000). Determinar cuántos tienen antigüedad inferior a 10 años. 
# Si no hay ninguno, imprimir el mensaje “Renovar stock”.

#VARIABLES 
from ssl import _create_default_https_context


año_creacion=0
cant_antiguedad=0
cant_cuadros=0
# Inicio del programa

#Ingreso de la primera puntura
año_creacion=int(input("Ingrese el año de creacion del cuadro:"))
cant_cuadros+=1
if año_creacion <= 1891:
    cant_antiguedad+=1
    
#ingreso de la segunda pintura
año_creacion=int(input("Ingrese el año de creacion del cuadro:"))
cant_cuadros+=1
if año_creacion <= 1891:
    cant_antiguedad+=1
    
#Ingreso de las tercera pintura
año_creacion=int(input("Ingrese el año de creacion del cuadro:"))
cant_cuadros+=1
if año_creacion <= 1891:
    cant_antiguedad+=1
    

#Mensaje para renovar el stock de las pinturas del siglo  1891
if cant_antiguedad==0:
    print("Renovar stock")

#salida por pantalla
print("Cuadros anteriores del siglo XX:"+ str(cant_antiguedad))
print("Cantidad de caudros ingresados son:",cant_cuadros)




#******************************************************************    
#          P R U E B A      D E     E S C R I T O R I O            
#******************************************************************        
#   año_creacion       cant_cuadros      cant_antiguedad    
#      1800                1                   1
#      2000                2                   1
#      1560                3                   2
# 




