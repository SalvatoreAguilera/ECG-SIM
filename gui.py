# GUI UPDATED 
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import numpy as np
from PIL import ImageTk, Image
from glob import glob
import matplotlib.pylab as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
import normal
from pathlib import Path
import print_plot
import csv
import pyautogui as pgui


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
    wave_var = ttk.StringVar(parameter_frame)
    wave_var = wave + " Wave"

    wave_label = ttk.Label(parameter_frame,borderwidth=10, text = wave_var, font=('Time', 20))
    wave_label.grid(row=row_title, column=col_title, padx=2, pady=2)

    sp_1_label = ttk.Label(parameter_frame, text="Amplitude", font=('Time', 14), bootstyle="primary", )
    sp_1_label.grid(row=row_amp_label, column=col_amp_label, padx=2,pady=2)
    sp_1 = ttk.Spinbox(parameter_frame, from_=-5, to_=10, increment=0.01, width=7, textvariable=var_P_amp, bootstyle= "success")
    sp_1.grid(row=row_amp_spin, column=col_amp_spin, padx=10,pady=2)

    sp_2_label = ttk.Label(parameter_frame, text="Frequency",font=('Time', 14), bootstyle="primary")
    sp_2_label.grid(row=row_feq_label, column=col_feq_label, padx=2,pady=2)
    sp_3 = ttk.Spinbox(parameter_frame, from_=-5, to_=10, increment=0.1, width=7, textvariable=var_P_feq, bootstyle= "success")
    sp_3.grid(row=row_freq_spin, column=col_freq_spin, padx=10,pady=2)

    sp_3_label = ttk.Label(parameter_frame, text="Period",font=('Time', 14), bootstyle="primary")
    sp_3_label.grid(row=row_per_label, column=col_per_label, padx=2,pady=2)
    sp_3 = ttk.Spinbox(parameter_frame, from_=-5, to_=10, increment=0.1, width=7, textvariable=var_P_per, bootstyle= "success")
    sp_3.grid(row=row_per_spin, column=col_per_spin, padx=10,pady=2) 

def new_Window():
    newWindow= ttk.Window()
    newWindow.geometry("800x675")
    newWindow.title(clicked.get())
    StaticFrame(newWindow).grid()
    ecg_frame.grid_forget()
    #StaticFrame(newWindow).grid()
    

# FUNCTION CREATES NEW WINDOW FOR THE LIVE ECG
def new_ecg_signal():
        ecg_signal_frame = tk.Frame(btm2_frame, height=frame_size_height,                                      # ecg signal frame inside btm2
                            width=(frame_size_width))
        ecg_signal_frame.grid(row = 0, column=0, columnspan=2)


def ecg_start():
    # turn off start
    if (clicked.get() != "Heart Rhytms"):
        btn_start.config(state="disable")

    # disease list need to update since chart shouldnt be next to the ecg signal 
    ecg_list = [["Atrial Flutter", 0],["VF", 1],["Atrial Tachycardia",2],["Sinus Arrhythmia",1],["A Fib",0],["Normal Rhythm", 2],["VT", 6],["Multifocal Atrial Tachycardia",7],
                ["VFib",1], ["Bradycardia",4], ["Tachycardia", 5]]
    ecg_num = 2 #init to normal rhythm
    
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]
    # update parameters 
    # create function to update the parameters for each wave depending on the disease selected 
    #live_signal = animation(child_window, ecg_num)
    if (clicked.get() == "Heart Rhytms"):
        tk.messagebox.showerror("Error", "Please Select Disease")
    else:
        ecg_frame.config(text=clicked.get())
        animation(ecg_num)

print_x = []
print_y = []
t = np.linspace(-2,2,1200)
y = normal.normal()

