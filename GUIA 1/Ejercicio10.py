#EJERCICIO 10
#   Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.

#VARIABLE
pesos=0.0
dolar=0.0
pesos_actual=0.0
cambio_dolar=0.0
cambio_pesos=0.0
opcion=0

#INICIO DEL PROGRAMA
print("conversor de dolares a pesos y pesos a dolares ")
pesos_actual=float(input("Ingrese el valor del peso actual:")) #Ingreso del valor actual del peso
print("""
        1.Dolares a pesos 
        2.Pesos a dolares 

""")
opcion=int(input("Ingrese una de las opciones:"))

if opcion==1:
    #Ingreso de los  dolares a cambiar
    dolar=float(input("Ingrese lo dolares que quiere cambiar:"))
    cambio_dolar= dolar * pesos_actual
    print("Tiene:$",cambio_dolar,"pesos")
else:
    #Ingreso de los pesos que desea cambiar 
    pesos=float(input("Ingrese los pesos que quiere cambiar:"))
    cambio_pesos= pesos / pesos_actual
    print("Tiene:$",cambio_pesos,"dolares")

#*********************************************************************************************************        
#                               P R U E B A      D E     E S C R I T O R I O
#*********************************************************************************************************  
# pesos_actual        opcion       dolar       cambio_dolar       pesos     cambio_pesos 
#     295                1           30            8850.0
#     295                2                                        3000         10.17                                  
# 
# 
#  
#     

