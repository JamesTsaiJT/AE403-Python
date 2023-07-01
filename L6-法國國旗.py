# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 20:42:57 2018

@author: Eric
"""

import turtle


def rectangle():
    tur.begin_fill()
    tur.forward(250)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(250)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.end_fill()
    
def myGoto(x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()
    
tur = turtle.Turtle()

#設置畫面大小
turtle.setup(850,850)

#左邊藍色部分
myGoto(-400,400)
tur.fillcolor(0,0,1)
rectangle()

#中間白色部分
myGoto(-150,400)
tur.fillcolor(1,1,1)
rectangle()


#右邊紅色部分
myGoto(100,400)
tur.fillcolor(1,0,0)
rectangle()

#完成程式
turtle.done()
turtle.exitonclick()