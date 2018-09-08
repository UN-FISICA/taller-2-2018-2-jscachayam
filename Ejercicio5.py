# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:37:30 2018

@author: Sebastian Cachaya
Punto 5
"""


from turtle import *

a=input("ingrese filas de la piramide ")
a=int(a)

def poligono(n):
    for i in range(n):
        forward(30)
        left(360/n)
        
def fila(lados,filas):
    for i in range(filas):
        poligono(lados)
        up()
        forward(60)
        down()    


def piramide(filas):
    for i in range(filas,0,-1):
        fila(i+2,i) 
        up()
        backward((i*60))
        forward(60/2)
        left(90)
        forward(30+30)
        right(90)
        down()
    done()
 
up()
goto(-130,-130)
down()       
piramide(a)
