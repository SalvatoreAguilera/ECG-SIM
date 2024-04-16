from tkinter import *
from tkinter import ttk
from glob import glob
from PIL import ImageTk, Image
import pandas as pd
import numpy as np
import cv2
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
from waves import normal


# animation function
def animation(window,ecg_num):
    btm_frame = ttk.LabelFrame(window, text ="ECG CHART", height=350, width=700)
    #btm_frame.grid(row=0,column=0,padx=10,pady=10)
    btm_frame.pack()
    # get image 
    ecg_files = glob('./ECG/*.jpeg') 
    image_chart = Image.open(ecg_files[ecg_num])
    
    # Resize the image
    resize_image_chart = image_chart.resize((500, 300))
    img_chart = ImageTk.PhotoImage(resize_image_chart)
    img1_chart = Label(btm_frame,image=img_chart)
    img1_chart.image = img_chart
    #img1_chart.grid(row=0,column=0)
    img1_chart.pack()
    #img1_chart.place(x=5,y=5)

    btm2_frame = Frame(window)
    btm2_frame.pack()

    t = normal.x
    y= normal.y
    #y = wave.y
    # create figure 
    fig, axis = plt.subplots(facecolor="black")                   # background of fig black

    axis.set_xlim([min(t),max(t)])                                # set the limits of time for x
    axis.set_ylim([min(y),max(y)])                                         # Set limit for amplitude for y
    
    plt.grid(color="#023020")
    
    plt.xticks(np.arange(min(t), max(t)+1, 0.05))
    plt.yticks(np.arange(min(y)-1,max(y), 0.05))
    
    animated_plot, = axis.plot([],[], color="#84F91C")  
    #animated_plot3, = axis.plot([],[], "o", markersize="10",color="black")

    axis.set_facecolor("black")                                   # set background of graph as black

    # function for Funcanimation 
    def update(frame):
    # update the new points after each frame
        animated_plot.set_data(t[:frame], y[:frame])
    
        return animated_plot
    
    # call animation
    animate = FuncAnimation(fig= fig, func= update,frames=len(t),interval=125, repeat=TRUE)

    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig, window)  

    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(fill=X,expand=0)

   
    

# Function to create new window
def newWindow(): 
    window = Toplevel(root)
    window.geometry( "600x520" )
    window.title( clicked.get() )

    ecg_list = [["Atrial Flutter", 0],["VF", 1],["Atrial Tachycardia",2],["SVT",3],["A Fib",4],["Normal Sinus Rhythms", 5],["VT", 6],["Multifocal Atrial Tachycardia",7],
                ["TdP",8], ["Bradycardia",9], ["Tachycardia", 10]]
    #print(clicked.get())
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]


    #print(clicked.get())
    window.configure( background='black' )

    # ECG TITLE 
    #live_label = LabelFrame(window, text= "LIVE FEED", width= 800, height= 300, background='black')
    #live_label.grid(row=0,column=0, columnspan=3)   

    #ecg_files = glob('./ECG/*.jpeg')                             # loads files to a dataset
    #print(len(ecg_files))

     # call animation function
    #live_signal = animation(window,live_label) 
    live_signal = animation(window, ecg_num)


### MAIN WINDOW ###

root= Tk()
root.title("ECG Simulator")
root.iconbitmap('./icon_logo.ico')
root.geometry("800x750")

main_frame = Frame(root, highlightbackground="#6082B6", highlightthickness=2)
main_frame.grid(row= 0,column=0, padx=10, pady=5)

# get image 
image = Image.open("./1.jpeg")
 
# Resize the image
resize_image = image.resize((50, 50))
img = ImageTk.PhotoImage(resize_image)
img1 = Label(image=img)
img1.image = img
img1.grid(row=0,column=0, padx=10, pady=10, sticky="w")
img1.place(x=5,y=5)

main_label = Label(main_frame, text = "Electrocardiogram Simulator" , font=('Time', 30), foreground="white")
main_label.grid(row= 0, column= 3, padx=10)

# style for label frame
style = ttk.Style()

# create style
style.theme_create('style_class',
                   settings = {
                    #'TLabelframe': {
                    #        'configure':{
                    #            'background': '#6082B6'
                    #        }
                    #},
                    'TLabelframe.Label': {
                        'configure': {
                            'background': '#6082B6',
                            'font' : 'Time 20'
                        }
                    }
           }
)
style.theme_use('style_class')
style.configure("S.TButton", font = ('Time', 15, 'bold'),borderwidth='4', background="#6082B6")
style.configure("Q.TButton", font = ('Time', 15, 'bold'),borderwidth='4', background="red")

left_frame = ttk.LabelFrame(root, text="ECG WAVE",height=400, width=500)
left_frame.grid(row=1, column=0, padx= 10, pady=10, sticky="N")

# get image 
image2 = Image.open("./ECG_wave.JPG")
 
# Resize the image
resize_image2 = image2.resize((400, 350))
img_2 = ImageTk.PhotoImage(resize_image2)
img2 = Label(image=img_2)
img2.image = img_2
#img2.grid(row=1,column=0, padx=10, sticky="w")
img2.place(x=50,y=130)

right_frame = ttk.LabelFrame(root, text="ECG Disease", height=400, width=260) 
right_frame.grid(row=1,column=2, padx =10, pady=10, sticky="N")

