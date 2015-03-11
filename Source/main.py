# -*- coding: utf-8 -*-

# An obstacle avoiding ball simulation using ML

"""
Machine Learing
Artificial Intelligence
"""

from Tkinter import Tk, Canvas
import numpy as np
import random as rnd
import time

class SimWin(Tk,object):
    
    WIN_HEIGHT = 600
    WIN_WIDTH = 600    
    WIN_BG = '#fff'
    
    def __init__(self, parent=None):
        
        super(SimWin, self).__init__(parent)
        self.canvas = Canvas(master=self, 
                             height=SimWin.WIN_HEIGHT, 
                             width=SimWin.WIN_WIDTH, 
                             background=SimWin.WIN_BG)
        self.canvas.pack()
    
    def changeProps(self, height, width, bg):
        
        SimWin.WIN_HEIGHT = height
        SimWin.WIN_WIDTH = width
        SimWin.WIN_BG = bg
        
    def envDraw(self, redius, C):
        # C is a 2D numpy array
        
        if(not (type(C)==type(np.array([1])))):
            print 'Input a valid NUMPY array'
        else:
            
            n = 0
            for (i,j) in C:
                self.canvas.create_oval(i-redius[n],j-redius[n],i+redius[n],j+redius[n],
                                        fill='#f00',
                                        outline='#f00')
                n = n + 1
    
    def cleanCanvas(self):
        
        self.canvas.delete('delete')

def main():
    
    win = SimWin()
    
    nofobs = 10    
        # random bubbles
    cnts = np.random.randint(low=50, high=600-50, size=(nofobs,2))
    reds = []    
    for i in range(nofobs):
        reds.append(rnd.randint(5,40))
    
    win.envDraw(reds, cnts)
    win.update()
        
    win.mainloop()
    
    return

if(__name__=='__main__'):
    main()