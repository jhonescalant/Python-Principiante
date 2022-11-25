# Desarrollar una rutina tal que dados una base y un exponente, enteros positivos, calcule  y retorne la potencia.

# Inicio del programa
def potencia(base, exponente):
    resultado=0
    if (base < 0 or exponente < 0):
        print( "Numero fuera de rango")
    
    resultado= base ** exponente
    return resultado

print(potencia(50, -5))
print(potencia(10,2))





