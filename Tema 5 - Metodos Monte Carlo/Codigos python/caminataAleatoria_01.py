# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#   Random Walk, in glorious Technicolour
#   https://docs.python.org/3/library/turtle.html
#   Authour: Alan Richmond, Python3.codes
 
import turtle
from random import randint
from colorsys import hsv_to_rgb
 
paso = 30                 # length of each step
npasos = 2000             # number of steps
hinc = 1.0/npasos         # hue increment
turtle.width(2)                # width of line
 
(w,h) = turtle.screensize()      # boundaries of walk
turtle.speed('fastest')
turtle.colormode(1.0)          # colours 0:1 instead of 0:255
turtle.bgcolor('black')        # black background
hue=0.0

for i in range(npasos):
    turtle.setheading(randint(0,359))
    #   https://docs.python.org/2/library/colorsys.html
    turtle.color(hsv_to_rgb(hue, 1.0, 1.0))  # pen colour in RGB
    hue += hinc                           # change colour
    turtle.forward(paso)                       # step along!
    (x,y) = turtle.pos()                         # where are we?
    if abs(x) > w or abs(y) > h:            # if at boundary
        turtle.backward(paso)                      # step back
turtle.done()