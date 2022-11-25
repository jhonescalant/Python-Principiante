# La letra T y los porcentajes. Desarrollar un programa en Python que permita cargar por teclado un texto completo. Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. El programa debe:
# a) Determinar la cantidad de palabras en las que solo aparece una única vez la letra “t”
# b) Determinar la cantidad de palabras cuya cantidad de letras es mayor a la cantidad de letras de la palabra anterior
# c) Determinar la cantidad de palabras con la cantidad de letras pares y comienzan con la letra “c”
# d) Determinar el porcentaje que representa el primer punto sobre el total de las palabras del texto procesado.

#Inicio del programa
def simplificaciones(P, Q):
    numeros_primos = (2, 3, 5, 7, 11)

    for n in numeros_primos:  
        if (P % n == 0 and Q % n == 0):
            P /= n
            Q /= n

    return [int(P), int(Q)]

#Casos de prueba
primera_fraccion = simplificaciones(105, 210)
segunda_fraccion = simplificaciones(15, 45)
tercera_fraccion = simplificaciones(22, 44)
cuarta_fraccion  = simplificaciones(9, 24)

# Salida por pantalla 
print(f"{primera_fraccion[0]}/{primera_fraccion[1]}")
print(f"{segunda_fraccion [0]}/{segunda_fraccion [1]}")
print(f"{tercera_fraccion[0]}/{tercera_fraccion[1]}")
print(f"{cuarta_fraccion[0]}/{cuarta_fraccion[1]}")




