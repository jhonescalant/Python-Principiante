#Sílaba "de" en la primera mitad: 
# Desarrollar un programa en Python que permita cargar por teclado un texto completo. 
# Siempre se supone que el usuario cargará un punto para indicar el final del texto, y que cada palabra de ese texto está separada de las demás por un espacio en blanco. 
# El programa debe:
# a) Determinar cuántas palabras tenían al menos un caracter que era en realidad un dígito (un caracter entre '0' y '9').
# b) Determinar cuántas palabras tenían 3 o menos letras, cuántas tenían 4 y hasta 6 letras, y cuántas tenían más de 6 letras.
# c) Determinar la longitud de la palabra más larga del t
# d) Determinar cuántas palabras contuvieron la expresión "de", pero en la primera mitad de la palabra


notas_examen=[7,4,10,9,3,1,5,6,10]

notas_trabajo=[8,6,10,9,7,10,7,3,10]


def aprobados(nota_minima, lista_notas):
    cant_aprobados=0
    for nota in lista_notas:
        if(nota>= nota_minima):
            cant_aprobados+=1
    return cant_aprobados

def promedio(lista_notas):
    total=0
    for i in range (len(lista_notas)):
        total+=lista_notas[i]
    return total / len(lista_notas)

print("La cantidad de aprobados en el examen es de "+ str(aprobados(4,notas_examen)))

print("El promedio de las notas del examen"+str(promedio(notas_examen)))


 

