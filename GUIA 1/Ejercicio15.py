#EJERCICIO 15
#Jornal de un Operario. 
#Se necesita desarrollar un programa para el área de recursos humanos de una empresa 
#que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno
#que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas.
#La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno.
#Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora.

#Variables
cant_horas=0
opcion=0
pago_total=0.0

#Inicio del programa 
print("  *** Turnos de trabajos ***") # Menu de turnos
print("""
        1.Turno diurno
        2.Turno nocturno
""")
#El usuario elije la opcion que necesita
opcion=int(input("Elija una de las opciones:"))

if (opcion == 1 ):
    print(" ***  Turno diurno  ***")
    #Ingreso de las horas trabajadas
    cant_horas=int(input("Ingrese las horas trabajadas:"))
    #Calculo del pago total
    pago_total= cant_horas * 35.50
    #Salida por pantalla 
    print("Su pago total por horas trabajas es de:"+str(pago_total))
else:
    print(" *** Turno nocturno ***")
    #Ingreso de las horas trabajadas
    cant_horas=int(input("Ingrese las horas trabajadas:"))
    #Calculo del pago total
    pago_total= cant_horas * 40.60
    #Salida por pantalla 
    print("Su pago total por horas trabajas es de:"+str(pago_total))


#**************************************************************************************        
#                  P R U E B A      D E     E S C R I T O R I O
#**************************************************************************************
#   opcion     cant_horas      pago_total  
#     1            5              177.5    
#     2            5              203.0
#     
#    