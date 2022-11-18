# Secuencia de n números. 
# Ingresar una secuencia de n números, de a uno por vez. El valor de n se ingresa por teclado, validar que sea mayor a 0. Determinar: 
# a) Cuántos números ingresados terminan en 5
# b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia 
# c) Cuántos números ingresados son mayores al anterior.


# ****************************************************************************
#                        D   I   S   E   Ñ   O  
# ****************************************************************************

# Variables
cant_numeros=0
num_ingresado=0
terminan_cinco=0
primer_numero=0
repeticiones_1num=0
numero_anterior=0
num_mayor=0

# Inicio del programa 


cant_numeros=int(input("Ingrese la cantidad de numeros que desea ingresar:"))
while (cant_numeros<0):
    cant_numeros=int(input("ERROR ---- Ingrese la cantidad correcta: "))

for i in range(cant_numeros):

    num_ingresado=int(input("Ingrese un numero: "))
    while (num_ingresado<0):
        num_ingresado=int(input("ERROR --- Ingrese un numero:" ))

    if (num_ingresado % 10 == 5):
        terminan_cinco+=1

    if (i == 0):
        primer_numero=num_ingresado
    
    if (primer_numero== num_ingresado):
        repeticiones_1num+=1

    if ((i>0) and (numero_anterior < num_ingresado)):
        num_mayor+=1
    
    numero_anterior=num_ingresado 

# Salida por pantalla 
print("Cantidad de numeros que terminan en 5:"+str(terminan_cinco))
print("La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia:"+str(repeticiones_1num))
print("Cantidad números ingresados son mayores al anterior:"+str(num_mayor))



# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

'''
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************                          
Ingrese la cantidad de numeros que desea ingresar: 6
Ingresa un numero: 5
Ingresa un numero: 10
Ingresa un numero: 15
Ingresa un numero: 20
Ingresa un numero: 5
Ingresa un numero: 1

**********************************************************
                    P R O C E S O
***********************************************************
        cant_numeros = 0 | 6
    numero_ingresado = 0 | 5 | 10 | 15 | 20 | 5 | 1 
     numero_anterior = 0 | 5 | 10 | 15 | 20 | 5 | 1 
      terminan_cinco = 0 | 1 | 2  | 3
       primer_numero = 0 | 5
repeticiones_1numero = 0 | 1
           num_mayor = 0 | 1 | 2  | 3

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
Cantidad de numeros que terminan en 5: 3
La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia: 1
Cantidad de numeros que son mayores al anterior: 3

'''

    

    












