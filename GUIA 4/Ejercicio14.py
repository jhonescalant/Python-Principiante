# Crear un programa que lea los precios de 5 artículos y las cantidades vendidas por una empresa en sus 4 sucursales. Informar:
# - Las cantidades totales de cada artículo.
# - La cantidad de artículos en la sucursal 2.
# - La cantidad del artículo 3 en la sucursal 1.
# - La recaudación total de cada sucursal.
# - La recaudación total de la empresa.
# - La sucursal de mayor recaudación.

# Varaibles1
recaudacion_sucursal=[]
cant_total_articulos=[]
empresa=[]
nueva_fila=[]
suma=0
cont=0


CANT_SUCURSAL=2
CANT_ARTICULOS=3

# Inicio del programa 

print ( "  ***  Innforme de las empresa ***  ")

# Creamos una matriz

for i in range(CANT_ARTICULOS):
    empresa.append([0]*CANT_SUCURSAL) 

# Pedimos al usuario que ingrese las cantidad de articulos vendidos por sucursal

for f in range (CANT_ARTICULOS):
    print(f"  **  sucursal {f+1}  **  ")
    for g in range(CANT_SUCURSAL):
        # Agregamos la cantidad de articulos vendidos por sucursal
        empresa[f][g]=int(input(f"cant articulo {g+1} vendidos:"))

# Las cantidades totales de cada articulo , en este caso vamos la sumar las filas

for q in range(CANT_ARTICULOS):    
    suma=sum(empresa[q])
    empresa[q].append(suma)

# Las cantidad totales de cada sucursal , en este caaaso vamos a sumar las columnas

for r in range (CANT_SUCURSAL+1):
    suma=sum(CANT_ARTICULOS[r] for CANT_ARTICULOS in empresa) 
    cant_total_articulos.append(suma)
empresa.append(cant_total_articulos)


# Imprimir con la forma de una matriz
for CANT_SUCURSAL in empresa:
    for elementos in CANT_SUCURSAL:
        print(elementos, end=" ")
    print()

# Salida por pantalla 
# a) cantidad totales por articulos
for z in range(CANT_ARTICULOS):
    cont+=1
    for f in range(CANT_ARTICULOS):
        if (f==2):
            print (f"Sucursal {cont}  tiene {empresa[z][f]} articulos")

# b)  cantidad de articulos de las sucursal 2
print ("La cantidad de artículos en la sucursal 2")
print (f"Sucursal: {2}  tiene {cant_total_articulos[1]} articulos")

# C) cantidad de articulos de las sucursal 1
print ("La cantidad de artículos en la sucursal 1")
print (f"Sucursal: {1}  tiene {cant_total_articulos[0]} articulos")


# d) racaudacion total de cada sucursal
for x in range(len(cant_total_articulos)):
    cont=0
    cont+=1
    print (f"Sucursal {cont}  recaudo {cant_total_articulos[x]} articulos")


















