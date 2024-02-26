import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt
import time
from tkinter import *
from glob import glob
 
root = Tk() 
  
root.geometry( "300x300" ) 
  
def newWindow(): 
    window = Toplevel(root)
    window.geometry( "800x200" )
    window.title( clicked.get() )

    ecg_list = [["Atrial Flutter", 0],["VF", 1],["Atrial Tachycardia",2],["SVT",3],["A Fib",4],["Normal Sinus Rhythms", 5],["VT", 6],["Multifocal Atrial Tachycardia",7],
                ["TdP",8], ["Bradycardia",9], ["Tachycardia", 10]]
    
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]

    print(clicked.get())
    window.configure( background='black' )

    Label(window, text="ECG", font=("Arial", 18)).pack()

    ecg_files = glob('./ECG/*.jpeg')                             # loads files to a dataset
    print(len(ecg_files))
    
    img_cv2 = cv2.imread(ecg_files[ecg_num])                           # reads one ecg
    kernal_edge = np.array([[-1,-1,-1],                          # kernal used for edge detection
                            [-1,8,-1],
                            [-1,-1,-1]])
    edge_img_cv2 = cv2.filter2D(img_cv2, -1, kernal_edge)        # filters with the kernal

    fig, axs = plt.subplots(1,2, figsize=(10,5))                       # figure to show img with plt
    axs[0].imshow(edge_img_cv2)
    axs[1].imshow(img_cv2)
    axs[0].axis("off")
    axs[1].axis("off")
    plt.show()

    xinc = 5
    yinc = 0
    create_canvas_animation = canvas_animation(window)
    ecg_signal_animation(window, create_canvas_animation, xinc,yinc)


def canvas_animation(window):
     # creating start line
    C = Canvas(window, bg="black", width=800, height=200)
    line = C.create_line(0, 100, 800,100 , fill= "#76EE00", width=2)
    C.pack(fill="both", expand=True)
    return C

def ecg_signal_animation(window, C, xinc, yinc):
    signal = C.create_line(0, 100, 10, 100, fill= "black", width=2)
    # loop
    while True:
        C.move(signal, xinc,yinc)
        window.update()
        time.sleep(0.01)
        signal_pos = C.coords(signal)
        xl,yl,xr,yr = signal_pos
        if xl < abs(xinc) or xr >= 800-abs(xinc):
            xl,yl,xr,yr = 0,0,0,0
            C.delete(signal)
            signal = C.create_line(0, 100, 10, 100, fill= "black", width=2)
                
            #signal_pos = C.coords(signal)
        print(signal_pos)
        


  
options = [ 
    "Normal Sinus Rhythms",
    "Bradycardia", 
    "Tachycardia", 
    "Atrial Tachycardia", 
    "Atrial Flutter", 
    "A Fib",
    "Multifocal Atrial Tachycardia",
    "VT",
    "SVT",
    "VF",
    "TdP"
] 
  
clicked = StringVar() 
  
clicked.set( " Heart Rhytms " ) 
  
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
  
button = Button( root , text = " Start " , command = newWindow ).pack() 

  
  
root.mainloop()