def animation(ecg_num):
    global t, y, print_y, print_x
    print_y = []

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
    print_y.extend(y)
    
    # create figure 
    fig1, axis = plt.subplots(figsize=(7,2),facecolor="#2B3F51")                   # background of fig black
    plt.axis("off")

    # inverse
    t2 = np.linspace(-2,2,1200)
    y2 = np.array(y)
    inverse_y2 = -y2

    # previous
    t_p = np.linspace(-2,2,1200)
    x = (1/1000)*t_p + 0.9
    y_p = np.linspace(0.9,0.9,1200)

    fig2, axis2 = plt.subplots(figsize=(7,2),facecolor="#2B3F51")
    plt.axis("off")

    # function for Funcanimation 
    def update(frame):
        global y, print_y
        nonlocal hr, update_requested
        if frame == len(t) - 1 and not update_requested:
            print_y.extend(y)
        if frame == len(t) - 1 and update_requested:
            y = normal.update_ecg()
            hr = normal.get_HR()
            print_y.extend(y)
            update_rate()
            update_requested = False 
        # update the new points after each frame
        
        animated_plot.set_data(t[:frame], y[:frame])
        pulse_sig.set_data([x[frame]], [0])
        animated_plot2.set_data(t2[:frame], inverse_y2[:frame])
        
        return animated_plot, animated_plot2, pulse_sig
    
    axis.set_xlim([-2,2])                                # set the limits of time for x
    axis.set_ylim([0,2.5])                                         # Set limit for amplitude for y 
    axis2.set_xlim([min(t2), max(t2)])                                # set the limits of time for x
    axis2.set_ylim([min(inverse_y2), max(inverse_y2)]) 
    plt.xticks(np.arange(min(t), max(t)+1, 0.25))
    plt.yticks(np.arange(min(y)-1,max(y), 0.25)) 
    animated_plot, = axis.plot([],[],color="#84f91c")
    pulse_sig, = axis.plot([],[],"-", markersize= 20, color="red")
    animated_plot2, = axis2.plot([],[],color="#84f91c")
    axis.set_facecolor("#2B3F51")
    axis2.set_facecolor("#2B3F51")                                   # set background of graph as black


    # call animation
    animate = FuncAnimation(fig= fig1, func= update,frames=len(t),interval=10, repeat="False")
    animate2 = FuncAnimation(fig= fig2, func= update,frames=len(t),interval=10, repeat="False")

    
    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig1, ecg_signal_frame)
    canvas2 = FigureCanvasTkAgg(fig2, V1_signal_frame)
    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(side="left")
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left")


    # dot blicking
    def blicking():
        cur_color = d_canvas.itemcget(dot, 'fill')
        new_color = 'red' if cur_color == '#2B3F51' else '#2B3F51'
        d_canvas.itemconfig(dot, fill=new_color)
        d_canvas.after(1000,blicking)

    blicking()

    def update_rate():
        HR_canvas.itemconfig(rate, text=str(hr))
        pulse_canvas.itemconfig(pulse_result, text=str(pulse_))
        awRR_canvas.itemconfig(awRR_result, text=str(awRR_))
        Tperi_canvas.itemconfig(Tperi_result, text=str(Tp))

    # check for manual input 
    if (var_1.get() == 1):
        hr = hr_entry.get()
    else:
        hr = normal.get_HR()
    if (var_2.get()==1):
        pulse_ = pulse_entry.get()
    #else:
    #    pulse_ = 0
    if ( var_3.get() == 1):
        awRR_ = awRR_entry.get()

    if (var_4.get() == 1):
        Tp = TP_entry.get()
    

    HR_canvas.after(11000,update_rate)

    #stop animation and update 
    def on_click_update():
        nonlocal update_requested
        update_requested = True

    # buttom frame
    def on_click_exit():
        global print_y, print_x
        clicked.set(" Heart Rhythms ")
        print_x = np.linspace(0, 4*(len(print_y)/1200), len(print_y))
        #print_onECG_change()
        ecg_signal_frame.destroy()
        
    button_exit_frame= ttk.Frame(btm4_frame)
    button_exit_frame.grid(row = 0, column = 4)
    button_exit = ttk.Button(button_exit_frame, text="Exit", style="Q.TButton", command=on_click_exit)
    button_exit.grid(row = 0, column = 0)
    
    button_update_frame= ttk.Frame(btm4_frame)
    button_update_frame.grid(row = 0, column = 4)
    button_update = ttk.Button(button_update_frame, text="Update", style="Q.TButton", command=on_click_update)
    button_update.grid(row= 1, column= 0)
    
