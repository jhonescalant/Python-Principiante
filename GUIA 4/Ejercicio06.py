# Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) 
# y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.



# Varaibles 
num_mes=0
lista_mes=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
lista_cant_dias=["30","28","31","30","31","30","31","31","30","31","30","31"]

# Inicio del programa

# Se le pide al usuario el numero del mes 
num_mes=int(input("Ingrese el mes:"))
# Se valida el numero que ingreso el usuario 
while (num_mes<0 or num_mes>12):
    # Mensaje error
    num_mes=int(input("ERROR --- Ingrese el mes:"))
#Salida por pantalla
print(f"Mes solicitado: {lista_mes[num_mes-1]}")
print(f"Cantidad de dias del mes: {lista_cant_dias[num_mes-1]}")

# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

Ingrese el mes:01

**********************************************************
                    P R O C E S O
***********************************************************

-----------------------------------------------------------

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************

Mes solicitado: enero
Cantidad de dias del mes: 30

"""






































