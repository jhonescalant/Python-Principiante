#EJERCICIO 7 
#Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.

# Variables
num=0
a=0
b=1
c=0
#Inicio del programa  
num=int(input("Ingrese un numero:"))
print(b)
for i in range(num-1):
    c= a+b
    a=b
    b=c
    print(b)


#**********************************************************       
#   P R U E B A      D E     E S C R I T O R I O
#***********************************************************
#   a   b   c  
#   1   1   1 
#   1   2   3
#   2   3   5
#   3   5   8
#   5   8   13



