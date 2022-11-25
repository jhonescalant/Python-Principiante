# Desarrollar un procedimiento que imprima una fecha en formato DD/MM/AA. 
# El dato que recibe es un longint con una fecha en formato aaaammdd.

#Inicio del programa
def cambiarFormatoFecha(año, mes, dia):
    dias_del_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    if (mes < 1 or mes > 12): 
        print("Mes fuera de rango")
    if (dia < 1 or dia > dias_del_mes[mes]): 
        print("Dia fuera de rango")

    return f"{dia}/{mes}/{str(año)[2:4]}"


print(cambiarFormatoFecha())





