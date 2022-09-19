#EJERCICIO 2
#2) Cuadrado de un binomio, plantear un script directamente en el shell de python, que permita mostrar, para dos valores a y b;
#   Un binomio al cuadrado(suma) es igual al cudrado del primer termino, mas el doble producto del primer por el segundo mas el 
#   cuadrado del segundo 

#variables 
primer_num=0
segundo_num=0
resultado=0
#inicio del programa
print("Calculo del cuadrado de un binomio")
print("( 2           2)")
print("(a + 2xaxb + b )")
#Ingreso de valores por el ususario
primer_num=int(input("Ingresa el valor de A :"))
segundo_num=int(input("Ingresa el vlaor de B:"))
#Proceso del caudrado de un binomio 
resultado=((primer_num)**2 )+ (2 * primer_num *segundo_num )+ ((segundo_num)**2) 
#Salida por pantalla 
print("El resultado del cuadrado de un binomio es:",resultado)


#*****************************************************************      
#            P R U E B A      D E     E S C R I T O R I O
#*****************************************************************
#  primer_num      segun_num      resultado     
#       4              2            36              
#       8              3            121           
#       9              4            169            

