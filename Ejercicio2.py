# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 19:05:21 2018

@author: Sebastian Cachaya

Punto 2
"""
a=input("numero de lados del poligono ")
a=int(a)

from math import *
from turtle import *

up()
goto(-75,-75)
down()

def poligono(lado,n):
    for i in range(n):
        forward(lado)
        left(360/n)

def guia(n):
    lado=2*25*sin(pi/a)
    for i in range(4):
        poligono(lado,n)
        left(360*i/4)
        up()
        forward(150)
        down()
        right(360*i/4)
    done()
 
guia(a)
