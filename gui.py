# GUI UPDATED 

from tkinter import *
from tkinter import ttk
import tkinter as tk
import numpy as np
from PIL import ImageTk, Image
from glob import glob
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
import normal
import sinusBrady
import sinusTachy
import sinusArr
import vFib


# FUNCTION updates the parameters in the gui from the disease files
# Not optimal since we have to write each parameter again depening on the disease
def update_parameters(ecg_num):
    if ecg_num == 2:
        # create variables for waves 
        var_P_amp = StringVar(parameter_frame)
        var_P_feq = StringVar(parameter_frame)
        var_P_per = StringVar(parameter_frame)
        var_P_amp.set(str(normal.params['p']['a']))
        var_P_feq.set(str(normal.params['p']['t']))
        var_P_per.set(str(normal.params['p']['d']))
        set_parameters_P("P", var_P_amp,var_P_feq, var_P_per)
        
        var_Q_amp = StringVar(parameter_frame)
        var_Q_per = StringVar(parameter_frame)
        var_Q_freq = StringVar(parameter_frame)
        var_Q_amp.set(str(normal.params['q']['a']))
        var_Q_freq.set(str(normal.params['q']['t']))
        var_Q_per.set(str(normal.params['q']['d']))
        set_parameters_P("Q", var_Q_amp,var_Q_freq, var_Q_per)

        var_R_amp = StringVar(parameter_frame)
        var_R_per = StringVar(parameter_frame)
        var_R_freq = StringVar(parameter_frame)
        var_R_amp.set(str(normal.params['r']['a']))
        var_R_per.set(str(normal.params['r']['d']))
        var_R_freq.set("0.0")
        set_parameters_P("R", var_R_amp,var_R_freq, var_R_per)

        var_S_amp = StringVar(parameter_frame)
        var_S_per = StringVar(parameter_frame)
        var_S_freq = StringVar(parameter_frame)
        var_S_amp.set(str(normal.params['s']['a']))
        var_S_freq.set(str(normal.params['s']['t']))
        var_S_per.set(str(normal.params['s']['d']))
        set_parameters_P("S", var_S_amp,var_S_freq, var_S_per)

        var_T_amp = StringVar(parameter_frame)
        var_T_per = StringVar(parameter_frame)
        var_T_freq = StringVar(parameter_frame)
        var_T_amp.set(str(normal.params['t']['a']))
        var_T_freq.set(str(normal.params['t']['t']))
        var_T_per.set(str(normal.params['t']['d']))
        set_parameters_P("T", var_T_amp,var_T_freq, var_T_per)
   
# setting Parameters to the correct place in the gui
def set_parameters_P(wave, var_P_amp,var_P_feq, var_P_per ): 
    if wave =="P":
        row_title = 0
        col_title = 0
        row_amp_label = 1
        col_amp_label = 0
        row_feq_label = 1
        col_feq_label = 1
        row_per_label = 1
        col_per_label = 2
        row_amp_spin = 2
        col_amp_spin = 0
        row_freq_spin = 2
        col_freq_spin = 1
        row_per_spin = 2
        col_per_spin = 2
    elif wave == "Q":
        row_title = 3
        col_title = 0
        row_amp_label = 4
        col_amp_label = 0
        row_feq_label = 4
        col_feq_label = 1
        row_per_label = 4
        col_per_label = 2
        row_amp_spin = 5
        col_amp_spin = 0
        row_freq_spin = 5
        col_freq_spin = 1
        row_per_spin = 5
        col_per_spin = 2
    elif wave == "R":
        row_title = 6
        col_title = 0
        row_amp_label = 7
        col_amp_label = 0
        row_feq_label = 7
        col_feq_label = 1
        row_per_label = 7
        col_per_label = 2
        row_amp_spin = 8
        col_amp_spin = 0
        row_freq_spin = 8
        col_freq_spin = 1
        row_per_spin = 8
        col_per_spin = 2
    elif wave == "S":
        row_title = 9
        col_title = 0
        row_amp_label = 10
        col_amp_label = 0
        row_feq_label = 10
        col_feq_label = 1
        row_per_label = 10
        col_per_label = 2
        row_amp_spin = 11
        col_amp_spin = 0
        row_freq_spin = 11
        col_freq_spin = 1
        row_per_spin = 11
        col_per_spin = 2
    elif wave == "T":
        row_title = 12
        col_title = 0
        row_amp_label = 13
        col_amp_label = 0
        row_feq_label = 13
        col_feq_label = 1
        row_per_label = 13
        col_per_label = 2
        row_amp_spin = 14
        col_amp_spin = 0
        row_freq_spin = 14
        col_freq_spin = 1
        row_per_spin = 14
        col_per_spin = 2

    # creates the title depending on the wave 
    wave_var = StringVar(parameter_frame)
    wave_var = wave + " Wave"

    wave_label = ttk.Label(parameter_frame,borderwidth=10, text = wave_var, font=('Time', 20), foreground="white")
    wave_label.grid(row=row_title, column=col_title, padx=2, pady=2)

    sp_1_label = Label(parameter_frame, text="Amplitude", font=('Time', 12), foreground="#6082B6")
    sp_1_label.grid(row=row_amp_label, column=col_amp_label, padx=2,pady=2)
    sp_1 = Spinbox(parameter_frame, from_=-5, to_=10, increment=0.01, width=10, textvariable=var_P_amp)
    sp_1.grid(row=row_amp_spin, column=col_amp_spin, padx=10,pady=2)

    sp_2_label = Label(parameter_frame, text="Frequency",font=('Time', 12), foreground="#6082B6")
    sp_2_label.grid(row=row_feq_label, column=col_feq_label, padx=2,pady=2)
    sp_3 = Spinbox(parameter_frame, from_=-5, to_=10, increment=0.1, width=10, textvariable=var_P_feq)
    sp_3.grid(row=row_freq_spin, column=col_freq_spin, padx=10,pady=2)

    sp_3_label = Label(parameter_frame, text="Period",font=('Time', 12), foreground="#6082B6")
    sp_3_label.grid(row=row_per_label, column=col_per_label, padx=2,pady=2)
    sp_3 = Spinbox(parameter_frame, from_=-5, to_=10, increment=0.1, width=10, textvariable=var_P_per)
    sp_3.grid(row=row_per_spin, column=col_per_spin, padx=10,pady=2)  

