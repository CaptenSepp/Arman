# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:11:05 2020

@author: torsten
"""
from math import sin
from Uebung_mapping import mapping
from Uebung_sinus import sinusliste


class AsciiBuffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.clear()
    
    def clear(self):
        buffer = list()
        for w in range(self.height):
            x = [' ']*self.width
            buffer.append(x)
            
        self.buffer = buffer
    
    def draw(self, x, y, char='*'):
        x = int(x)
        y = int(y)
        
        if x<0 or x>=self.width:
            return

        if y<0 or y>=self.height:
            return
        
        self.buffer[y][x] = char
        
    def hline(self, y):
        for x in range(self.width):
            self.draw(x, y, char='-')

    def vline(self, x):
        for y in range(self.height):
            self.draw(x, y, char='|')
        
    def __str__(self):
        result = ''
        for l in self.buffer:
            result += ''.join(l)
            result += '\n'
        return result
      
xminmax = [0, 30]
yminmax = [-1.5, 1.5]


buffer = AsciiBuffer(width=81, height=21)

#Demo für die draw-Funktion
#4 Linien zeichnen. 2 vertikal (vline) und 2 horizontal (hline)
if 0:
    buffer.hline(10)
    buffer.hline(12)
    buffer.vline(30)
    buffer.vline(32)
    
    #Zwei Punkte zeichnen
    buffer.draw(31, 11)  #In den Mittelpunkt der Linienkreuzung
    buffer.draw(buffer.width-1, buffer.height-1) #Unten Rechts
    
    print(buffer)



#Ab hier Code der Studierenden

if 1:
    buffer.clear()
    buffer.hline(0)
    buffer.hline( (buffer.height-1)//2 )
    buffer.hline( buffer.height-1 )
    
    buffer.vline(0)
    buffer.vline( buffer.width-1 )
    
    data = sinusliste(xmin=xminmax[0], xmax=xminmax[1], step=0.1)

    for x,y in data:
        posx = mapping(x, xminmax, [0, buffer.width-1])
        posy = mapping(y, yminmax, [buffer.height-1, 0])
        buffer.draw(posx, posy)
        
    print(buffer)
