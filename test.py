import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt
import time
from tkinter import *
from glob import glob
import coor


def canvas_animation(window):
     # creating start line
    C = Canvas(window, bg="black", width=1000, height=1000)
    #line = C.create_line(0, 100, 800,100 , fill= "#76EE00", width=2)
    C.pack(fill="both", expand=True)
    return C

def ecg_signal_animation(window, C, xinc, yinc):
    signal = C.create_line(0, 100, 10, 100, fill= "#76EE00", width=2)
    # loop
    index = 0
    ecg_cor = coor.coords
    while True:
        xinc, yinc = ecg_cor[index]
        C.move(signal, xinc,yinc)
        window.update()
        time.sleep(0.05)
        signal_pos = C.coords(signal)
        xl,yl,xr,yr = signal_pos
        if xl < abs(xinc) or xr >= 1000-abs(xinc):
            xl,yl,xr,yr = 0,0,0,0
            C.delete(signal)
            signal = C.create_line(0, 100, 10, 100, fill= "black", width=2)
        index+=1

def main():
    window = Tk() 
    xinc = 5
    yinc = 0
    window.geometry( "1000x1000" ) 
    create_canvas_animation = canvas_animation(window)
    ecg_signal_animation(window, create_canvas_animation, xinc,yinc)
main()