# FUNCTION CREATES NEW WINDOW FOR THE LIVE ECG
def newWindow():
    window= Toplevel(root)
    window.geometry("800x675")
    window.title(clicked.get())

    # disease list need to update since chart shouldnt be next to the ecg signal 
    ecg_list = [["Atrial Flutter", 0],["VF", 1],["Atrial Tachycardia",2],["Sinus Arrhythmia",1],["A Fib",0],["Normal Rhythm", 2],["VT", 6],["Multifocal Atrial Tachycardia",7],
                ["VFib",1], ["Bradycardia",4], ["Tachycardia", 5]]
    
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]
    # update parameters 
    # create function to update the parameters for each wave depending on the disease selected 
    update_parameters(ecg_num)
    # color of background for the main window
    window.configure( background='black' )
    live_signal = animation(window, ecg_num)

    

# Animation
def animation(window,ecg_num):
    
    btm2_frame = tk.LabelFrame(window,bg="black", foreground="#99f20f",text="LEAD II",bd=0, height=250, width=500)
    btm2_frame.pack()
    btm3_frame = tk.LabelFrame(window,bg="black", foreground="#99f20f",text="V1",bd=0, height=250, width=500)
    btm3_frame.pack()
    
    if(clicked.get() == 'Normal Rhythm'):
        t = np.linspace(-2,2,1200)
        y = normal.ecg_waveform
    elif (clicked.get() == 'Sinus Arrhythmia'):
        t = sinusArr.x
        y = sinusArr.y
    elif (clicked.get() == 'Bradycardia'):
        t = sinusBrady.x
        y = sinusBrady.y
    elif (clicked.get() == 'Tachycardia'):
        t = sinusTachy.x
        y = sinusTachy.y
    elif (clicked.get() == 'VFib'):
        t = vFib.x
        y = vFib.y

    # create figure 
    fig, axis = plt.subplots(figsize=(7,2),facecolor="black")                   # background of fig black
    fig2, axis2 = plt.subplots(figsize=(7,2),facecolor="black")
    # function for Funcanimation 
    def update(frame):
    # update the new points after each frame
        animated_plot.set_data(t[:frame], y[:frame])
        return animated_plot
    
    axis.set_xlim([min(t),max(t)])                                # set the limits of time for x
    axis.set_ylim([min(y),max(y)])                                         # Set limit for amplitude for y 
    plt.xticks(np.arange(min(t), max(t)+1, 0.25))
    plt.yticks(np.arange(min(y)-1,max(y), 0.25)) 
    animated_plot, = axis.plot([],[],color="#84f91c")
    
    axis.set_facecolor("black")                                   # set background of graph as black

    # call animation
    animate = FuncAnimation(fig= fig, func= update,frames=len(t),interval=10, repeat="False")
    
    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig, btm2_frame)  
    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(side=LEFT)

    #HR
    HR_frame= tk.LabelFrame(btm2_frame, text="HR",font=('Arial', 15),bg="black", highlightthickness=0, width=100,foreground="#99f20f",height=100)
    HR_frame.pack(side=LEFT)
    d_canvas = tk.Canvas(HR_frame, bg="black",bd=0,highlightcolor="black",highlightthickness=0, width = 18, height=20)
    d_canvas.pack(side=LEFT, anchor=NW)

    # dot blicking
    def blicking():
        cur_color = d_canvas.itemcget(dot, 'fill')
        new_color = 'red' if cur_color == 'black' else 'black'
        d_canvas.itemconfig(dot, fill=new_color)
        d_canvas.after(2000,blicking)

    dot = d_canvas.create_oval(2, 2, 18, 18, fill='red', outline= "")
    blicking()

    HR_canvas = tk.Canvas(HR_frame,highlightthickness=0, bg="black",width = 100, height=100)
    HR_canvas.pack()

    def update_rate():
        HR_canvas.itemconfig(rate, text=str(HR))

    if (ecg_num == 2):
            HR = int(normal.Hr)
    elif (ecg_num ==4):
        HR = int(sinusBrady.Hr)
    # add more heartrates for dieseas
    # ...
    #
    rate = HR_canvas.create_text(50, 50, text="--", font=('Arial', 40), fill= "#99f20f")
    HR_canvas.after(11000,update_rate)


    # buttom frame
    def on_click():
        var1 = StringVar(parameter_frame)
        var2 = StringVar(parameter_frame)
        var3 = StringVar(parameter_frame)

        var1.set("0")
        var2.set("0")
        var3.set("0")

        set_parameters_P("P",var1,var2, var3)
        set_parameters_P("Q",var1,var2,var3)
        set_parameters_P("R",var1,var2, var3)
        set_parameters_P("S",var1,var2, var3)
        set_parameters_P("T",var1,var2, var3)
 
        clicked.set( " Heart Rhytms " ) 
        window.destroy()
    button_frame= Frame(window)
    button_frame.pack()
    button = ttk.Button(button_frame, text="Exit", style="Q.TButton", command=on_click)
    button.pack()


