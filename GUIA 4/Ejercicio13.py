# De una empresa de transporte se quiere guardar el nombre de los conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
# - Nombre: Lista para guardar los nombres de los conductores.
# - kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realza cada conductor. Al finalizar se muestra la lista con 
# los nombres de conductores y los kilómetros que ha realizado.


# Variables 
lista_conductores=[]
lista_kilometros=[]
total_km=[]
suma=0
cant_conduc=0
cont=0
semana=7

#Inicio del programa
cant_conduc=int(input("Ingrese la cantidad de consuctores:"))

for i in range(cant_conduc):
    nombre_conduc=input("Ingrese el nombre del conductor:")
    lista_conductores.append([nombre_conduc])

for k in range (cant_conduc):
    lista_kilometros.append([0]*7)
print(lista_kilometros)

for c in range (cant_conduc):
    print(f" ****  Kilometros del {c+1} conductor  ***** ")
    for h in range (7):
        lista_kilometros[c][h]=int(input(f"km del dia {h+1}: "))

#                          Lista del total de los km de cada conductor

# Creamos la lista de los kilometros totales
for t in range (cant_conduc):
    total_km.append([0])

# Suma de los km 
for c in range (cant_conduc):
    suma=0
    for h in range (7):
        suma+=lista_kilometros[c][h] 
    total_km[c]=suma     


for x in range (1):
    for z in range(2):
        print(f"conductor:{cant_conduc[z][x]}    km totales={total_km[z][x]}")
































