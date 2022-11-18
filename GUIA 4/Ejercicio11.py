# Diseñar el algoritmo correspondiente a un programa, que:
# a) Crea una tabla bidimensional de longitud 5x5 y nombre ‘diagonal’.
# b) Carga la tabla de forma que los componentes pertenecientes a la diagonal de la matriz tomen el valor 1 y el resto el valor 0.
# c) Muestra el contenido de la tabla en pantalla.


# Variables 
filas=5
columnas=5
matriz=[]

# Inicio del programa

for i in range (filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        if (f==c or f+c == 4 ):
            matriz[f][c]=1

for filas in matriz:
    for elementos in filas:
        print(elementos, end=" ")
    print()






























