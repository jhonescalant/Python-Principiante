#Secuencia numérica. 
# Ingresar una secuencia de números, de a uno por vez, la carga finaliza cuando el usuario ingresa el cero. Determinar
# a) Porcentaje que representan los números divisibles por 3 sobre el total de números ingresados en la secuencia
# b) Determinar la cantidad de números que son el cuadrado del número anterior
# c) Determinar la posición del mayor elemento impar de la secuencia


# Variables 
num=1
cont=0
cant_numeros=0

# Inicio del programa 

while num != 0 :

    num=int(input("Ingrese un numero aleatorio: "))
    while num <0:
        num=int(input("ERROR --- Ingrese el numero correcto mayores a 0 (cero):  "))

    if num !=0:
        cant_numeros+=1
        if (num % 3 == 0):
            cont+=1

        # PUNTO B
         


        



        
        
        


print("Porcentaje de los numeros divisibles por 3:"+str(cont*100)/cant_numeros+"%")
print("cantidad de numeros que son el cuadrado del anterior:")
print("La posicion del mayor elemento impar de la secuencia:")