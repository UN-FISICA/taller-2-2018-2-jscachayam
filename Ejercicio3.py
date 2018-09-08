# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 19:41:12 2018

@author: Sebastian Cachaya
Punto 3
"""
a=input("numero de lados del poligono ")
a=int(a)
b=input("numero de lados del poligono de aliniacion ")
b=int(b)

from math import *
from turtle import *


def poligono(lado,n):
    for i in range(n):
        forward(lado)
        left(360/n)

def guia(lado1,lado2):
    length=2*25*sin(pi/a)
    lado0=2*130*sin(pi/b) 
    for i in range(lado2):
        poligono(length,lado1)
        left(360*i/lado2)
        up()
        forward(lado0)
        down()
        right(360*i/lado2)                
    done()
  
up()
goto(-65,-65)
down()
guia(a,b)
