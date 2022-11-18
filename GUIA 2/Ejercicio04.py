#4.	Decimal a Hexadecimal: 
# Generar n números aleatorios entre el rango de 5000 y 450000, por cada uno de ellos mostrar y 
# generar el numero hexadecimal.

#Librerias
from random import randrange 

#Variables 

numero=0
num_aleatorio=0
letra=""
resto=0
cociente=0
# Inicio del programa

print(" **  Decimal a Hexadecimal  ** ")

numero=int(input("Ingrese la cantidad de numeros aleatorios:"))
print(" ** Numeros aleatorios ** ")



for i in range (numero):
    num_aleatorio=randrange(5000,450000)
    resto=num_aleatorio % 16
    cociente=num_aleatorio//16

    if resto == 10:
        letra= "A"

    if resto == 11:
        letra= "B"

    if resto == 12:
        letra= "C"

    if resto == 13:
        letra= "D"

    if resto == 14:
        letra= "E"

    if resto == 15:
        letra= "F"

    print("Numero decimal: "+str(num_aleatorio)+" Numero hexadecimal: "+""+str(resto)+""+letra)
   

       
   
























