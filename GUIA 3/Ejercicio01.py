#Comisión de vendedores. 
# Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores, para ello 
# les solicita un sistemita que le permita calcular dichos montos. Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores(1 a 4).
# Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta(el proceso termina cuando se ingrese una categoría igual a cero) 
# y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base a los siguientes cálculos:
# Categoría1:cobra una comisión de 10%
# Categoría2:cobra una comisión de 25%
# Categoría3:cobra una comisión de 30%
# Categoría4:cobra una comisión de 40%
#Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedor es que en el la empresa junto con el total general.



# Variables
categorias=1
ventas=0.0
cobro_comision1=0.0
cobro_comision2=0.0
cobro_comision3=0.0
cobro_comision4=0.0
total_uno=0.0
total_dos=0.0
total_tres=0.0
total_cuatro=0.0
sumatoria=0.0

# Inicio del programa 
print("       **   INGRESE 0 (CERO) PARA SALIR   ** ")
while (categorias>0):
    # MENU  DE ELECCION DE CATEGORIA 

    print("""
        1.Categoria 1
        2.Categoria 2
        3.Categoria 3
        4.Categoria 4    
    """)
    # EL USUARIO INGRESA LA CATEGORIA  QUE LE CORRESPONE 
    categorias=int(input("Ingrese la categoria que corresponda:"))
    # VALIDAMOS QUE EL DATO INGRESADO ES ENTRE 1 Y 4
    while (categorias <=1 and categorias>=4):
        # MENSAJE ERROR
        categorias=int(input("ERROR --- Ingrese los numeros 1/2/3/4:"))
    
    if (categorias>0):

        if(categorias==1):
            venta=float(input(" Ingrese el total de las ventas: $"))
            while(venta<0):
                venta=float(input("ERROR --- Ingrese el total de la venta: $"))
            cobro_comision1=venta * 0.1
            total_uno+=cobro_comision1
            

        
        if(categorias==2):
            venta=float(input(" Ingrese el total de las ventas: $"))
            while(venta<0):
                venta=float(input("ERROR --- Ingrese el total de la venta: $"))
            cobro_comision2=venta * 0.25
            total_dos+=cobro_comision2

        if(categorias==3):
            venta=float(input(" Ingrese el total de las ventas: $"))
            while(venta<0):
                venta=float(input("ERROR --- Ingrese el total de la venta: $"))
            cobro_comision3=venta * 0.3
            total_tres+=cobro_comision3

        if(categorias==4):
            venta=float(input(" Ingrese el total de las ventas: $"))
            while(venta<0):
                venta=float(input("ERROR --- Ingrese el total de la venta: $"))
            cobro_comision4=venta * 0.4
            total_cuatro+=cobro_comision4

        
        sumatoria=total_uno+ total_dos + total_tres + total_cuatro





print("Cobro de la primera comision: $"+str(cobro_comision1))
print("Cobro de la segunda comision: $"+str(cobro_comision2))
print("Cobro de la tercera comision: $"+str(cobro_comision3))
print("Cobro de la cuarta comision: $"+str(cobro_comision4))
print("Cobro de la total de las comisiones: $"+str(sumatoria))
