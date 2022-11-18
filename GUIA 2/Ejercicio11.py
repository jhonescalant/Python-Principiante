#11.Menores y promedio 
# Realizar un programa que genere 5000 numeros aleatorios en el rango de [0,100000] y que permita:
# Determinar el menor de los numeros genera dos en forma aleatoria.Calcular el valor promedio de los números menores a 10.000.

# Libreria
from random import randrange
# Variables
num=0
menor=0
promedio=0
sumatoria=0
cant=0

# Inicio del programa
for i in range (0,5000):
    #Se genera numeros aleatorios
    num=randrange(0,100000)
    #se guarda el primero numero en la variable menor 
    if( i == 1):
        menor=num
    #Comparamos la variable menor y num
    if (menor > num):
        #Si menor > num se reemplaza el valor de menor por el de num
        menor=num

    if (num < 10000):
        #Contador de numeros a 10000
        cant+=1
        #sumamos los numeros 
        sumatoria+=num
        #Calculamos el promedio de los numeros 
        promedio= sumatoria / cant

#Salida por pantalla
print("El numero menor de los 5000 numeros es: "+str(menor))
print("El promedio de los numeros menores a 10000 es de : "+str(promedio))


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

El numero menor de los 5000 numeros es:
El promedio de los numeros menores a 10000 es de :

"""






