# Queremos guardar los nombres y las edades de los alumnos de un curso. Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos: 
# Todos los alumnos mayores de edad y los alumnos mayores (los que tienen más edad).


# Variables

lista_alumnos=[]
lista_mayores=[]
nombre_ingresado=0
edad_ingresado=0

# Inicio del programa
print("Introduzca (*) para finalizar")

while (nombre_ingresado!="*"):
    # Se solicita el ingreso de   
    nombre_ingresado=input("Ingrese el nombre: ")
    if (nombre_ingresado!="*"):
        edad_ingresado=int(input("edad:"))
        if(edad_ingresado>18 and edad_ingresado<40):
            lista_alumnos.append(nombre_ingresado)
        if (edad_ingresado>40):
            lista_mayores.append(nombre_ingresado)

# Salida de pantalla        
print(f"lista de mayores de 18:{lista_mayores}")
print(f"lista de mayores de 40:{lista_alumnos}")


# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

Introduzca (*) para finalizar
Ingrese el nombre: jhon
edad:45
Ingrese el nombre: tomas
edad:5
Ingrese el nombre: marcos
edad:19
Ingrese el nombre: pedro 
edad:20
Ingrese el nombre: juan
edad:48
Ingrese el nombre: *

**********************************************************
                    P R O C E S O
***********************************************************
nombre_ingresado=jhon|tomas|marcos|pedro|juan|
  edad_ingresado= 45 |  5  |  19  |  20 | 48 |
   lista_alumnos=['marcos', 'pedro ']
   lista_mayores=['jhon', 'juan']


**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
lista de mayores de 18:['jhon', 'juan']
lista de mayores de 40:['marcos', 'pedro ']

"""




























