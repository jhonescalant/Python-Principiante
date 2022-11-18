#3.	Sueldos y aguinaldo. 
# Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego: 
# a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período. 
# b) Determinar en qué mes recibió el sueldo más bajo del período. 
# c) Informar el sueldo promedio del semestre.

#Variables 
sueldo_Vendedor=0.0
aguinaldo=0.0
sueldo_maximo=0.0
sueldo_minimo=0.0
mes_minimo=0
sueldo_total=0.0
promedio=0.0

#Inicio del programa 

for i in range (1,7):
    
    print("  **  Mes 0"+ str(i) +"   **") #Se imprime el mes que le corresponde a cada sueldo
    sueldo_Vendedor=float(input("Ingrese su sueldo:"))#Se ingresa el sueldo de cada mes
    #Sumamos todos lo sueldos ingresados por el usuario
    sueldo_total+=sueldo_Vendedor
    #Almacenamos los primeros datos ingresados para poder compararlos 
    if (i == 1):
        sueldo_maximo=sueldo_Vendedor
        sueldo_minimo=sueldo_Vendedor
    # comparamos el sueldo almacenado y el sueldo ingresado para sacar el sueldo mayor
    if (sueldo_maximo<sueldo_Vendedor):
        #El nuevo sueldo mayor reemplazamos y guardamos en la variable sueldo_maximo  
        sueldo_maximo = sueldo_Vendedor
        #Calculo del aguinaldo con el sueldo_maximo obtenido
        aguinaldo=sueldo_maximo/2
    
    #Comparamos los sueldos para poder averiguar el suelgo minimo
    if (sueldo_minimo > sueldo_Vendedor):
        #El nuevo sueldo minimo reemplazamos y guardamos en la variable sueldo_minimo  
        sueldo_minimo = sueldo_Vendedor
        #Almacenamos el de valor de i para poder obtener el mes con el sueldo_minimo
        mes_minimo = i   
#Calculo del promedio que la suma de todos los sueldos ingresados dividido por la cantidad
promedio=sueldo_total / 6

# SALIDA  POR  PANTALLA 
print("\n")
print("El aguinaldo que te corresponde es de: $"+str(aguinaldo))
print("El sueldo mas bajo lo recibio el mes: 0"+str(mes_minimo)+" con sueldo de: $"+str(sueldo_minimo))
print("El sueldo pormedio es de: $"+str(round(promedio,1)))

#********************************************************************************************************************************
#                              P R U E B A    D  E     E S C R I T O R I O 
#********************************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

  **   Mes 01  ** 
Ingrese su sueldo=20
  **   Mes 02  ** 
Ingrese su sueldo=30
  **   Mes 03  ** 
Ingrese su sueldo=40
  **   Mes 04  ** 
Ingrese su sueldo=10
  **   Mes 05  ** 
Ingrese su sueldo=5
  **   Mes 06  ** 
Ingrese su sueldo=80

**********************************************************
                    P R O C E S O
***********************************************************

sueldo_vendedor= 0.0 | 20 | 30 | 40 | 10  | 5 | 80 
  sueldo_maximo= 0.0 | 20 | 30 | 40 | 80 
  sueldo_minimo= 0.0 | 20 | 10 | 5  
      aguinaldo= 0.0 | 10 | 15 | 20 | 40 
     mes_minimo=   0 |  1 | 1  |  1 |  4  | 5 
   sueldo_total= 0.0 | 20 | 50 | 90 | 100 | 105 | 185   
       promedio= 0.0 | 30.8

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************

El aguinaldo que te corresponde es de: $40.0
El sueldo mas bajo lo recibio el mes: 05 con un sueldo de $5.0
El sueldo pormedio es de: $30.8


"""






















