#EJERCICIO 4
#4) Ultimos digitos ¿Como usaria el operador resto (%) para obtener el valor del ultimo digito de un numero entero ?¿y como 
#   obtendria los dos digitos?
# Desarrolle un programa que cargue  un numero entero por teclado, y muestre el ultimo digito del mismo (por un lado) 
# y los dos ultimos digitos (por otro lado).

#Variable 
numero=0
ultimoDigito=0
dosUltimosDigitos=0

#Inicio del programa
numero=int(input("Ingrese un numero entero:"))

#dividimos el numero en 10 y sacamos el resto
ultimoDigito  =  numero  %  10

#dividimos el numero en 100 y sacamos el resto
dosUltimosDigitos  =  numero  %  100

#Salida por pantalla
print ( "El ultimo digito es:" , ultimoDigito )
print ( "Los dos ultimos digitos son:" , dosUltimosDigitos )


#**********************************************************       
#   P R U E B A      D E     E S C R I T O R I O
#***********************************************************
#    numero    ultimoDigito    dosUltimoDigitos
#     10            0                 10
#     25            5                 25

