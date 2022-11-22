import pygame as p
#import game3




#Dimisiones del tableros 
ANCHO,ALTO=512,512
DIMENSION=8 # Dimension del tablero
DIM_CASILLAS=512//DIMENSION # Dimension de las casillas
max_fps_=15 # Para las animaciones
imagines={}

"""
Para inicialisar las imagines de las piezas 
"""

def cargaImagines ():
    piesas=["ab","cb","pb","Qb","rb","tb","an","cn","pn","Qn","rn","tn"]
    for pieza in piesas:
        imagines[pieza]=p.transform.scale(p.image.load("IMAGINES/"+pieza+".png"),(DIM_CASILLAS,DIM_CASILLAS))



