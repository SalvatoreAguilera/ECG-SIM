import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
import time
from tkinter import *
from glob import glob

root = Tk() 
  
root.geometry( "500x300" ) 
  
def newWindow(): 
    window = Toplevel(root)
    window.geometry( "800x200" )
    window.title( clicked.get() )

    ecg_list = [["Atrial Flutter", 0],["VF", 1],["Atrial Tachycardia",2],["SVT",3],["A Fib",4],["Normal Sinus Rhythms", 5],["VT", 6],["Multifocal Atrial Tachycardia",7],
                ["TdP",8], ["Bradycardia",9], ["Tachycardia", 10]]
    print(clicked.get())
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]
        else:
            ecg_num = ecg_list[5][1]

    print(clicked.get())
    window.configure( background='black' )

    Label(window, text="ECG", font=("Arial", 18)).pack()

    ecg_files = glob('./ECG/*.jpeg')                             # loads files to a dataset
    print(len(ecg_files))
    
    img_cv2 = cv2.imread(ecg_files[ecg_num])                           # reads one ecg

    fig, axs = plt.subplots(figsize=(10,5))                       # figure to show img with plt
    axs.imshow(img_cv2)
    axs.axis("off")
    plt.show()

# equation
    t = np.linspace(0,10,100)
    y= np.sin(t)

    # create figure 
    fig, axis = plt.subplots(facecolor="black")                   # background of fig black

    axis.set_xlim([min(t),max(t)])                                # set the limits of time for x
    axis.set_ylim([-2,2])                                         # Set limit for amplitude for y

    animated_plot, = axis.plot([],[])                             # empty plot to set the x and y from the equation

    axis.set_facecolor("black")                                   # set background of graph as black
    
    def update(frame):

        # update the new points after each frame
        animated_plot.set_data(t[:frame], y[:frame])

        return animated_plot
    
    # call animation
    animate = FuncAnimation(fig= fig, func= update,frames=len(t),interval=25)

    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig, master=window)  

    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP,fill = BOTH, expand= 1)
  
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

# button to quit
button = Button(master=root, text="Quit", command=quit)
button.pack(side= BOTTOM)

root.mainloop()





