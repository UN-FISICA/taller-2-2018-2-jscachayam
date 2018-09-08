# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 18:36:52 2018

@author: Sebastian Cachaya

Punto 1
"""


from turtle import *
up()
goto(200,-200)
down()

def poligono(lado,n):
    for i in range(n):
        forward(lado)
        right(360/n)


def guia(lado,n):
    for i in range(n):
        poligono(lado,n)
        left(360/n)
        up()
        forward(5*lado)
        down()
        
    done()
    
guia(50,4)
