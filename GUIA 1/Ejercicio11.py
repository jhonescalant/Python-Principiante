#EJERCICIO 11
# Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado.

#VARIABLES 
sueldo=0.0
ahorros=0.0
#INICIO DEL PROGRAMA 
print("Bienvenido al sistema de ahorro:")
for i in range(1,13):
    print("Ingrese el sueldo del mes ",i)
    #Se ingresa el suelgo del mes 
    sueldo=float(input("Sueldo mensual:"))
    #Se suma el 10% del sueldo de cada mes 
    ahorros+=sueldo*0.10 
#salida por pantalla 
print("El ahorro total del año es:$",ahorros)

#**********************************************************        
#        P R U E B A      D E     E S C R I T O R I O
#**********************************************************
#    i (mes)     sueldo    ahorros 
#       1         100         10
#       2         200         30                         
#       3         300         60   
#     

