# Diseñar el algoritmo correspondiente a un programa, que:
# a) Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# b) Carga la tabla con valores numéricos enteros.
# c) Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

# Varables
matriz=[]
nueva_fila=[]
suma=0

# Inicio del programa
filas=int(input("cantidad de filas:"))            # filas = 2
columnas= int (input("Cantidad de columnas:"))    # columnas=3

for i in range(filas): 
    matriz.append([0]*columnas)    # [[0, 0, 0], [0, 0, 0]]

# Ingresamos el num en cada posicion de la matriz
for f in range (filas):
    for c in range (columnas):
        matriz[f][c]= int(input("Ingrese el numero:"))

# Suma de las filas 
for k in range (filas):
    suma=sum(matriz[k])
    matriz[k].append(suma)

#  Suma de cada columna 
for r in range (columnas+1):
    suma=sum(filas[r] for filas in matriz)# 
    nueva_fila.append(suma)
matriz.append(nueva_fila)



# Imprimimos la matriz con sus respectivas sumas
for filas in matriz:
    for elemento in filas:
        print(elemento, end="  ") 
    print()
























































