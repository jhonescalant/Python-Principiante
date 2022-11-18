# Proceso de discriminantes:
# Un matemático desea un simple programa que le permita cargar una serie de números quere presentan los discriminantes de 
# diferentes ecuaciones de segundo grado, el proceso de la secuencia analiza cuando el matemático no desea seguir cargando discriminantes. 
# Usted debe:
# a) Determinar la cantidad de discriminantes quedarán 2 raíces
# b) Determinar la cantidad de discriminantes quedarán una única raíz
# c) Determinar la cantidad de discriminantes quedaran raíces en el campo de los números imaginarios
# d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados por el matemático
#



# ****************************************************************************
#                        D   I   S   E   Ñ   O  
# ****************************************************************************

# Variables 
continuar="S"
descriminante=0
valor_b=0
valor_a=0
valor_c=0
dos_Raiz=0
Unica_Raiz=0
imaginarios=0
total=0
porcentaje=0

# Inicio del programa

print(" **  FORMULA DEL DESCRIMINATE  **")
print("           b²- 4.a.c   ") 
while (continuar=="S"):

  # Se Le pide al usuario que ingrese los valores de a , b ,c 
  valor_b=int(input("\nIngrese el valor de b: "))
  valor_a=int(input("Ingrese el valor de a: "))
  valor_c=int(input("Ingrese el valor de c: "))

  # Una vez obtenidos los valores  de a,b,c calculamos el discriminante
  descriminante=((valor_b)**2 - 4 * valor_a*valor_c)
  print (descriminante)
  # Cuando el descriminante es mayor a cero tiene 2 soluciones R(reales)
  if (descriminante>0):
    dos_Raiz+=1
  # Cuando el descriminante es menor a cero  tiene una solucion con numeros imaginarios 
  if (descriminante<0):
    Unica_Raiz+=1
  # Cuando el discriminante es igua a cero  tiene una solucion R(reales) 
  if (descriminante==0):
    imaginarios+=1

  # 
  continuar=input("Desea continuar S/N:").upper()
  while (continuar!="S" and continuar!="N" ):
    continuar=input("ERROR ---- Desea continuar S/N:").upper()

# Calculamos el porcentaje de los numeros imaginarios 
total=(dos_Raiz+Unica_Raiz+imaginarios)*imaginarios
print(total)
porcentaje=total * 0.1
print(porcentaje)

# Salida por pantalla 
print("Cantidad de discriminantes quedarán 2 raíces:"+str(dos_Raiz))
print("Cantidad de discriminantes quedarán una única raíz:"+str(Unica_Raiz))
print("Cantidad de discriminantes quedaran raíces en el campo de los números imaginarios:"+str(imaginarios))
print("Porcentaje de los descriminante con numeros imaginarios:"+str(porcentaje)+"%")

# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************
Ingrese el valor de b: 4
Ingrese el valor de a: 5
Ingrese el valor de c: 6
Desea continuar S/N:s

Ingrese el valor de b: 8
Ingrese el valor de a: 5
Ingrese el valor de c: 2
Desea continuar S/N:s

Ingrese el valor de b: 7
Ingrese el valor de a: 5
Ingrese el valor de c: 9
Desea continuar S/N:n


**********************************************************
                    P R O C E S O
***********************************************************
    continuar=S|s|n|
      valor_b=4|8|7|0|
      valor_a=5|5|5|0|
      valor_c=6|2|9|0|
descriminante=-104|24|-131 
     dos_Raiz=0|1|0|0|
   Unica_Raiz=1|1|2|0|
  imaginarios=0|0|0|0|
        total=0|0|0|0|
   porcentaje=0|0|0|0|

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************

Cantidad de discriminantes quedarán 2 raíces:1
Cantidad de discriminantes quedarán una única raíz:2
Cantidad de discriminantes quedaran raíces en el campo de los números imaginarios:0
Porcentaje de los descriminante con numeros imaginarios:0.0%

"""
