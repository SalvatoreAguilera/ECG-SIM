import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt
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

