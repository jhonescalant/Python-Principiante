# EJERCICIO 18. 
# Tarjeta de Bingo 
# Realizar un programa que genere 15 numero aleatorios enteros en el rango del 1 al 100, que representaria la tarjeta de 
# bingo de una persona. Una vez generado los numeros aleatorios solicitar al usuario que ingrese 3 numeros enteros, a parƟr de alli mostrar 
# los siguientes mensajes: Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador Ɵene mala suerte, no marco ninguna casilla”. 
# Caso contrario mostrar “El jugador marco algun numero de la tarjeta”. 

#librerias
import random

#varaibles
numero=0
primer_numero=0
segundo_numero=0
tercer_numero=0
cont=0

#Inicio del programa
print("      ** Ingresa los 3 numeros para poder reclamar tu premio **\n")
#Ingrese el primer numero 
primer_numero=int(input("Ingrese el primer numero:"))
#Ingrese el segundo numero 
segundo_numero=int(input("Ingrese el segundo numero:"))
#Ingrese el tercer numero 
tercer_numero=int(input("Ingrese el tercer numero:"))

print("  *** Estos son los 15 numeros de la tarjeta de numero ***")
for i in range(15):
    numero=random.randint(1,100)
    if (primer_numero==numero):
        cont+=1
    if (segundo_numero==numero):
        cont+=1
    if (tercer_numero==numero):
        cont+=1

    #Se imprime los 15 numeros aleatorios
    print (numero, end=" ") 

#Salida por pantalla 
print("\n Tus numeros son:",primer_numero , segundo_numero , tercer_numero)
if (cont > 0):
    print("\n ** El jugador marco algun numero de la tarjeta **")
else:
    print("\n ** El jugador tiene mala suerte, no marco ninguna casilla ")

#*********************************************************************************************************************************************    
#                                              P R U E B A      D E     E S C R I T O R I O            
#*********************************************************************************************************************************************        
#  primer_numero     segundo_numero      tercer_numero                       numero                                  cont
#        10               20                  85              95 4 86 38 41 25 2 95 75 52 44 32 32 64 81               0
#
#        10               20                  45              74 94 30 53 82 14 96 20 23 5 6 19 67 97 91               1
#
#
#


























