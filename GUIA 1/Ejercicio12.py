#EJERCICIO 12
#Crear un conversor de pies y pulgadas a centímetros.

#Variables 
pies=0.0
pulgadas=0.0
centimetro=0.0
opcion=0

# Inicio del programa 
print("Convertidos de pies y pulgadas a centimetro")

#Menu de opciones
print("Medidas a convertir")
print("""
    1.Pies a centimetro
    2.Pulgadas a centimetro
""")
#opcion elegida por el usuario
opcion=int(input("Elija una de las opciones:"))


if (opcion==1):
    pies=float(input("Ingrese la medida en pies:"))#Ingreso de la mediadas en pies
    #Proceso de convercion de pies a centimetro
    centimetro=pies * 30.48 
    #Salida por pantalla
    print(str(pies)+" pies son:"+str(centimetro) +" cm")
else:
    pulgadas=float(input("Ingrese la medida en pulgadas:")) #Ingreso de las pulgadas
    #Proceso de convercion de pulgadas a centimetro
    centimetro=pulgadas * 2.54 
    #Salida por pantalla
    print(str(pulgadas)+" pies son: "+str(centimetro)+" cm")

#**********************************************************        
#        P R U E B A      D E     E S C R I T O R I O
#**********************************************************
#   opcion     pies       pulgadas     centimetro 
#     1         40                        1219.2
#     2                     40            101.6
#          
#     








