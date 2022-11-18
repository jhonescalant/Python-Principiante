# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x15 y nombre ‘marco’. Carga la tabla con dos únicos valores 0 y 1, donde el valor uno ocupará las posiciones o elementos que delimitan la tabla, es decir, las más externas, mientras que el resto de los elementos contendrán el valor 0.
# 111111111111111
# 100000000000001
# 100000000000001
# 100000000000001
# 111111111111111
# Visualiza el contenido de la matriz en pantalla.

# Varaibles 

matriz=[]
filas=5
columnas=15
# Inicio del programa

for i in range (filas):
    matriz.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        if (f==0 or f==4 or c==0 or c==14 ):
            matriz[f][c]=1

for filas in matriz:
    for elementos in filas:
        print(elementos, end="")
    print()