# create main window 
root= Tk()

# title for main window
root.title("ECG Simulator")
#root.configure(background="black")

# open window to screen size
root.attributes('-fullscreen',TRUE)

# style formate for ttk
style = ttk.Style()
# create style
style.theme_create('style_class',
                   settings = {
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
style.configure("Q.TButton", font = ('Time', 15, 'bold'),borderwidth='7', background="red")

# main title
main_frame = Frame(root, highlightbackground="white", highlightthickness=2)
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

# disease container 
disease_frame = ttk.LabelFrame(root, borderwidth=10, text="DISEASES",height=500, width=250)
disease_frame.grid(row= 1,column=1, padx=10, pady=5)

# parameter container
parameter_frame = ttk.LabelFrame(root, borderwidth=10, text="PARAMETERS",takefocus="1", height=600, width=500)
parameter_frame.grid(row= 1,column=0, columnspan=1, padx=10, pady=5, sticky="w")
parameter_frame.grid_propagate(False)

# Options for disease 

options = [ 
        "Normal Rhythm",
        "Bradycardia", 
        "Tachycardia", 
        "Atrial Tachycardia", 
        "Atrial Flutter", 
        "A Fib",
        "Multifocal Atrial Tachycardia",
        "VT",
        "Sinus Arrhythmia",
        "VF",
        "VFib"
    ] 
    # menu for disease 
clicked = StringVar()  
clicked.set( " Heart Rhytms " ) 
drop = OptionMenu( disease_frame , clicked , *options )
drop.place(x = 60, y = 50)

var1 = StringVar(parameter_frame)
var2 = StringVar(parameter_frame)
var3 = StringVar(parameter_frame)

var1.set("0")
var2.set("0")
var3.set("0")

set_parameters_P("P",var1,var2, var3)
set_parameters_P("Q",var1,var2,var3)
set_parameters_P("R",var1,var2, var3)
set_parameters_P("S",var1,var2, var3)
set_parameters_P("T",var1,var2, var3)

# Button to start signal
btn_start = ttk.Button( disease_frame , text = " Start " ,style='S.TButton', command = newWindow)
btn_start.place(x= 100,y = 400)

# close window
button = ttk.Button(root, text="Exit", style="Q.TButton", command=quit)
button.place(x= 400,y=700)


root.mainloop()