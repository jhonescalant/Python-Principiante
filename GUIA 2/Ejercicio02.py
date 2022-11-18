#2.	Secuencia de impares. 
# Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre 
# ellos, en forma ascendente y descendente.


#Variables
primer_numero=0
segundo_numero=0
menor=0

#Inicio del programa

primer_numero=int(input("Ingrese el primer numero:")) #El usuario ingresa el primer numero 
segundo_numero=int(input("Ingrese el segundo numero:"))# Se ingresa el segundo numero 

#Si el primer numero es menor que el segundo 
if primer_numero < segundo_numero:

    #         Forma ascendente 
    print("     ** Forma ascendente  **")
    for i in range(primer_numero,segundo_numero):
        #Solo se imprimen los numeros impares 
        if (i % 2 != 0):
            print (i ,end=" ")

    #          forma descendente
    print("\n     **  Forma descendente  **")
    for x in range(segundo_numero-1,primer_numero,-1):
        if (x % 2 != 0):
            print (x ,end=" ")
else:
    #Si el primer numero es mayor que el otro
    if primer_numero > segundo_numero:
        # guardamos el numero mas chico en la variable menor
        menor=segundo_numero

    print("     ** Forma ascendente  **")
    for n in range(menor+1,primer_numero):
        if (n % 2 != 0):
            print (n ,end=" ")

    print("\n     **  Forma descendente  **")
    for m in range(primer_numero,segundo_numero,-1):
        if (m % 2 != 0):
            print (m ,end=" ")
        

#*************************************************************************
#      P R U E B A     D E    E S C R I T O R I O 
#*************************************************************************
"""
DATOS DE ENTRADAS:

Ingrese el primer numero=10
Ingrese el segundo numero=20

-------------------------------------------------------
PROCESOS:
primer_numero=10
segundo_numero=20

i= 11 13 15 17 19
x= 19 17 15 13 11
--------------------------------------------------------
SALIDA:
  ** Forma ascendente  **
 11 13 15 17 19
  ** Forma descendente  **
 19 17 15 13 11
"""