def update_tk_parameters(*args):
    global update_in_progress
    try:
        w = args[2].get()
    except tk.TclError:
        w = 0.0

    if update_in_progress:
        normal.params[args[0]][args[1]] = w 

def switch_frame(frame):
    for f in frames.values():
        f.grid_forget()  
    frames[frame].grid()

# **************** Print Frame Functions ********************
def print_update(val):
    start = Slider.val  
    end = start + tk.print_window_size  # Set the end based on window size
    tk.print_ax.set_xlim([start, end])  # Adjust x-axis limits
    tk.print_fig.canvas.draw_idle()
    
def print_onECG_change():
    global print_y, print_x
    tk.print_ax.clear()
    tk.print_ax.plot(print_x, print_y)
    tk.print_fig.canvas.draw_idle()

def print_onPrint_click():
    global print_y, print_x
    start_val = (tk.entry_from.get())
    end_val = (tk.entry_to.get())
    if not start_val or not end_val:
        return
    
    start = int(start_val)
    end = int(end_val)
    
    print_x_np = np.array(print_x)  
    print_y_np = np.array(print_y)
    
    print_list_y = print_y_np[(print_x_np >= start) & (print_x_np <= end)]
    end = end - start
    #print_plot.plot_ecg(print_list_y, end)

   
# **************** Simulator Frame Functions ********************

def save_to_csv(filename='ecg_save', folder_path='./simulations'):
    global print_x, print_y
    if tk.filename_entry.get():
        filename = tk.filename_entry.get()
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    file_path = Path(folder_path) / f"{filename}.csv"
    
    with open(file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['X', 'Y'])
        for x_value, y_value in zip(print_x, print_y):
            writer.writerow([x_value, y_value])

    print(f"Data saved to {file_path}")

