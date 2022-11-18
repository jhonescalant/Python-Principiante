#Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores)
# y posterior ordene los elementos de menor a mayor.

# Librerias
import random

# Variables 
lista_numeros=[]
num_aleatorios=0
k=0
x=5
auxiliar=0

# Inicio del programa
while len (lista_numeros)<4:
    num_aleatorios=random.randint(1,1000)
    lista_numeros.append(num_aleatorios)
print(lista_numeros)

# Metodo burbuja 
# Bucle para el recorrido 
for i in range(0,3):  
    print("   **  valor de i:"+str(i)) 
    # Comparacion e intercambios
    for j in range(0,3): 
        print("valor de j:"+str(j))         
        if (lista_numeros[j] > lista_numeros[j+1]):
            print(lista_numeros)
            auxiliar=lista_numeros[j]
            lista_numeros[j]=lista_numeros[j+1]
            lista_numeros[j+1] = auxiliar 


print(lista_numeros)


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
[957, 278, 341, 935]
   **  valor de i:0 
valor de j:0        
[957, 278, 341, 935]
valor de j:1        
[278, 957, 341, 935]
valor de j:2        
[278, 341, 957, 935]
   **  valor de i:1
valor de j:0
valor de j:1
valor de j:2
   **  valor de i:2
valor de j:0
valor de j:1
valor de j:2
[278, 341, 935, 957]


**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
[957, 278, 341, 935]
[278, 341, 935, 957]

"""
    






















