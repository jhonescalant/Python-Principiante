#Menu de Opciones con secuencias. 
# Escribir un programa que le permita al usuario, a través de un menú de opciones, las siguientes operaciones: 
# a) Generar una serie n de números (n ingresado por teclado y validando que sea mayor a cero) y mostrar la suma de los cuadrados 
# b) Ingresar un texto finalizado por un punto y determinar la cantidad de palabras que finalizan con vocales 
# c) Ingresar una serie de números (la carga finaliza con cero) y determinar si hay mayor cantidad de valores pares o de impares 
# d) Salir



# Variables 
continuar="S"
opcion=""
num=0

# Inicio del programa

while (continuar!="N"):

    print(" **  MENU  DE  OPCIONES  ** ")
    print("""
        A)Generar una serie de numeros y la suma de los cuadrados
        B)Cantidad de palabras que finalizan con vocales
        C)Determinar si hay mayor cantidad de valores pares o de impares
        D)Salir 
    """)
    opcion=str(input("Elija una de las opciones:")).upper()
    while(opcion!="A" and opcion!="B" and opcion!="C" and opcion!="D" ):
        opcion=str(input("ERROR ----- Elija una de las opciones:")).upper()

    if (opcion!="D"):

        if (opcion=="A"):

            num=int(input("Ingrese un numero:"))
            while (num< 0):
                num=int(input("ERROR --- Ingrese un numero:"))

        
        if(opcion=="B"):
            texto=str(input("Ingrese el texto:"))
            



        

 

    continuar=str(input("Desea realizar otra operacion S/N:")).upper()
    while(continuar!="S" and continuar!="N"):
        continuar=str(input("ERROR ---- Desea realizar otra operacion S/N:")).upper()


































