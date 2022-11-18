# Vamos a crear un programa que tenga el siguiente menú:
# 1.	Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
# 2.	Añadir número de la lista en una posición: Me pide un número y una posición, y si la posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
# 3.	Longitud de la lista: te muestra el número de elementos de la lista.
# 4.	Eliminar el último número: Muestra el último número de la lista y lo borra.
# 5.	Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de ella (la posición se pide a partir de 1).
# 6.	Contar números: Te pide un número y te dice cuantas apariciones hay en la lista.
# 7.	Posiciones de un número: Te pide un número y te dice en que posiciones está (contando desde 1).
# 8.	Mostrar números: Muestra los números de la lista
# 9.	Salir


#variables
opcion=0
num_eliminado=0
suma=0
lista_numeros=[]
# Inicio del programa


while (opcion!=9):
    #  MENU DE OPCIONES 

    print("""
        1.Añadir numero a la lista
        2.Añadir numero a la lista con una posicion determina
        3.Longitud de las lista
        4.Eliminar el ultimo numero
        5.Eliminar un numero
        6.contar numeros
        7.Posicion de un numero
        8.mostrar numeros
        9.salir
    """) 

    opcion=int(input("Ingrese una de las opciones:"))


    if (opcion!=9):
        if(opcion==1):
            print(" ***  Añadir un numero a la lista  ***")
            num=int(input("numero="))
            lista_numeros.append(num)
        
        if(opcion==2):
            print( "***** sjklghbdfkjghadfjk *******")
            print(lista_numeros)
            num=int(input("numero="))
            posicion=int(input("Ingrese la posicion:"))
            lista_numeros.insert(posicion,num)

            print(lista_numeros)
        
        if(opcion==3):
            print(f"longitud de la lista:{len(lista_numeros)} ")

        if (opcion==4):
            print("eliminar")
            print(f"lista:{lista_numeros}")

            num_eliminado=lista_numeros.pop()
            print(num_eliminado)

            print(lista_numeros)

        if(opcion==5):
            print(f"lista:{lista_numeros}")
            posicion=int(input("posicion de num: "))
            for i in range(len(lista_numeros)):
                if (i == posicion-1): 
                    lista_numeros.pop(posicion-1)


                    
        if(opcion==6):
            for i in range(len(lista_numeros)):
                suma+=lista_numeros[i]

            

    


    else:
        print("FIN DEL PROGRAMA")
























