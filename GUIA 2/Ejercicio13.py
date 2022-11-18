#13.Desarrollar un programa que permita procesar los datos del último censo de un apequeña población.
# Por cada habitantes e ingresa:
# sexo(M/F)y edad. 
# La carga de datos analiza al ingresar cualquier otro valor para sexo.
# El programa debe informar:Aqué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)
# Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.

# Variables
sexo=""
edad=0
cant_masculino=0
cant_femenino=0
cant_escolar=0
cant_mayores=0
continuar="S"
maximo=0
minimo=0
sexo_correspondiente=""

# Inicio del programa 
print("  **  Beinvenido al sistema de censo  **  ")
while (continuar!="N"):

    sexo=str(input("Ingrese el sexo de la persona M/F:")).upper()
    while (sexo=="M" and sexo=="F"):
        sexo=str(input("ERROR---- Ingrese entre M/F "))

    edad=int(input("Ingrese la edad de la persona:"))
    while (edad<0):
        edad=int(input("ERROR ---- Ingrese la edad correcta:"))

    if(sexo=="M"):
        cant_masculino+=1

    if(sexo=="F"):
        cant_femenino+=1
    
    if(cant_masculino==1 and cant_femenino==0):
        maximo=cant_masculino
        minimo=cant_masculino

    if(cant_masculino==0 and cant_femenino==1):
        maximo=cant_femenino
        minimo=cant_femenino

    if (maximo<cant_masculino):
        maximo=cant_masculino
        sexo_correspondiente="Masculino"

    if(maximo<cant_femenino):
        maximo=cant_femenino
        sexo_correspondiente="Femenino"
    
    if (edad>=4 and edad<=18 and sexo=="F"):
        cant_escolar+=1   

    if (edad>80 and sexo=="M"):
        cant_mayores+=1 

    continuar=input("Desea conotinuar S/N:").upper()
    while (continuar!="S"  and continuar!="N" ):
        continuar=input("ERROR ---- Ingrese los datos correctos S/N:")    

# SALIDA POR PANTALLA
print ("El sexo con mas habitantes es de: "+str(sexo_correspondiente)+" de "+str(maximo))
print ("Cantidad de mujeres en edad escolar: "+str(cant_escolar))
print("Personas mayores  de 80 años: "+str(cant_mayores))


























