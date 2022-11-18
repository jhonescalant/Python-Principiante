# Programa que declare tres listas ‘lista1’, ‘lista2’ y ‘lista3’ de cinco enteros cada uno, pida valores para ‘lista1’ y ‘lista2’ y calcule lista3=lista1+lista2

# Variables
lista_uno=[]
lista_dos=[]
lista_tres=[]
num=0
suma=0

# Inicio del programa
print(" ****     NUMEROS DE LA PRIMERA LISTA       *****  ")
while len(lista_uno)<5:
    # Se solicita el ingreso de numeros para la primera lista
    num=int(input("Ingrese un numero para la primera lista:"))
    lista_uno.append(num)
print(" ****     NUMEROS DE LA SEGUNDA LISTA       *****  ")
while len(lista_dos)<5:
    # Se solicita el ingreso de numeros para la segunda lista
    num=int(input("Ingrese un numero para la segunda lista:"))
    lista_dos.append(num)
# Se hace las sumas de los valores de las lista
for i in range (0,5):
    suma=lista_uno[i]+lista_dos[i]
    print(f"suma:{lista_uno[i]}+{lista_dos[i]}")
    lista_tres.append(suma)

# Salida por pantalla
print(f"Primera lista:{lista_uno}")
print(f"Segunda lista:{lista_dos}")
print(f"Suma de las lista:{lista_tres}")

# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************
 ****     NUMEROS DE LA PRIMERA LISTA       *****  
Ingrese un numero para la primera lista:1  
Ingrese un numero para la primera lista:2
Ingrese un numero para la primera lista:3
Ingrese un numero para la primera lista:4 
Ingrese un numero para la primera lista:5
 ****     NUMEROS DE LA SEGUNDA LISTA       *****  
Ingrese un numero para la segunda lista:1
Ingrese un numero para la segunda lista:2
Ingrese un numero para la segunda lista:3
Ingrese un numero para la segunda lista:4
Ingrese un numero para la segunda lista:5

**********************************************************
                    P R O C E S O
***********************************************************

suma=1+1
suma=2+2
suma=3+3
suma=4+4
suma=5+5

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
Primera lista:[1, 2, 3, 4, 5]
Segunda lista:[1, 2, 3, 4, 5]
Suma de las lista:[2, 4, 6, 8, 10]

"""

