#9.	Promedio de números aleatorios:
#  Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de[0,100000].


#librerias
from random import randrange

#variables
num=0
cant=0
sumatoria=0
promedio=0

#inicio del programa

for i in range (1000):
    #Genera numeros aleatorios de un rango de  0 a 100000
    num=randrange(0,100000)
    #contador de las cantidades de numeros creados
    cant+=1
    #Sumatorios de los nuemros  creados aleatoriamente
    sumatoria +=num
    #Calculo del promedio  
    promedio= sumatoria / cant

#Salida por pantalla    
print("el promedio es de :"+str(promedio))

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

hasta 1000 numeros

     cant=0|1 |2 | 3|4 .....
   numero=0|10|20|30|40 ....
sumatoria=0|10|30|60|100....
 promedio=0|10|15|20|25 ....

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************

El promedio es de:

"""  