def load_saved_simulation(*args):
    global print_x, print_y, y, t
    x_values = []
    y_values = []
    path = './simulations/' + clicked_sim_menu.get() + '.csv'
    with open(path, mode='r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  
        for row in reader:
            if row:  
                x_values.append(float(row[0])) 
                y_values.append(float(row[1])) 
    
    print_x = x_values
    print_y =y_values
    y = y_values
    t = x_values
    print_onECG_change()

#######################  Main window for ECG  ########################
window = ttk.Window(themename = "superhero")
window.title("ECG Simulator")
window.attributes('-fullscreen',True)

class StaticFrame(tk.Frame):
    def __init__(self,master,*args,**kwargs):
        tk.Frame.__init__(self,master,*args,**kwargs)

        #screen size
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # size for frames
        #left_width = int(screen_width * 0.10)
        #right_width = int(screen_height * 0.80)

        #left_f = ttk.Frame(self, width= left_width, height= screen_height)
        #left_f.grid(row = 0, column = 0)
        #left_f.grid_propagate(False)
        #right_f = ttk.Frame(self, width= right_width, height= screen_height)
        #right_f.grid(row = 0, column = 1)

        # close window
        #btn_quit = ttk.Button(left_f, text="Exit", style="Q.TButton", command=quit)
        #btn_x_quit = int((left_width/4))
        #btn_quit.config(width= 7)
        #btn_quit.place(x= btn_x_quit,y=1000)

        main_label = ttk.Label(self, text="Electrocardiogram Simulator", font=('Time', 30), foreground="white")
        main_label.grid(row = 0, sticky="n")
     

#StaticFrame(window).grid()
#screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# size for frames
left_width = int(screen_width * 0.20)
right_width = int(screen_height * 0.80)

pf_width_size = int(right_width * .50)
pf_height_size = int(screen_height * .65)
df_width_size = int(right_width * .25)
df_height_size = int(screen_height * .30)
ecg_width_size = int(right_width * .60)
ecg_height_size = int(screen_height * .65)
save_width_size = int(right_width * .33)
save_height_size = int(screen_height * .30)

'''
# button clicked
def on_click(event):
    x, y = pgui.position()
    if (frames.values() == "Electrocardiogram"):
        if ((780 <= x <= 1350) & (150 <= y <= 300)):
            new_Window()

window.bind("<Button-1>", on_click)
'''
#quit
def on_escape(event):
    window.quit() 
window.bind('<Escape>', on_escape)

#### LEFT / RIGHT FRAMES ####
left_frame = ttk.Frame(window, width= left_width, height= screen_height)
left_frame.grid(row = 0, column = 0)
left_frame.grid_propagate(False)
right_frame = ttk.Frame(window, width= right_width, height= screen_height)
right_frame.grid(row = 0, column = 1)

right_frame.columnconfigure(0, weight= 1)
right_frame.columnconfigure(1, weight= 1)
right_frame.columnconfigure(2, weight= 1)
# Button to start signal
btn_start = ttk.Button(left_frame , text = " Start " ,style='S.TButton', command= ecg_start)
btn_x_start = int((left_width/3))
btn_start.config(width= 7)
btn_start.place(x= btn_x_start,y = 500)
# close window
btn_quit = ttk.Button(left_frame, text="Exit", style="Q.TButton", command=quit)
btn_x_quit = int((left_width/3))
btn_quit.config(width= 7)
btn_quit.place(x= btn_x_quit,y=600)

### TOP / BOTTOM FRAMES ######
top_frame = ttk.Frame(right_frame, width = right_width, height= (screen_height* .75))
top_frame.grid(row = 0)

top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
top_frame.columnconfigure(2, weight=1)

bottom_frame = ttk.Frame(right_frame, width = right_width, height= (screen_height* .25))
bottom_frame.grid(row = 1)
bottom_frame.rowconfigure(0, weight=1)
bottom_frame.rowconfigure(1, weight=1)

main_label = ttk.Label(top_frame, text="Electrocardiogram Simulator", font=('Time', 30), foreground="white")
main_label.grid(row = 0, sticky="n")
switch_frame_area = ttk.Frame(top_frame, width= ecg_width_size,height=ecg_height_size)
switch_frame_area.grid(row =1 , column= 1, columnspan=2, sticky='e')

switch_frame_area.columnconfigure(0, weight=1)
switch_frame_area.columnconfigure(1, weight=1)
switch_frame_area.columnconfigure(2, weight=1)

# dashboard 
icon = tk.PhotoImage(file="ecg.png")  
icon_label = ttk.Label(left_frame, image=icon)  
icon_label.grid(row = 0)  
title_dash = ttk.Frame(left_frame, width= left_width, height = (screen_height * 0.10))
title_dash.grid(row = 1, sticky="nsew", pady=10)

content_area = ttk.Frame(switch_frame_area)
content_area.grid(row = 0)
content_area.columnconfigure(0, weight=1)
content_area.columnconfigure(1, weight=1)
content_area.columnconfigure(2, weight=1)
buttons = [
    ("Electrocardiogram", lambda: switch_frame("Electrocardiogram")),
    ("Print", lambda: switch_frame("Print")),
    ("Simulator", lambda: switch_frame("Simulator"))
]

for text, cmd in buttons:
    btn = ttk.Button(title_dash, text=text, command=cmd, width=20, style="Custom.TButton")
    btn.grid(padx=25)

ecg_frame = ttk.LabelFrame(content_area, text="LIVE ECG", width= ecg_width_size,height=ecg_height_size)
print_frame = ttk.LabelFrame(content_area, text="ECG PRINT", width= ecg_width_size,height=ecg_height_size)
print_frame.grid_propagate(False)
sim_frame = ttk.LabelFrame(content_area, text="Simulation", width= ecg_width_size,height=ecg_height_size)

frames = {
    "Electrocardiogram": ecg_frame,
    "Print": print_frame,
    "Simulator": sim_frame
}
ecg_frame.grid()

# parameter container
parameter_frame = ttk.LabelFrame(top_frame, text="PARAMETERS",takefocus="1", width= pf_width_size, height=pf_height_size)
parameter_frame.grid(row= 1,column=0, rowspan= 2,columnspan= 1,padx=2, pady=2, sticky="w")
parameter_frame.grid_propagate(False)
var_P_amp = tk.DoubleVar()
var_P_feq = tk.DoubleVar()
var_P_per = tk.DoubleVar()

var_Q_amp = tk.DoubleVar()
var_Q_feq = tk.DoubleVar()
var_Q_per = tk.DoubleVar()

var_R_amp = tk.DoubleVar()
var_R_feq = tk.DoubleVar()
var_R_per = tk.DoubleVar()

var_S_amp = tk.DoubleVar()
var_S_feq = tk.DoubleVar()
var_S_per = tk.DoubleVar()

var_T_amp = tk.DoubleVar()
var_T_feq = tk.DoubleVar()
var_T_per = tk.DoubleVar()

parameters = [var_P_amp, var_P_feq, var_P_per, var_Q_amp, var_Q_feq, var_Q_per,
              var_R_amp, var_R_feq, var_R_per, var_S_amp, var_S_feq, var_S_per,
              var_T_amp, var_T_feq, var_T_per]

get_new_parameters(parameters)


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

parameter_values = [var.get() for var in parameters]

########live ecg frame############
### SIZE FOR FRAME 
frame_size_width = ecg_width_size * .80                                                                # width for signal frame
frame_size_height = ecg_height_size * .35                                                              # height for signal frame
bot_frame_size_w = ecg_width_size * .20                                                                # bottom frames width
bot_frame_size_h = ecg_height_size * .30                                                               # bottom frames height
hr_width_side = ecg_width_size * .20                                                                   # heatrate width for frame

ecg_frame.columnconfigure(0, weight=1)
ecg_frame.columnconfigure(1, weight=1)
ecg_frame.columnconfigure(2, weight=1)

#### LEAD II FRAME AND LABEL 
leadII_label = ttk.Label(ecg_frame,text="LEAD II", foreground="#84f91c")                                                      # Label for LeadII
leadII_label.grid(row = 0, column = 0, sticky="w")                                                                 # placing leadII
btm2_frame = ttk.Frame(ecg_frame, height=frame_size_height,width= frame_size_width)                     # frame for leadII signal
btm2_frame.grid(row = 1, column=0)
###

# LEAD V1 FRAME AND LABEL 
leadV1_frame = ttk.Label(ecg_frame,text="V1", foreground="#84f91c")                                           # Label for LeadV1
leadV1_frame.grid(row = 2, column=0, sticky= "w")
btm3_frame = ttk.Frame(ecg_frame,height=frame_size_height, width=frame_size_width)                     # frame for V1
btm3_frame.grid(row = 3, column=0)
V1_signal_frame = tk.Frame(btm3_frame,height=frame_size_height,width=frame_size_width)
V1_signal_frame.grid(row = 0, column=0, sticky='w')

btm4_frame = ttk.Frame(ecg_frame, height=bot_frame_size_h,width=bot_frame_size_w)
btm4_frame.grid(row = 4)


### ECG LIVE SIGNAL WITH HR 
ecg_signal_frame = tk.Frame(btm2_frame,height=frame_size_height,width=frame_size_width)           # ecg signal frame inside btm2
ecg_signal_frame.grid(row = 0, column=0)
HR_frame= tk.Frame(ecg_frame,width=hr_width_side,height=100)                                          # frame for heartrate  
HR_frame.grid(row= 1, column=1)
HR_canvas = tk.Canvas(HR_frame,highlightthickness=0, bg="#84f91c",width = 100,                          # Canvas for HR to display numbers
                     height=100)
HR_canvas.grid(row = 0, column=2)
Heart_rate = HR_canvas.create_text(10,10, text="HR", font=('Arial', 15), fill= "red")                   # label for heartrate

d_canvas = tk.Canvas(HR_frame, bg="#84f91c",bd=0,highlightcolor="#84f91c",                                 # canvas to draw the red circle
                     highlightthickness=0, width = 18, height=20)
d_canvas.grid(row=0, column=0)
dot = d_canvas.create_oval(2, 2, 18, 18, fill='red', outline= "")                                      # create the dot
rate = HR_canvas.create_text(50, 50, text="--", font=('Arial', 40), fill= "#99f20f")                    # output the HR
#####


###  BOTTOM FRAME OF ECG FRAME (PULSE, awRR, TPERI)
pulse_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h, padx= 2)
pulse_frame.grid(row = 0, column=1)
pulse_canvas = tk.Canvas(pulse_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw pulse
                         height= bot_frame_size_h, width=100)                           
