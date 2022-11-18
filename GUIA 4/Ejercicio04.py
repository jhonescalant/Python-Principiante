# Programa que declare una lista y la vaya llenando de números hasta que introduzcamos un número negativo. 
# Entonces se debe imprimir el vector (sólo los elementos introducidos).

# Variables 
lista_numeros=[]
num_ingresados=0

# Inicio del programa
while(num_ingresados>-1):
    # Se pide al usuario que ingrese los numeros
    num_ingresados=int(input("Ingrese los numeros:"))
    # Solo agregamos los nuemros que sean mayores a -1 
    if (num_ingresados>-1):
        lista_numeros.append(num_ingresados)

# Salida por pantalla 
print(f"Lista de nuemros ingresados:{lista_numeros}")

# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

Ingrese los numeros:1
Ingrese los numeros:2
Ingrese los numeros:5
Ingrese los numeros:4
Ingrese los numeros:8
Ingrese los numeros:-1

**********************************************************
                    P R O C E S O
***********************************************************
lista_numeros=[1, 2, 5, 4, 8]
num_ingresados=1| 2| 5| 4| 8|-1

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
Lista de nuemros ingresados:[1, 2, 5, 4, 8]

"""
































