# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:37:30 2018

@author: Sebastian Cachaya
Punto 4
"""
from math import *
from turtle import *

a=input("numero de lados del poligono ")
a=int(a)
b=input("numero de filas de la piramide ")
b=int(b)

def poligono(n):
    for i in range(n):
        forward(2*25*sin(pi/n))
        left(360/n)
        
def fila(lados,filas):
    for i in range(filas):
        poligono(lados)
        up()
        forward(50)
        down()   
    
def piramide(lados,filas):
    for i in range(filas,0,-1):
        fila(lados,i) 
        up()
        backward((i*50))
        forward(50/2)
        left(90)
        forward(30+20)
        right(90)
        down()
    done()

up()
goto(-130,-130)
down()
        
piramide(a,b)
