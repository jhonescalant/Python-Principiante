#EJERCICIO 5
#5) Conversión de medidas 
#    Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en: 
#   yardas pulgadas cenơmetros metros Sabiendo que: 
#   1 pie = 12 pulgadas 
#   1 yarda = 3 pies 
#   1 pulgada = 2.54 centímetros
#   1 metro =1000 centimetros

#VARIABLES
medida_pies=0
medida_pulgadas=0
medida_yarda=0
medida_centimetro=0
medida_metros=0
opcion=0
#inicio del programa
medida_pies=int(input("Ingrese la medidas en pies:"))   #El usuario ingresa los pies que desea convertir 
print("        Conversion de medidas")
# Menu de opcion
print("""
        1.PULGADAS
        2.YARDA
        3.CENTIMETRO
        4.METRO
    """)
# Ingreso de la opcion elegida por el usuario 
opcion=int(input("Ingrese la opcion que desea:"))

if opcion == 1 :
    # Pasaje de pies a pulgadas 
    medida_pulgadas= medida_pies * 12
    print("La medida es de:",medida_pulgadas,"pulgadas")
if opcion == 2 :
    # Pasaje de pies a yardas 
    medida_yarda= medida_pies * 3
    print("La medida es de:",medida_yarda,"yardas")
if opcion == 3 :
    # Pasaje de pies a centimetro 
    medida_pulgadas= medida_pies * 12  # Primero pasamos a pulgadas 
    medida_centimetro= medida_pulgadas * 2.54 # Una ves que lo pconvertimos en pulgadas lo podemos pasar a centimetros
    print("La medida es de:",medida_centimetro,"centimetros")
if opcion == 4 :
    # Pasaje de pies a pulgadas 
    medida_pulgadas= medida_pies * 12   # Primero lo pasamos a pulgadas
    medida_centimetro= medida_pulgadas * 2.54 # Depues lo pasamos a centimetro
    medida_metros=medida_centimetro / 1000 # Y por ultimo lo pasamos a centimetro 
    print("La medida es de:",medida_metros,"metros")


#*********************************************************************************************************        
#                               P R U E B A      D E     E S C R I T O R I O
#*********************************************************************************************************  
# medida_pies     opcion    medida_pulgadas     medida_yarda      medida_centimetro       medida_metros    
#      20           1            240       
#      20           2                                 60 
#      20           3            240                                    609.6
#      20           4            240                                    609.6                0.6096    
#                                             
                                           

