#Abrir una ventana en  pygame
import pygame , sys

# Inicialisamos pygame
pygame.init()
# Definir colores 
BLACK = (0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
# Tamaño de la ventana
size=(800,500)

#Crear ventana 
ventana=pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        # Imprime los momivientos que hace el usuario
        print(event)
        # Esta funcion me permite cerrar la ventana apretando la (X)
        if event.type == pygame.QUIT:
            sys.exit()

# Color de fondo 
ventana.fill(WHITE)
# Zona de dibujo 
for x in range (100,700,100):
    pygame.draw.rect(ventana,BLACK , (X,230,50,50))
    pygame.draw.line(ventana, GREEN , (x,0),(x,100),5)
pygame.display.flip()

