# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
# A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

# Varaibles 
lista_notas=[]
notas=0

# Inicio del programa 
print("la nota corresponde de 0 a 10")
for i in  range(5):
   # Pedimos al usuario que ingrese las notas 
   notas=int(input("Ingrese las notas:"))
   # Validamos que los valores esten entre 0 y 10 
   while (notas<0 or notas>10):
      notas=int(input("ERROR --- Ingrese las notas:"))
   # Utilzamos el metodo append() para agregar cada valor que el usuario ingrese
   lista_notas.append(notas)
# Utilizamos el metodo sort()  para ordenar los elementos de las lista
lista_notas.sort()
# Salida por pantalla 
print(f"lista de notas:{lista_notas}")
print(f"Nota mas alta:{lista_notas[4]}")
print(f"Nota media:{lista_notas[2]}")
print(f"Nota mas baja:{lista_notas[0]}")


# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

la nota corresponde de 0 a 10
Ingrese las notas:5
Ingrese las notas:8
Ingrese las notas:2 
Ingrese las notas:7
Ingrese las notas:98
ERROR --- Ingrese las notas:5

**********************************************************
                    P R O C E S O
***********************************************************
lista_notas=[2, 5, 5, 7, 8]
      notas=2| 5| 5| 7| 8

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
ista de notas:[2, 5, 5, 7, 8]
Nota mas alta:8
Nota media:5
Nota mas baja:2

"""
