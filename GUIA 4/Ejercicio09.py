# Queremos guardar la temperatura mínima y máxima de 5 días. Realiza un programa que de la siguiente información:
# a) La temperatura media de cada día
# b) Los días con menos temperatura
# c) Se lee una temperatura por teclado y se muestran los días cuya temperatura máxima coincide con ella. si no existe ningún día se muestra un 
#    mensaje de información.

# varaibles 
lista_temperaturas=[]
list_temp_ordenada=[]
tem_minimo=0
tem_maxima=0
tem_media=0.0
temp_buscada=0

# Imicio del programa
for i in range(1,6):
    print(f"Dia:{i}")
    tem_minimo=int(input("Ingrese la temperatura minima:"))
    tem_maxima=int(input("Ingrese la temperatura maxima:"))

    tem_media=(tem_minimo+tem_maxima)/2
    # Imprimimo la temperatura media 
    print(f"La temperatura media:{tem_media}")
    # Agregamos cada elemto la a lista dentro de una sublista
    lista_temperaturas.append([tem_minimo,tem_maxima,i])

# Ordenamos la lista 
print(lista_temperaturas)
lista_temperaturas.sort()
list_temp_ordenada.extend(lista_temperaturas)
print(list_temp_ordenada)

# Salida por pantalla
print("\n  **  Dias con menos tempreaturas  **")
print(f"Dia:{list_temp_ordenada[0][2]} con una temperatura:{list_temp_ordenada[0][0]}")
print(f"Dia:{list_temp_ordenada[1][2]} con una temperatura:{list_temp_ordenada[1][0]}")

# Solicitamos al usuario que ingrese la temperatura que desea buscar
temp_buscada=int(input("Ingrese la temperaura que busca:"))

# Utilizamos el for para recorrer la listas
for i in lista_temperaturas:
    # comparamos la temperatura que busca y compararlo con cada sublista 
    if (i[1] == temp_buscada):      
        print(f"Dia {i[2]}: coincide la temperatura maxima")
    else:
        print(f"Dia {i[2]}: no coincide la temperatura maxima")


# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************
Dia:1
Ingrese la temperatura minima:10
Ingrese la temperatura maxima:25
Dia:2
Ingrese la temperatura minima:12
Ingrese la temperatura maxima:30
Dia:3
Ingrese la temperatura minima:14
Ingrese la temperatura maxima:26
Dia:4
Ingrese la temperatura minima:22
Ingrese la temperatura maxima:23
Dia:5
Ingrese la temperatura minima:21 
Ingrese la temperatura maxima:34
**********************************************************
                    P R O C E S O
***********************************************************
lista_temperaturas=[[10, 25, 1], [12, 30, 2], [14, 26, 3], [22, 23, 4], [21, 34, 5]]
list_temp_ordenada=[[10, 25, 1], [12, 30, 2], [14, 26, 3], [21, 34, 5], [22, 23, 4]]
        tem_minimo=10|12|14|22|21|
        tem_maxima=25|30|26|23|34|
         tem_media=17.5|21.0|20.0|22.5|27.5|
      temp_buscada=12

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
La temperatura media:17.5  
La temperatura media:21.0
La temperatura media:20.0
La temperatura media:22.5
La temperatura media:27.5

   **  Dias con menos tempreaturas  **
Dia:1 con una temperatura:10
Dia:2 con una temperatura:12

Dia 1: no coincide la temperatura maxima
Dia 2: no coincide la temperatura maxima
Dia 3: no coincide la temperatura maxima
Dia 5: no coincide la temperatura maxima
Dia 4: no coincide la temperatura maxima
"""












