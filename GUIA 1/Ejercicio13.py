#EJERCICIO 13
#Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de mail para el 
# nombre y apellido ingresado de acuerdo a las siguientes reglas: 
# Componer la dirección de correo de la siguiente manera: @ Por ejemplo 
# para Nombre = Felipe, 
# Apellido= Steffolani y 
# Dominio= umet.edu.ar 
# la dirección de mail sería: fsteffolani@umet.edu.ar. 
# Pero si la primera primera letra del nombre y la primera letra del apellido son la misma entonces uƟlizar: .@ 
# Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar la dirección de mail sería:
#soledad.steffolani@umet.edu.ar

#VARAIBLES 
nombre=""
apellido=""
dominio=""
mail=""
extraccion_nombre=""
extraccion_apellido=""
#inicio del programa 
nombre=str(input("Ingrese su nombre:"))
apellido=str(input("Ingrese su apellido:"))
dominio=str(input("Ingrese el dominio:"))
#Se extrae el primer caracter del nombre ingresado por el usuario 
extraccion_nombre=nombre[0:1]
extraccion_apellido=apellido[0:1]
if(extraccion_nombre == extraccion_apellido):
    print("Dirreccion de mail:"+str(nombre)+"."+str(apellido)+"@"+str(dominio))
else:
    print(extraccion_nombre + apellido +"@"+dominio)


#**************************************************************************************        
#                  P R U E B A      D E     E S C R I T O R I O
#**************************************************************************************
#  nombre      apellido       dominio         extraccion_nombre      extraccion_apellido   
#   jorge       lopez       @umet.edu.ar               j                       l               
#   maria       martinez    @umet.edu.ar               m                       m  
#       
#     