# Options for disease 
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
# menu for disease 
clicked = StringVar()  
clicked.set( " Heart Rhytms " ) 
drop = OptionMenu( right_frame , clicked , *options )
drop.place(x = 60, y = 50)

# Button to start signal
btn_start = ttk.Button( right_frame , text = " Start " ,style='S.TButton', command = newWindow)
btn_start.place(x= 110,y = 100)


# button to quit
button = ttk.Button(right_frame, text="Quit", style="Q.TButton", command=quit)
button.place(x=110,y=300)

# bottom frame
bottom_frame = ttk.LabelFrame(root, text="ECG Parameters", height=200, width=500) 
bottom_frame.grid(row=3,column=0, columnspan=3, padx =10, pady=10, sticky='nesw')

# create canvas
canvas = Canvas(bottom_frame)
scrollbar = ttk.Scrollbar(bottom_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# create frame for scrolling
content_frame = ttk.Frame(canvas)

#Configure the Canvas and Scrollable Content Frame
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

def updateParameters():
   amp = sp_1.get()
   frequency =sp_2.get()
   period = sp_3.get()

   print(amp, frequency,period)

p_wave = Label(content_frame, text = "P Wave", font= ('Time', 20), bg="#222222", foreground='#6082B6')
p_wave.grid(row=0, column=0, padx=10, pady=5, sticky= 'w')
# p wave
p_wave = Label(content_frame, text = "P Wave", font= ('Time', 20), bg="#222222", foreground='#6082B6')
p_wave.grid(row=0, column=0, padx=10, pady=5, sticky= 'w')
sp_1_label = Label(content_frame, text="Amplitude", font=('Time', 15), foreground="#6082B6")
sp_1_label.grid(row=1, column=0, padx=0,pady=2)
sp_1 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command= updateParameters, wrap=True)
sp_1.grid(row=2, column=0, padx=20,pady=5)

sp_2_label = Label(content_frame, text="Frequency",font=('Time', 15), foreground="#6082B6")
sp_2_label.grid(row=1, column=1, padx=0,pady=2)
sp_2 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command=updateParameters, wrap=TRUE)
sp_2.grid(row=2, column=1, padx=20,pady=5)

sp_3_label = Label(content_frame, text="Period", font=('Time', 15), foreground="#6082B6")
sp_3_label.grid(row=1, column=2, padx=0,pady=2)
sp_3 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command= updateParameters, wrap=TRUE)
sp_3.grid(row=2, column=2, padx=20,pady=5)


# R wave
r_wave = Label(content_frame, text = "R Wave", font= ('Time', 20), bg="#222222", foreground='#6082B6')
r_wave.grid(row=3, column=0, padx=10, pady=5, sticky= 'w')


sp_4_label = Label(content_frame, text="Amplitude", font=('Time', 15), foreground="#6082B6")
sp_4_label.grid(row=4, column=0, padx=0,pady=2)
sp_4 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command= updateParameters, wrap=True)
sp_4.grid(row=5, column=0, padx=20,pady=5)


sp_5_label = Label(content_frame, text="Frequency",font=('Time', 15), foreground="#6082B6")
sp_5_label.grid(row=4, column=1, padx=0,pady=2)
sp_5 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command=updateParameters, wrap=TRUE)
sp_5.grid(row=5, column=1, padx=20,pady=5)


sp_6_label = Label(content_frame, text="Period", font=('Time', 15), foreground="#6082B6")
sp_6_label.grid(row=4, column=2, padx=0,pady=2)
sp_6 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command= updateParameters, wrap=TRUE)
sp_6.grid(row=5, column=2, padx=20,pady=5)


# T wave
T_wave = Label(content_frame, text = "T Wave", font= ('Time', 20), bg="#222222", foreground='#6082B6')
T_wave.grid(row=6, column=0, padx=10, pady=5, sticky= 'w')


sp_7_label = Label(content_frame, text="Amplitude", font=('Time', 15), foreground="#6082B6")
sp_7_label.grid(row=7, column=0, padx=0,pady=2)
sp_7 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command= updateParameters, wrap=True)
sp_7.grid(row=8, column=0, padx=20,pady=5)


sp_8_label = Label(content_frame, text="Frequency",font=('Time', 15), foreground="#6082B6")
sp_8_label.grid(row=7, column=1, padx=0,pady=2)
sp_8 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command=updateParameters, wrap=TRUE)
sp_8.grid(row=8, column=1, padx=20,pady=5)


sp_9_label = Label(content_frame, text="Period", font=('Time', 15), foreground="#6082B6")
sp_9_label.grid(row=7, column=2, padx=0,pady=2)
sp_9 = Spinbox(content_frame, from_=0, to_=10, increment=0.5, command= updateParameters, wrap=TRUE)
sp_9.grid(row=8, column=2, padx=20,pady=5)



# Create Window Resizing Configuration
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
bottom_frame.columnconfigure(0, weight=1)
bottom_frame.rowconfigure(0, weight=1)

#Pack Widgets onto the Window
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")

def _on_mousewheel(event):
   canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

#canvas.grid(row=2,column=0, columnspan=3, padx =10, pady=10 )



root.mainloop()