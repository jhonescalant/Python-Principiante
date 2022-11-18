# Sólo menores que 7. 
# Desarrollar un programa de Phyton que permita cargar por teclado un secuencia de números, uno por uno. 
# Siempre se supone que el usuario cargará un 0(cero) para indicar el final del proceso de carga. El cero no debe considerarse un dato a procesar. 
# El programa debe:
# a) Determinar el porcentaje que cantidad de números pares representa en la cantidad total de números ingresados.
# b) Determinar cuántos de los números ingresados tenían su último dígito igual a 4 o igual a 5.
# c) Determinar el menor de los números ingresados que sean divisibles por 3.
# d) Determinar si la secuencia estaba formada sólo por números.



# Varibles 

# Inicio del programa
def carga_numeros():
    num_ingresado=1
    lista_numeros=[]
    while(num_ingresado!=0): 
        num_ingresado=int(input("Ingrese un numero: "))      
        if (num_ingresado!=0):   
            lista_numeros.append(num_ingresado)  
    return lista_numeros

def cant_numeros_pares(lista_numeros):
    cant_num_ingresado=0
    pares=0
    porcentaje=0.0

    for numeros in lista_numeros:
        cant_num_ingresado+=1

        if(numeros % 2 ==0):
            pares+=1
    
    porcentaje=round(((pares*100)/cant_num_ingresado),2)
    
    return porcentaje

def ultimo_digito(lista_numeros):
    UltimoDigito=0
    
    for numero in lista_numeros:
        if(numero%10==4 or numero%10==5):
            UltimoDigito+=1   
    return UltimoDigito

def numero_menor(lista_numeros):
    menor=999
    divisible_por_tres=0
    for numero in lista_numeros:

        if menor > numero:
            menor=numero
        
        if (menor % 3):
            divisible_por_tres=menor
    
    return divisible_por_tres

def menores_de_siete(lista_numeros):
    menor_siete=0

    for numeros in lista_numeros:

        if (numeros >= 7):
            menor_siete=1

    if (menor_siete>=1):
        print("no son mayores a 7")
    else:
        print(" son menores a 7")

       
lista_numeros=carga_numeros()
print(lista_numeros)
print(f"el porcentaje: {cant_numeros_pares(lista_numeros)}%")

print(f"Ultimo digito: {ultimo_digito(lista_numeros)}")

print(f"menor y divisible: {numero_menor(lista_numeros)}")

menores_de_siete(lista_numeros)




 


























# v=[]
# c=[]
# guardovector=0
# guardo_numeros_pares=0
# guardo_impares=0
# #funcion en donde introduzco los numeros en la lista
# #def llenarvector(numeros) en esta parte defino la lista numeros
# def llenarvector(numeros):
#     #empiezo en 1 para que entre en el bucle
#     añadir_numero=1
#     #el bucle termina cuando añadir_numero sea 0
#     while(añadir_numero!=0):
#             minimo=0
#             #ingreso numero por teclado
#             añadir_numero=int(input("ingrese un numero: "))
#             #condicional para que no cuente el cero
#             if(añadir_numero>=1):
#                 #introduzco numeros a la lista
#                 numeros.append(añadir_numero)
#     #retorno el valor de numeros
#     return(numeros)
# #funcion para sumar los numeros pares de la lista
# #no importa que numeros sea distinto a numeros1 por que no es la misma variable
# #las funciones no hablan entre si
# def pares(numeros1):
#     numeros_pares=0
#     #for que recorre la lista numeros
#     for i in range(len(numeros1)):
#         #condicional para que el numero sea par
#         if(numeros1[i]%2==0):
#             #acumulo los numeros pares
#             numeros_pares=numeros_pares+1

#     #retorno la suma de los numeros pares de la lista
#     return numeros_pares

# def porcentaje(numeros2):
#     pares_porcentaje=0
#     pares_porcentaje=pares(v)
#     porcentaje=((pares_porcentaje*100)/len(numeros2))
#     return porcentaje

# def menor(numeros3):
#     minimo=100000
#     for i in numeros3:
#         if(i%3==0):
#             #print(i)
#             if(i<minimo):
#                 minimo=i
#     print(minimo)
#     return minimo
# #aca hago el pasaje de parametros
# #numeros toma el valor de v
# #numeros es igual a v
# guardovector=llenarvector(v)
# print("lista de numeros:"+str(guardovector))
# #como numero es igual a v
# #vuelve a tomar el valor de numeros y lo llamo en numeros pares
# guardo_numeros_pares=pares(guardovector)
# print("numeros pares:"+str(guardo_numeros_pares))
# guardo_porcentaje=porcentaje(v)
# print("porcentaje de numeros pares:"+str(guardo_porcentaje))
# guardo_impares=menor(v)
# print("menor de numeros impares:"+str(guardo_impares))


























