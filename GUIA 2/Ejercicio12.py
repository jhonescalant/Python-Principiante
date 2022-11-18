#12.	Números pares e impares 
# Se pide desarrollar un programa que permita leer una serie de números. 
# La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo. 
# Los requerimientos funcionales del programa son: 
# La sumatoria de solo los números que estén comprendidos entre 50 y 100. 
# Cantidad de valores pares ingresados. Cantidad de valores impares ingresados. 
# Informar si en la carga de números se ingreso al menos un número 0. 
# Informar si la serie contiene solo números pares e impares alternados.


# Variables
num=0
sumatoria=0
cant_pares=0
cant_ceros=0
# Inicio del programa


while (num>=0):
    num=int(input("Ingrese un numero:"))
    #Entra solamente si el numero es mayor a 0
    if (num>=0):
        #Solo suma los numero entre los valores de 50 y 100
        if(num>50 and num<100):
            #Se crea un acumalor para obtener la suma total de los numeros 
            sumatoria+=num
        
        if (num%2==0):
            #Se creo un contador para saber la cantidad de numeros 
            # pares fueron ingresados.
            cant_pares+=1
        
        if (num==0):
            #Se crea un contador para saber cuantos 0(ceros) fueron ingresados
            cant_ceros+=1
            




        
        
        










