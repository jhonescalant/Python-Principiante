#6.	Mostrar por pantalla el promedio de los números ingresados por teclado. 
# Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero).

#variables
cant=0
numero=1
promedio=0
sumatoria=0
#Inicio del programa 
  
print("  **   Ingrese el 0 (cero) para finalizar  **  ")
while (numero>0): #Mientra numero sea mayor a 0  se ejecuta el WHILE
    if (numero >0 ):#Si el el numero sea mayor a 0 se ejecuta  el if
        #Contador de los numeros ingresados por el usuario
        cant+=1
        #el usuario ingresa el numero
        numero=int(input("Ingrese un numero:"))
        #suma de los numeros ingresados por el usuario
        sumatoria+=numero
        #Calculo del promedio 
        promedio=sumatoria/cant
        #Salida por pantalla mostrando el promedio 
        print(" El promedio de los numeros ingresados es:"+str(round(promedio,1)))

#El programa finalizo ingresando 0
print(" ** PROGRAMA  FINALIZADO ** ")

#********************************************************************************************************************************
#                              P R U E B A    D  E     E S C R I T O R I O 
#********************************************************************************************************************************
"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

Ingrese un numero:10
Ingrese un numero:20
Ingrese un numero:30
Ingrese un numero:40
Ingrese un numero:0

**********************************************************
                    P R O C E S O
***********************************************************

     cant=0|1 |2 | 3|4 
   numero=0|10|20|30|40 
sumatoria=0|10|30|60|100
 promedio=0|10|15|20|25 

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************

El promedio de los numeros ingresados es:10
El promedio de los numeros ingresados es:15
El promedio de los numeros ingresados es:20
El promedio de los numeros ingresados es:25

"""




