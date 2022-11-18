#10.Búsqueda de mayor 
# Realizar un programa que permita buscar el mayor de 10.000 números 
# aleatorios generados en el rango de[0,100.000].

#Librerias

from random import randrange

#variables 
num=0
mayor=0

#Inicio del programa
for i in range (10000):
    #Genera nuemro aleatorios
    num=randrange(0,100000)
    #Utilizamos la funcion IF para poder guardar el numero en la variables mayor
    if (i==1):
        mayor=num
    #Comparamos la varible mayor con el numero generado y porder averiguar 
    #cual es mayor.
    if (mayor<num):
        mayor=num
#Salida por pantalla 
print("El numero mayor de los 10000 numeros es:"+str(mayor))

#********************************************************************************************************************************
#                              P R U E B A    D  E     E S C R I T O R I O 
#********************************************************************************************************************************
"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

No tiene ingreso de  datos 

**********************************************************
                    P R O C E S O
***********************************************************

Hasta 10000 numeros

      num=0|10|20|30|40 ....
    mayor=0|10|30|60|100....

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************

El numero mayor de los 10000 numeros es:

"""  

