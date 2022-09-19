#EJERCICIO 6
#Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar.

nombre=""
contador=0
#Inicio del programa 
print("Cantidad de letras de los nombres")
#El usuario ingresa el nombre
nombre=str(input("Ingrese su nombre:"))
#La variable i tomara el valor de cada caracter del nombre ingresado
for i in nombre:
    #cuenta la cantidad de letras
    contador+=1
#Salida por pantalla
if (contador % 2 == 0):
    print("la cantidad de letras es par ")
else:
    print("La cantidad de letras es impar")


#**********************************************************       
#   P R U E B A      D E     E S C R I T O R I O
#***********************************************************
#    nombre     contador
#      jhon         4
#   florencia       9
#    
#     


