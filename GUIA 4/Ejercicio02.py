#Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.

palabras=[]
palabras_ingresadas=""
palabras_invertidas=[]

#  Inicio del programa

while len (palabras)<5:
    palabras_ingresadas=input("Ingrese una palabra:")
    palabras.append(palabras_ingresadas)
print(palabras)

palabras_invertidas=list(reversed(palabras))

print(palabras_invertidas)

# ********************************************************************************************************************
#                               P R U E B A    D E    E S C R I T O R I O 
# ********************************************************************************************************************

"""
**********************************************************
             D A T O S   D E   E N T R A D A
**********************************************************

Ingrese una palabra:jhon
Ingrese una palabra:lucas
Ingrese una palabra:maria
Ingrese una palabra:soledad
Ingrese una palabra:martin 

**********************************************************
                    P R O C E S O
***********************************************************
           palabras=[]
palabras_invertidas=[]
palabras_ingresadas=""

**********************************************************
          S A L I D A   P O R   P A N T A L L A
**********************************************************
['jhon', 'lucas', 'maria', 'soledad', 'martin ']
['martin ', 'soledad', 'maria', 'lucas', 'jhon']

"""


