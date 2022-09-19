#EJERCICIO 3
#3) Area de un trinagulo desarrolle un programa para calcular el area de un triangulo, cargando por teclado el valor de la 
#   base, pero sabiendo que su altura es igual al cuadrado de la base

#variables
base_triangulo=0.0
area=0.0
altura=0.0
#inicio del programa
print("Sabiendo que la altura es el cuadrado de la base ")
#Ingreso de la base por el usuario
base_triangulo=float(input("Ingrese la base del triangulo:"))
#calculo de la altura
altura=((base_triangulo)**2)
print(altura)
#calculo del area 
area=(base_triangulo*altura)//2
#Salda por pantalla 
print("El area del triangulo es de:",area)

#*****************************************************************      
#            P R U E B A      D E     E S C R I T O R I O
#*****************************************************************
#  base_triangulo     altura    area    
#       4              16        32             
#       8              64       256             
#       9              81       364            

