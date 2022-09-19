#EJERCICIO 14
#   Suma - División - Potencia 
#   Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir 
#   por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo

#VARIABLES
numero=0.0
suma=0.0
mayor_diez=0.0
menor_diez=0.0
#INICIO DEL PROGRAMA
for i in range(1,4):
    numero=int(input("Ingrese un nunmero:"))
    suma+=numero

if suma > 10 :
    mayor_diez= suma / 2
    print("Como el resultado es mayor a 10 el resultado es:",mayor_diez)
else:
    menor_diez= suma**3
    print("Como el resultado es menor a 10 el resultado es:",menor_diez)


#**************************************************************************************        
#                  P R U E B A      D E     E S C R I T O R I O
#**************************************************************************************
#   numero     suma      mayor_diez     menor_diez   
#     5          5       ---------       ---------
#     6          11      ---------       ---------
#     7          18          9           ---------
#    