pulse_canvas.grid(row = 0, column=0)                                                            
pulse = pulse_canvas.create_text(20,20, text="Pulse", font=('Arial', 15), fill= "#0fbef2")              # create pulse label
pulse_result = pulse_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "#0fbef2" )         # create "--" waiting for input

awRR_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h, padx= 2)
awRR_frame.grid(row = 0, column= 2)
awRR_canvas = tk.Canvas(awRR_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw awRR
                         width= 100, height= bot_frame_size_h)                           
awRR_canvas.grid(row = 0, column= 0)                                                            
awRR = awRR_canvas.create_text(20,20, text="awRR", font=('Arial', 15), fill= "white")                                  # create awRR label
awRR_result = awRR_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "white" )         # create "--" waiting for input

Tperi_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h, padx= 2)
Tperi_frame.grid(row = 0, column= 3)
Tperi_canvas = tk.Canvas(Tperi_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw pulse
                         width=100, height= bot_frame_size_h)                           
Tperi_canvas.grid(row = 0, column= 0)                                                          
Tperi = Tperi_canvas.create_text(20,20, text="Tperi", font=('Arial', 15), fill= "#84f91c")              # create pulse label
Tperi_result = Tperi_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "#84f91c" )         # create "--" waiting for input
####

########save test frame###########
#save_frame = ttk.LabelFrame(bottom_frame, text="History", width= save_width_size, height=save_height_size)
#save_frame.grid(row = 0, column= 0)
#save_frame.grid_propagate(False)

