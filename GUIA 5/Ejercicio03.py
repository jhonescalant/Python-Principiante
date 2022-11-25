# Solamente 'a' Desarrollar un programa que permita ingresar por teclado, con palabras separadas por un espacio y terminado en punto. 
# En base al texto ingresado, determinar: 
# a) Cuál es la longitud de la palabra más larga. 
# b) Cuántas palabras tienen la a como única vocal 
# c) Qué porcentaje representan las que sólo tienen la vocal a sobre el total de palabras. 
# *********************************************
# Ejemplo: "el agua clara salta por las piedras." 
# La longitud de la palabra más larga es 7 letras. 
# Las palabras cuya única vocal es la a son: 3 
# El porcentaje de estas palabras sobre el total es 43 %


# Inicio del programa
def solamente_a(texto):

    vocales = ("e", "i", "o", "u")
    palabras_ingresadas = 0
    palabra_mas_larga = 0
    palabras_con_a = 0     
    porcentaje_con_a = 0 
    cont = 0


    # El split() método divide una cadena en una lista.
    for palabra in texto.split():
        palabras_ingresadas += 1

        # determino la palabra mas larga
        if (palabras_ingresadas == 1 or len(palabra) > palabra_mas_larga):
            palabra_mas_larga = len(palabra)
        
        # Palabras que tienen la A como unica vocal 
        for letra in palabra:
            if (letra in vocales): 
                cont += 1
        if (cont == 0): 
            palabras_con_a += 1      
        cont = 0 

    #Calculo del porcentaje        
    porcentaje_con_a = int(palabras_con_a * 100 / palabras_ingresadas) 

    # Salida por panmtalla 
    print(f"La longitud de la palabra mas larga es de {palabra_mas_larga} letras")
    print(f"Palabras cuya unica vocal es la A: {palabras_con_a}")
    print(f"El porcentaje de estas palabras sobre el total es {porcentaje_con_a} %")

solamente_a("el agua clara salta por las piedras")

