# EJERCICIO 1
#1) Division con resto plantear un algoritmo que permita informar, para dos valores a y b el resultado de la dibision a/b y el
#   resto de esa divicion

#variables
primer_num=0
segun_num=0
resultado=0
resto=0
#Inicio del programa
print ("**Bienvenido al sistema de division**")

#Ingreso de datos por el usuario
primer_num=int(input("Ingrese el primer numero:"))
segun_num=int(input("Ingrese el segundo numero:"))

#Proceso de calculo
resultado= primer_num // segun_num
resto = primer_num % segun_num

#Salida por pantalla 
print("El resultado es de:",resultado)
print("El resto es de:",resto)

# comentarios



#*****************************************************************      
#            P R U E B A      D E     E S C R I T O R I O
#*****************************************************************
#  primer_num      segun_num      resultado     resto 
#       4              2              2           0 
#       8              3              2           2
#       9              4              2           1

