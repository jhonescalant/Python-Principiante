# Desarrollar una rutina tal que dada una fecha (AAAAMMDD) y un número natural que representa una cantidad de días, 
# calcule y retorne la nueva fecha en tres parámetros  año (AAAA), mes (MM) y día (DD) que resulte de incrementar al
#  parámetro fecha con el parámetro cantidad de días.

# Inicio del programa
def tiempo_transcurrido(año, mes, dia, nro): 

    dias_del_mes = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    #Validaciones del mes 
    if (mes < 1 or mes > 12): 
        print("ERROR --- Mes no valido")
    if (dia < 1 or dia > 31): 
        print("ERROR --- Dia no valido")
    if (nro < 0): 
        print("ERROR --- Dias a transcurrir no valido")

    #Se repite hasta que ya no queden dias por sumar
    while (nro != 0):

        if (dia + nro > dias_del_mes[mes-1]): 
            nro -= dias_del_mes[mes-1] - dia
            dia = 0
            mes += 1
            #Incremento del año y nuevo valor de la variable mes
            if (mes == 13):
                mes = 1
                año += 1
        else:
            dia += nro
            nro -= dia

    return [año, mes, dia]

#salida por pantalla
print(tiempo_transcurrido(2022, 4, 25, 20))



