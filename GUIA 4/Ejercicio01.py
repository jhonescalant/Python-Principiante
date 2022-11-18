# Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y posteriormente
# muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

# Variable 
import random
listas_numero=[]
numero_aleatorio=0
cuadrado=0
cubo=0

# Inicio del programa
while len (listas_numero)<10:
    numero_aleatorio=random.randint(1,10) 
    listas_numero.append(numero_aleatorio) # Se agrega el numero eleatorio a la lista
print(listas_numero)

for numero_aleatorio in listas_numero:
    cuadrado= numero_aleatorio**2
    cubo= numero_aleatorio**3
    print(f"Numero:{numero_aleatorio} - cuadrado:{cuadrado} - cubo:{cubo}")




# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

----------------------------------------------------------

**********************************************************
                    P R O C E S O
***********************************************************
listas_numero=[10, 5, 4, 1, 8, 9, 4, 4, 9, 9]
numero_aleatorio=10| 5| 4| 1| 8| 9| 4| 4| 9| 9|
        cuadrado=100|25 | 16| 1| 64| 81| 16| 16| 81| 81| 
            cubo=1000| 125| 64| 1| 512| 729| 64| 64| 729| 729|

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
[10, 5, 4, 1, 8, 9, 4, 4, 9, 9]
Numero:10 - cuadrado:100 - cubo:1000
Numero:5 - cuadrado:25 - cubo:125
Numero:4 - cuadrado:16 - cubo:64
Numero:1 - cuadrado:1 - cubo:1
Numero:8 - cuadrado:64 - cubo:512
Numero:9 - cuadrado:81 - cubo:729
Numero:4 - cuadrado:16 - cubo:64
Numero:4 - cuadrado:16 - cubo:64
Numero:9 - cuadrado:81 - cubo:729
Numero:9 - cuadrado:81 - cubo:729

"""









