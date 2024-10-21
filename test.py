# GUI UPDATED 

from tkinter import *
#from tkinter import ttk
import ttkbootstrap as ttk
import tkinter as tk
import numpy as np
from PIL import ImageTk, Image
from glob import glob
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
import normal
update_in_progress = False
# FUNCTION TO GET THE NEW PARAMETERS FROM THE GUI
def get_new_parameters(parameters):
    global update_in_progress
    update_in_progress = False
    
    var_P_amp, var_P_feq, var_P_per, var_Q_amp, var_Q_feq, var_Q_per, \
    var_R_amp, var_R_feq, var_R_per, var_S_amp, var_S_feq, var_S_per, \
    var_T_amp, var_T_feq, var_T_per = parameters

    var_P_amp.set(normal.params['p']['a'])
    var_P_feq.set(normal.params['p']['d'])
    var_P_per.set(normal.params['p']['t'])
    set_parameters_P("P", var_P_amp, var_P_feq, var_P_per)

    var_Q_amp.set(normal.params['q']['a'])
    var_Q_feq.set(normal.params['q']['d'])
    var_Q_per.set(normal.params['q']['t'])
    set_parameters_P("Q", var_Q_amp, var_Q_feq, var_Q_per)

    var_R_amp.set(normal.params['r']['a'])
    var_R_feq.set(normal.params['r']['d'])
    var_R_per.set(normal.params['r']['t'])
    set_parameters_P("R", var_R_amp, var_R_feq, var_R_per)

    var_S_amp.set(normal.params['s']['a'])
    var_S_feq.set(normal.params['s']['d'])
    var_S_per.set(normal.params['s']['t'])
    set_parameters_P("S", var_S_amp, var_S_feq, var_S_per)

    var_T_amp.set(normal.params['t']['a'])
    var_T_feq.set(normal.params['t']['d'])
    var_T_per.set(normal.params['t']['t'])
    set_parameters_P("T", var_T_amp, var_T_feq, var_T_per)
    
    update_in_progress = True



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
    ecg_num = 2 #init to normal rhythm
    
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]
    # update parameters 
    # create function to update the parameters for each wave depending on the disease selected 
    
    # color of background for the main window
    window.configure( background='black' )
    live_signal = animation(window, ecg_num)
    

    
t = np.linspace(-2,2,1200)
y = normal.normal()

def animation(window,ecg_num):
    global t, y
    btm2_frame = tk.LabelFrame(window,bg="black", foreground="#99f20f",text="LEAD II",bd=0, height=250, width=500)
    btm2_frame.pack()
    btm3_frame = tk.LabelFrame(window,bg="black", foreground="#99f20f",text="V1",bd=0, height=250, width=500)
    btm3_frame.pack()
    update_requested = False
    if(clicked.get() == 'Normal Rhythm'):
        t = np.linspace(-2,2,1200)
        y = normal.normal()
    elif (clicked.get() == 'Sinus Arrhythmia'):
        t = np.linspace(-2,2,1200)
        y = normal.sinus_arrythmia()
    elif (clicked.get() == 'Bradycardia'):
        t = np.linspace(-2,2,1200)
        y = normal.sinus_brady()
    elif (clicked.get() == 'Tachycardia'):
        t = np.linspace(-2,2,1200)
        y = normal.sinus_tachy()
    elif (clicked.get() == 'VFib'):
        t = np.linspace(-2,2,1200)
        y = normal.vfib()
    else:
        t = np.linspace(-2,2,1200)
        y = normal.update_ecg()
         
    get_new_parameters(parameters)
    
    # create figure 
    fig1, axis = plt.subplots(figsize=(7,2),facecolor="black")                   # background of fig black
    fig2, axis2 = plt.subplots(figsize=(7,2),facecolor="black")
    
    # function for Funcanimation 
    def update(frame):
        global y, update_requested
        # If we're at the last frame of the current animation
        if frame == len(t) - 1 and update_requested:
            # Apply the new parameters
            y = normal.update_ecg()
            hr = normal.get_HR()
            update_rate()
            update_requested = False  # Reset the flag

        
        animated_plot.set_data(t[:frame], y[:frame])
        
        return animated_plot
    
    axis.set_xlim([min(t),max(t)])                                # set the limits of time for x
    axis.set_ylim([min(y),max(y)])                                         # Set limit for amplitude for y 
    plt.xticks(np.arange(min(t), max(t)+1, 0.25))
    plt.yticks(np.arange(min(y)-1,max(y), 0.25)) 
    animated_plot, = axis.plot([],[],color="#84f91c")
    
    axis.set_facecolor("black")                                   # set background of graph as black

    # call animation
    animate = FuncAnimation(fig= fig1, func= update,frames=len(t),interval=10, repeat="False")
    
    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig1, btm2_frame)
      
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
        HR_canvas.itemconfig(rate, text=str(hr))


    hr = normal.get_HR()

    rate = HR_canvas.create_text(50, 50, text="--", font=('Arial', 40), fill= "#99f20f")
    HR_canvas.after(11000,update_rate)

    
    def on_click_update():
        global update_requested
        update_requested = True
        
        

    # buttom frame
    def on_click_exit():
        clicked.set(" Heart Rhythms ")
        window.destroy()
    
    button_exit_frame= Frame(window)
    button_exit_frame.pack()
    button_exit = ttk.Button(button_exit_frame, text="Exit", style="Q.TButton", command=on_click_exit)
    button_exit.pack()
    
    button_update_frame= Frame(window)
    button_update_frame.pack()
    button_update = ttk.Button(button_update_frame, text="Update", style="Q.TButton", command=on_click_update)
    button_update.pack()
    