########################################## disease container ###########################################################
disease_frame = ttk.LabelFrame(bottom_frame, borderwidth=10, text="DISEASES",height=df_height_size, width=df_width_size)
disease_frame.grid(row= 0,column=0, sticky= "w")
disease_frame.grid_propagate(False)
# Options for disease 
options = [ 
        "Heart Rhytms",
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
### menu for disease 
clicked = tk.StringVar()  
clicked.set( " Heart Rhytms " ) 
drop = ttk.OptionMenu( disease_frame , clicked , *options )
drop.place(x = 30, y = 50)
####################################################################################################################

######################################### MANUAL INPUTS ############################################################
input_= ttk.LabelFrame(bottom_frame, text= "Input Rates", width= (2*save_width_size), height=save_height_size)
input_.grid(row = 0, column= 1, columnspan= 2)
input_.grid_propagate(False)

def check_HR():
    if var_1.get() == 1:
        hr_entry.config(state="normal")
    if var_2.get() ==1:
        pulse_entry.config(state="normal")
    if var_3.get() ==1:
        awRR_entry.config(state="normal")
    if var_4.get() ==1:
        TP_entry.config(state="normal")

def manual_():
    hr = hr_entry.get()
    pulse_result = pulse_entry.get()
    awRR_result = awRR_entry.get()
    Tperi_result = TP_entry.get()

var_1 = tk.IntVar()
HR_checkbutton= ttk.Checkbutton(input_, text="Manually input HR", variable=var_1,onvalue= 1, offvalue= 0, command= check_HR)
HR_checkbutton.grid(row = 1, column= 1)
hr_entry = tk.Entry(input_, state="disable")
hr_entry.grid(row = 2, column= 2,)

var_2 = tk.IntVar()
Pulse_checkbutton= ttk.Checkbutton(input_, text="Manually input Pulse", variable=var_2,onvalue= 1, offvalue= 0, command= check_HR)
Pulse_checkbutton.grid(row = 3, column= 1)
pulse_entry = tk.Entry(input_, state="disable")
pulse_entry.grid(row = 4, column= 2,)

var_3 = tk.IntVar()
awRR_checkbutton= ttk.Checkbutton(input_, text="Manually input awRR", variable=var_3,onvalue= 1, offvalue= 0, command= check_HR)
awRR_checkbutton.grid(row = 5, column= 1)
awRR_entry = tk.Entry(input_, state="disable")
awRR_entry.grid(row = 6, column= 2,)

var_4 = tk.IntVar()
TP_checkbutton= ttk.Checkbutton(input_, text="Manually input Tperi", variable=var_4,onvalue= 1, offvalue= 0, command= check_HR)
TP_checkbutton.grid(row = 8, column= 1)
TP_entry = tk.Entry(input_, state="disable")
TP_entry.grid(row = 9, column= 2,)

button_awRR= ttk.Button(input_, text="Enter", command= manual_)
button_awRR.grid(row = 10, column= 2)

#placeholder = ttk.LabelFrame(bottom_frame, text= "Saved Test", width=save_width_size, height=save_height_size)
#placeholder.grid(row = 0, column= 3)
#placeholder.grid_propagate(False)
####################################################################################################################


#***************************PRINT FRAME********************************
print_main_frame = ttk.Frame(print_frame)
print_main_frame.grid(row = 0)
print_frame = ttk.LabelFrame(print_frame, borderwidth=10, text="Editor")
print_frame.grid(row = 1)

#plot frame
print_fig, print_ax = plt.subplots(figsize=(4, 2))
print_ax.plot(print_x, print_y)
print_window_size = 5

print_ax.set_xlim([0, print_window_size])
canvas = FigureCanvasTkAgg(print_fig, master=print_frame)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

slider_ax = print_fig.add_axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(slider_ax, 'Time (s)', 0, 30 - print_window_size, valinit=0)

slider.on_changed(print_update)

label_range = ttk.Label(print_frame, text="Range")
label_range.pack(pady=10, padx=10)

input_frame = ttk.Frame(print_frame)
input_frame.pack()

label_from = ttk.Label(input_frame, text="From:")
label_from.pack(side=tk.LEFT, padx=5)
entry_from = ttk.Entry(input_frame, width=10)
entry_from.pack(side=tk.LEFT, padx=5)


label_to = ttk.Label(input_frame, text="To:")
label_to.pack(side=tk.LEFT, padx=5)
entry_to = ttk.Entry(input_frame)
entry_to.pack(side=tk.LEFT, padx=5)

label_filename = ttk.Label(print_frame, text="Filename:")
label_filename.pack(pady=10, padx=10)  
filename_entry = ttk.Entry(print_frame, width=30) 
filename_entry.pack(pady=10, padx=10)

submit_button = ttk.Button(print_frame, text="Print", command=print_onPrint_click)
submit_button.pack(pady=20)

#save_button = ttk.Button(print_frame, text="Save", command=save_to_csv)
#save_button.pack(pady=0, padx=20)

#***************************SIMULATOR FRAME********************************
sim_main_frame = ttk.Frame(sim_frame)
sim_main_frame.pack(padx=10, pady=5) 

sim_main_label = ttk.Label(sim_main_frame, text="Simulator ECG", font=('Time', 30), foreground="white")
sim_main_label.pack(padx=10) 

simulator_frame = ttk.LabelFrame(sim_frame, borderwidth=10, text="Simulations", height=500, width=500)
simulator_frame.pack(padx=10, pady=10, side="top", fill="y")

def get_file_names(folder_path):
    return [file.stem for file in Path(folder_path).iterdir() if file.is_file()]

options_sim = get_file_names('./simulations')
clicked_sim_menu = tk.StringVar()
clicked_sim_menu.set( " Simulations " ) 
save_sim_drop = ttk.OptionMenu( simulator_frame , clicked_sim_menu , *options_sim )
save_sim_drop.place(x = 60, y = 50)

clicked_sim_menu.trace_add("write", load_saved_simulation)



window.mainloop()
