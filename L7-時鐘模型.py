# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 17:46:28 2018

@author: Eric
"""

import turtle
tur = turtle.Turtle()

def writeNumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()

tur.seth(90)

writeNumber(12)
tur.right(90)

writeNumber(3)
tur.right(90)

writeNumber(6)
tur.right(90)

writeNumber(9)
tur.right(90)


turtle.done()
turtle.exitonclick()