def update_tk_parameters(*args):
    global update_in_progress
    try:
        w = args[2].get()
    except TclError:
        w = 0.0

    if update_in_progress:
        normal.params[args[0]][args[1]] = w 

    
 

root = ttk.Window(themename="cyborg")
root.title("ECG Simulator")
root.attributes('-fullscreen', False)

# Quit function
def on_escape(event):
    root.quit()
root.bind('<Escape>', on_escape)

# Main title frame
main_frame = Frame(root, highlightbackground="white", highlightthickness=2)
main_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

# Main label
main_label = Label(main_frame, text="Electrocardiogram Simulator", font=('Time', 30), foreground="white")
main_label.grid(row=0, column=3, padx=10)

# Disease container
disease_frame = ttk.LabelFrame(root, borderwidth=10, text="DISEASES", height=600, width=250)
disease_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

# Parameter container
parameter_frame = ttk.LabelFrame(root, borderwidth=10, text="PARAMETERS", takefocus="1", height=600, width=500)
parameter_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
parameter_frame.grid_propagate(False)

# Configure dynamic resizing for root window
root.grid_rowconfigure(1, weight=1)  # Allow disease_frame and parameter_frame to expand vertically
root.grid_columnconfigure(0, weight=3)  # Make parameter_frame expand more (3x space of disease_frame)
root.grid_columnconfigure(1, weight=1)  # disease_frame expands less

# Options for disease
options = [
    "Normal Rhythm", "Bradycardia", "Tachycardia", "Atrial Tachycardia",
    "Atrial Flutter", "A Fib", "Multifocal Atrial Tachycardia", "VT",
    "Sinus Arrhythmia", "VF", "VFib"
]
clicked = StringVar()
clicked.set("Heart Rhythms")
drop = OptionMenu(disease_frame, clicked, *options)
drop.place(x=60, y=50)

# Parameter variables
var_P_amp = DoubleVar()
var_P_feq = DoubleVar()
var_P_per = DoubleVar()

var_Q_amp = DoubleVar()
var_Q_feq = DoubleVar()
var_Q_per = DoubleVar()

var_R_amp = DoubleVar()
var_R_feq = DoubleVar()
var_R_per = DoubleVar()

var_S_amp = DoubleVar()
var_S_feq = DoubleVar()
var_S_per = DoubleVar()

var_T_amp = DoubleVar()
var_T_feq = DoubleVar()
var_T_per = DoubleVar()

parameters = [var_P_amp, var_P_feq, var_P_per, var_Q_amp, var_Q_feq, var_Q_per,
              var_R_amp, var_R_feq, var_R_per, var_S_amp, var_S_feq, var_S_per,
              var_T_amp, var_T_feq, var_T_per]

get_new_parameters(parameters)

# Parameter tracing
var_P_amp.trace_add("write", lambda *args: update_tk_parameters("p", "a", var_P_amp))
var_P_feq.trace_add("write", lambda *args: update_tk_parameters("p", "d", var_P_feq))
var_P_per.trace_add("write", lambda *args: update_tk_parameters("p", "t", var_P_per))

var_Q_amp.trace_add("write", lambda *args: update_tk_parameters("q", "a", var_Q_amp))
var_Q_feq.trace_add("write", lambda *args: update_tk_parameters("q", "d", var_Q_feq))
var_Q_per.trace_add("write", lambda *args: update_tk_parameters("q", "t", var_Q_per))

var_R_amp.trace_add("write", lambda *args: update_tk_parameters("r", "a", var_R_amp))
var_R_feq.trace_add("write", lambda *args: update_tk_parameters("r", "d", var_R_feq))
var_R_per.trace_add("write", lambda *args: update_tk_parameters("r", "t", var_R_per))

var_S_amp.trace_add("write", lambda *args: update_tk_parameters("s", "a", var_S_amp))
var_S_feq.trace_add("write", lambda *args: update_tk_parameters("s", "d", var_S_feq))
var_S_per.trace_add("write", lambda *args: update_tk_parameters("s", "t", var_S_per))

var_T_amp.trace_add("write", lambda *args: update_tk_parameters("t", "a", var_T_amp))
var_T_feq.trace_add("write", lambda *args: update_tk_parameters("t", "d", var_T_feq))
var_T_per.trace_add("write", lambda *args: update_tk_parameters("t", "t", var_T_per))

# Button to start signal
btn_start = ttk.Button(disease_frame, text="Start", bootstyle='danger', command=newWindow)
btn_start.place(x=100, y=400)

# Close window button
button = ttk.Button(root, text="Exit", bootstyle="danger", command=quit)
button.place(x=500, y=700)

root.mainloop()
