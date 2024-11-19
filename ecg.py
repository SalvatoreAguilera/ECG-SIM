
# ECG SIMULATOR
# Senior Project II
#  
import tkinter as tk
import ttkbootstrap as ttk
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
import normal
import os

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

    wave_label = ttk.Label(parameter_frame,
                           borderwidth=10, 
                           text = wave_var, 
                           font=('Time', 20))
    wave_label.grid(row=row_title, 
                    column=col_title, 
                    padx=2, 
                    pady=2)

    sp_1_label = ttk.Label(parameter_frame,
                           text="Amplitude", 
                           font=('Time', 14), 
                           bootstyle="primary", )
    sp_1_label.grid(row=row_amp_label,column=col_amp_label, padx=2,pady=2)
    sp_1 = ttk.Spinbox(parameter_frame, 
                       from_=-5, 
                       to_=10, 
                       increment=0.01, 
                       width=7, 
                       textvariable=var_P_amp, 
                       bootstyle= "success")
    sp_1.grid(row=row_amp_spin, column=col_amp_spin, padx=10,pady=2)

    sp_2_label = ttk.Label(parameter_frame, 
                           text="Frequency",
                           font=('Time', 14), 
                           bootstyle="primary")
    sp_2_label.grid(row=row_feq_label, column=col_feq_label, padx=2,pady=2)

    sp_3 = ttk.Spinbox(parameter_frame, 
                       from_=-5, to_=10, 
                       increment=0.1, 
                       width=7, 
                       textvariable=var_P_feq, 
                       bootstyle= "success")
    sp_3.grid(row=row_freq_spin, column=col_freq_spin, padx=10,pady=2)

    sp_3_label = ttk.Label(parameter_frame, 
                           text="Period",
                           font=('Time', 14), 
                           bootstyle="primary")
    sp_3_label.grid(row=row_per_label, column=col_per_label, padx=2,pady=2)
    sp_3 = ttk.Spinbox(parameter_frame, 
                       from_=-5, 
                       to_=10, 
                       increment=0.1, 
                       width=7, 
                       textvariable=var_P_per, 
                       bootstyle= "success")
    sp_3.grid(row=row_per_spin, column=col_per_spin, padx=10,pady=2) 

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

#stop animation and update 
def on_click_update():
    global update_requested
    update_requested = True

def new_Window():
    newWindow= ttk.Window()
    #newWindow.geometry("800x675")
    newWindow.attributes('fullscreen', True)
    newWindow.title(combo.get())
    btn_start.config(state="disable")
    ecg_frame.grid_forget()

def set_new_window(newWindow):
    new_ecg_width_size = newWindow.winfo_screenwidth()
    
    new_ecg_height_size = newWindow.winfo_screenheight()

    new_hr_width_side = new_ecg_width_size * .10  # heart rate width for frame
    new_frame_size_width = new_ecg_width_size - new_hr_width_side  # width for signal frame
    new_frame_size_height = new_ecg_height_size * .30  # height for signal frame
    new_bot_frame_size_w = new_ecg_width_size * .25  # bottom frames width
    new_bot_frame_size_h = new_ecg_height_size * .20  # bottom frames height
    
    # resize 
    newWindow.columnconfigure(0, weight= 1)
    newWindow.rowconfigure(0, weight = 1)

    # Create the main ECG frame
    new_ecg_frame = ttk.LabelFrame(newWindow, 
                              width= new_ecg_width_size, 
                              height= new_ecg_height_size)
    new_ecg_frame.grid(row=0, column=0)
    new_ecg_frame.grid_propagate(False)
    new_ecg_frame.columnconfigure(0, weight=1)
    new_ecg_frame.rowconfigure(0, weight=1)
    #new_ecg_frame.rowconfigure(1, weight=1)
    new_ecg_frame.rowconfigure(2, weight=1)
    new_ecg_frame.rowconfigure(3, weight = 1)
    new_ecg_frame.rowconfigure(4, weight=3)


    #### LEAD II FRAME AND LABEL 
    new_leadII_label = ttk.Label(new_ecg_frame, 
                                 text="LEAD II", 
                                 foreground="#84f91c")
    new_leadII_label.grid(row=0, column=0, sticky="w")
    

    new_leadII_frame = ttk.LabelFrame(new_ecg_frame, 
                                 height=new_frame_size_height, 
                                 width=new_frame_size_width)
    new_leadII_frame.grid_propagate(False)
    new_leadII_frame.grid(row=1, column=0)
    new_leadII_frame.columnconfigure(0, weight=1)

    # ECG Live Signal with HR
    new_II_frame = tk.LabelFrame(new_leadII_frame, 
                            height=new_frame_size_height, 
                            width=new_frame_size_width)
    new_II_frame.grid(row=0, column=0, sticky = 'w')
    new_II_frame.grid_propagate(False)

    new_HR_frame = tk.LabelFrame(new_leadII_frame, 
                            width=new_hr_width_side, 
                            height=100)
    new_HR_frame.grid(row=0, column=1, sticky="e")

    new_HR_canvas = tk.Canvas(new_HR_frame, 
                              highlightthickness=0, 
                              width=100, 
                              height=100)
    new_HR_canvas.grid(row=0, column=2)
    new_Heart_rate = new_HR_canvas.create_text(10, 10, 
                                               text="HR", 
                                               font=('Arial', 15), 
                                               fill="red")

    new_d_canvas = tk.Canvas(new_HR_frame, 
                             bg="#84f91c", 
                             bd=0, 
                             highlightcolor="#84f91c",
                             highlightthickness=0, 
                             width=18, 
                             height=20)
    new_d_canvas.grid(row=0, column=0)
    new_dot = new_d_canvas.create_oval(2, 2, 18, 18, 
                                       fill='red', 
                                       outline="")
    new_rate = new_HR_canvas.create_text(50, 50, 
                                         text="--", 
                                         font=('Arial', 40), 
                                         fill="#99f20f")

    # LEAD V1 FRAME AND LABEL 
    new_leadV1_label = ttk.Label(new_ecg_frame, 
                                 text="V1",
                                 font=("Time", 15), 
                                 foreground="#84f91c")
    new_leadV1_label.grid(row=2, column=0, sticky="w")
    new_V1_frame = ttk.LabelFrame(new_ecg_frame, 
                                 height=new_frame_size_height, 
                                 width=new_frame_size_width)
    
    new_V1_frame.grid(row=3, column=0)
    new_V1_frame.grid_propagate(False)
    new_V1_frame.columnconfigure(0, weight=1)
    
    new_leadV1_frame = ttk.LabelFrame(new_V1_frame, 
                                 height=new_frame_size_height, 
                                 width=new_frame_size_width)
    new_leadV1_frame.grid(row=0, column=0, sticky="w")

    space_frame = ttk.LabelFrame(new_V1_frame, 
                            width=new_hr_width_side, 
                            height=100)
    space_frame.grid(row=0, column=1, sticky="e")
    
    # Bottom frame for ECG (Pulse, awRR, TPERI)
    new_rate_frames = ttk.LabelFrame(new_ecg_frame, 
                                height=new_bot_frame_size_h, 
                                width=new_bot_frame_size_w)
    new_rate_frames.grid(row=4, column=0, columnspan=1)

    # Bottom frame for Pulse, awRR, TPERI
    new_pulse_frame = tk.Frame(new_rate_frames, 
                               width=new_bot_frame_size_w, 
                               height=new_bot_frame_size_h)
    new_pulse_frame.grid(row=0, column=0)
    new_pulse_canvas = tk.Canvas(new_pulse_frame, 
                                 highlightthickness=0, 
                                 bd=0, 
                                 bg="black", 
                                 height=new_bot_frame_size_h, 
                                 width=new_bot_frame_size_w)
    new_pulse_canvas.grid(row=0, column=0)
    new_pulse = new_pulse_canvas.create_text(20, 20, 
                                             text="Pulse", 
                                             font=('Arial', 15), 
                                             fill="#0fbef2")
    new_pulse_result = new_pulse_canvas.create_text(70, 70, 
                                                    text="--", 
                                                    font=('Arial', 50), 
                                                    fill="#0fbef2")

    new_awRR_frame = tk.Frame(new_rate_frames, 
                              width=new_bot_frame_size_w, 
                              height=new_bot_frame_size_h)
    new_awRR_frame.grid(row=0, column=1)
    new_awRR_canvas = tk.Canvas(new_awRR_frame, 
                                highlightthickness=0, 
                                bd=0, 
                                bg="black", 
                                width=new_bot_frame_size_w, 
                                height=new_bot_frame_size_h)
    new_awRR_canvas.grid(row=0, column=0)
    new_awRR = new_awRR_canvas.create_text(20, 20, 
                                           text="awRR", 
                                           font=('Arial', 15), 
                                           fill="white")
    new_awRR_result = new_awRR_canvas.create_text(70, 70, 
                                                  text="--", 
                                                  font=('Arial', 50), 
                                                  fill="white")

    new_Tperi_frame = tk.Frame(new_rate_frames, 
                               width=new_bot_frame_size_w, 
                               height=new_bot_frame_size_h)
    new_Tperi_frame.grid(row=0, column=2)
    new_Tperi_canvas = tk.Canvas(new_Tperi_frame, 
                                 highlightthickness=0, 
                                 bd=0,  
                                 width=new_bot_frame_size_w, 
                                 height=new_bot_frame_size_h)
    new_Tperi_canvas.grid(row=0, column=0)
    new_Tperi = new_Tperi_canvas.create_text(20, 20, 
                                             text="Tperi", 
                                             font=('Arial', 15), 
                                             fill="#84f91c")
    new_Tperi_result = new_Tperi_canvas.create_text(70, 70, 
                                                    text="--", 
                                                    font=('Arial', 50), 
                                                    fill="#84f91c")


    widgets = {
    "leadII_label": new_leadII_label,
    "leadII_frame": leadII_frame,
    "leadV1_frame": new_leadV1_frame,
    "II_frame": new_II_frame,
    "HR_frame": new_HR_frame,
    "HR_canvas": new_HR_canvas,
    "Heart_rate": new_Heart_rate,
    "d_canvas": new_d_canvas,
    "dot": new_dot,
    "rate": new_rate,
    "rate_frames": rate_frames,
    "pulse_frame": new_pulse_frame,
    "pulse_canvas": new_pulse_canvas,
    "pulse": new_pulse,
    "pulse_result": new_pulse_result,
    "awRR_frame": new_awRR_frame,
    "awRR_canvas": new_awRR_canvas,
    "awRR": new_awRR,
    "awRR_result": new_awRR_result,
    "Tperi_frame": new_Tperi_frame,
    "Tperi_canvas": new_Tperi_canvas,
    "Tperi": new_Tperi,
    "Tperi_result": new_Tperi_result,
}   
    return widgets

def ecg_start():
    if (combo.get() == "Heart Rhytms" and len(y) == 0):
        tk.messagebox.showerror("Error", "Please Select Disease")
        return
    screen = tk.Toplevel()
    screen.geometry("800x675")
    screen.title(combo.get())
    dict_widgets = set_new_window(screen)
    dict_widgets['window'] = screen
    
    # turn off start
    if (combo.get() != "Heart Rhytms" or len(y) != 0):
        btn_start.config(state="disable")

    # disease list need to update since chart shouldnt be next to the ecg signal 
    ecg_list = [["Atrial Flutter", 0],
                ["VF", 1],
                ["Atrial Tachycardia",2],
                ["Sinus Arrhythmia",1],
                ["A Fib",0],
                ["Normal Rhythm", 2],
                ["VT", 6],
                ["Multifocal Atrial Tachycardia",7],
                ["VFib",1], 
                ["Bradycardia",4], 
                ["Tachycardia", 5]]
    ecg_num = 2 #init to normal rhythm
    
    for i in range(0,len(ecg_list)):
        if ( combo.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]
    
    ecg_frame.config(text=combo.get())
    animation(ecg_num,widgets, False)
    animation(ecg_num,dict_widgets, True)
    btn_start.config(state="normal")

print_x = []
print_y = []
t = np.linspace(-2,2,1200)
y = normal.normal()
# inverse
t2 = np.linspace(-2,2,1200)
inverse_y2 = -y
update_requested = False
def animation(ecg_num,widgets, copy):
    global t, y, t2, inverse_y2,print_y, print_x, update_requested
    if not copy:
        print_y = []

    update_requested = False
    if not copy:
        if(combo.get() == 'Normal Rhythm'):
            t = np.linspace(-2,2,1200)
            y = normal.normal()
        elif (combo.get() == 'Sinus Arrhythmia'):
            t = np.linspace(-2,2,1200)
            y = normal.sinus_arrythmia()
        elif (combo.get() == 'Bradycardia'):
            t = np.linspace(-2,2,1200)
            y = normal.sinus_brady()
        elif (combo.get() == 'Tachycardia'):
            t = np.linspace(-2,2,1200)
            y = normal.sinus_tachy()
        elif (combo.get() == 'VFib'):
            t = np.linspace(-2,2,1200)
            y = normal.vfib()
        else:
            t = np.linspace(-2,2,1200)
            #y = normal.update_ecg()
         
    get_new_parameters(parameters)
    if not copy:
        print_y.extend(y)
    
    fig_x = 6
    fig_y = 2


    # create figure 
    fig1, axis = plt.subplots(figsize=(fig_x,fig_y),facecolor="#2B3F51")                   # background of fig black
    plt.axis("off")

    # previous
    t_p = np.linspace(-2,2,1200)
    x = (1/1000)*t_p + 0.9
    y_p = np.linspace(0.9,0.9,1200)

    fig2, axis2 = plt.subplots(figsize=(fig_x,fig_y),facecolor="#2B3F51")
    plt.axis("off")

    # function for Funcanimation 
    def update(frame):
        global y, inverse_y2, print_y, update_requested
        nonlocal hr, pulse_
        
        if frame == len(t) - 1 and not update_requested:
            if len(y) > 1200:
                y = y[1200:]
            if not copy:
                print_y.extend(y)
        if frame == len(t) - 1 and update_requested:
            y = normal.update_ecg()
            inverse_y2 = -y
            if (HR_checker.get() == 1):
                hr = hr_entry.get()
            else:
                hr = normal.get_HR()
            widgets['HR_canvas'].after(100,update_rate)
            if not copy:
                print_y.extend(y)
            update_requested = False 
        # update the new points after each frame)
        '''if (pulse_checker.get() == 1):
            pulse_ = pulse_entry.get()
        else:
            pulse_ = 0
        widgets['pulse_canvas'].after(100,update_rate)'''

        animated_plot.set_data(t[:frame], y[:frame])
        #pulse_sig.set_data([x[frame]], [0])
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
    canvas = FigureCanvasTkAgg(fig1, widgets['II_frame'])
    canvas2 = FigureCanvasTkAgg(fig2, widgets['leadV1_frame'])
    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(side="left")
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left")

    
    # dot blicking
    def blicking():
        cur_color = widgets['d_canvas'].itemcget(dot, 'fill')
        new_color = 'red' if cur_color == '#2B3F51' else '#2B3F51'
        widgets['d_canvas'].itemconfig(dot, fill=new_color)
        widgets['d_canvas'].after(1000,blicking)

    blicking()

    def update_rate():
        widgets['HR_canvas'].itemconfig(widgets['rate'], text=str(hr))
        widgets['pulse_canvas'].itemconfig(widgets['pulse_result'], text=str(pulse_))
        widgets['awRR_canvas'].itemconfig(widgets['awRR_result'], text=str(awRR_))
        widgets['Tperi_canvas'].itemconfig(widgets['Tperi_result'], text=str(Tp))

    # check for manual input 
    if (all_checker.get() == 1):
        hr = hr_entry.get()
        pulse_ = pulse_entry.get()
        awRR_ = awRR_entry.get()
        Tp = TP_entry.get()
    else:
        if (HR_checker.get() == 1):
            hr = hr_entry.get()
        else:
            hr = normal.get_HR()
        if (pulse_checker.get()==1):
            pulse_ = pulse_entry.get()
        else:
            pulse_ = 0
        if ( awRR_checker.get() == 1):
            awRR_ = awRR_entry.get()
        else:
            awRR_ = 0

        if (TP_checker.get() == 1):
            Tp = TP_entry.get()
        else:
            Tp = 0
    

    widgets['HR_canvas'].after(11000,update_rate)

    # buttom frame
    def on_click_exit():
        global print_y, print_x
        combo.set(" Heart Rhythms ")
        print_x = np.linspace(0, 4*(len(print_y)/1200), len(print_y))
        btn_start.config(state="normal")
        #if not copy:
        #    print_onECG_change()
        if 'window' in widgets:
            widgets['window'].destroy()
        else:
            animate.event_source.stop()  
            animate2.event_source.stop()
            canvas.get_tk_widget().destroy()
            canvas2.get_tk_widget().destroy()
            button_exit.destroy()
            widgets['HR_canvas'].itemconfig(widgets['rate'], text="")
            widgets['pulse_canvas'].itemconfig(widgets['pulse_result'], text="")
            widgets['awRR_canvas'].itemconfig(widgets['awRR_result'], text="")
            widgets['Tperi_canvas'].itemconfig(widgets['Tperi_result'], text="")

        
            
        #ecg_signal_frame.destroy()
    if not copy:
        button_exit_frame= ttk.Frame(rate_frames)
        button_exit_frame.grid(row = 0, column = 4)
        button_exit = ttk.Button(button_exit_frame, text="Exit", style="S.TButton", command=on_click_exit)
        button_exit.grid(row = 0, column = 0)
# resize 
def resize(win_frame,rows, cols):
    for i in range(rows):
        win_frame.rowconfigure(i, weight= 1)
    for j in range(cols):
        win_frame.columnconfigure(j, weight= 1)

# **************** Print Frame Functions ********************
def print_update(val):
    start = slider.val  
    end = start + print_window_size  # Set the end based on window size
    print_ax.set_xlim([start, end])  # Adjust x-axis limits
    print_fig.canvas.draw_idle()
    
def print_onECG_change():
    global print_y, print_x
    print_ax.clear()
    print_ax.plot(print_x, print_y)
    print_fig.canvas.draw_idle()

def print_onPrint_click():
    global print_y, print_x
    start_val = (entry_from.get())
    end_val = (entry_to.get())
    if not start_val or not end_val:
        tk.messagebox.showerror("Error", "Please enter start and end values")
        return
    if len(print_x) == 0 or len(print_y) == 0:
        tk.messagebox.showerror("Error", "No data to print")
        return
    start = int(start_val)
    end = int(end_val)
    
    print_x_np = np.array(print_x)  
    print_y_np = np.array(print_y)
    
    print_list_y = print_y_np[(print_x_np >= start) & (print_x_np <= end)]
    end = end - start
    print_plot.plot_ecg(print_list_y, end, filename_entry.get())

# **************** Simulator Frame Functions ********************

def save_to_csv(filename='ecg_save', folder_path='./simulations'):
    global print_x, print_y
    if len(print_x) == 0 or len(print_y) == 0:
        tk.messagebox.showerror("Error", "No data to save")
        return
    if filename_entry.get():
        filename = filename_entry.get()
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

def sim_from_to_time():
    global y, sim_time_options
    rhythm = (sim_entry_from.get()).lower()
    if not sim_entry_time.get().isdigit():
        tk.messagebox.showerror("Error", "Please enter valid time")
        return
        
    time_val = int(sim_entry_time.get())

    if not rhythm or not time_val:
        tk.messagebox.showerror("Error", "Please enter rhythm and time")
        return
    if sim_time_options.count(rhythm) == 0:
        tk.messagebox.showerror("Error", "Invalid rhythm entered current or valid rhythm")
        return

    
    goal = []
    if rhythm == "sinus arrhythmia":
        goal = normal.sinus_arrythmia()
    elif rhythm == "bradycardia":
        goal = normal.sinus_brady()
    elif rhythm == "tachycardia":
        goal = normal.sinus_tachy()
    elif rhythm == "vfib":
        goal = normal.vfib()
    elif rhythm == "VT":
        goal = normal.VT()
    elif rhythm == "atrial tachycardia":
        goal = normal.atrial_tachy()
    elif rhythm == "current":
        goal = normal.update_ecg()

    y = normal.normal()

    intervals = (time_val*60) // 12  
    extended_y = list(normal.normal())
    resid = []
    resid_list = []
    for i in range(len(y)):
        resid.append((goal[i] - y[i])/intervals)
    resid_list = resid
    for i in range(intervals):
        extended_y.extend(resid_list+y)
        resid_list = [x+y for x,y in zip(resid_list,resid)]

    y = extended_y

def delete_csv_file():
    filename = clicked_sim_menu.get()
    if filename == '':
        tk.messagebox.showerror("Error", "Invalid file")
    if os.path.exists('./simulations/' + filename + '.csv'):
        os.remove('./simulations/' + filename + '.csv')
    else:
        tk.messagebox.showerror("Error", "Could not delte file")

########## main window ##########
#root = ttk.Window(themename="superhero")                       # create window
window = tk.Tk()
style = ttk.Style(theme="superhero")                            # style with B.S.
window.title("Electrocardiogram Simulator")                       # title for window
window.attributes("-fullscreen", True)                            # open fullscreen
window.protocol("WM_DELETE_WINDOW", 
                lambda: (window.quit(), 
                 window.destroy()))

ecg_title = ttk.Label(
                    window, 
                    text = "ECG Simulator", 
                    font=('Time', 30))
ecg_title.grid(row = 0, pady = 5)                              # main title
window.columnconfigure(0, weight= 1)
window.rowconfigure(1, weight=1)

screen_width = window.winfo_screenwidth()                         # window sizes
screen_height = window.winfo_screenheight()
dash_w = int(screen_width * 0.20)
dash_h = int(screen_height - 30)
main_w = int(screen_width * 0.80)
main_h = int(screen_height - 30)
par_w = (main_w * 0.40)
par_h = (main_h * 0.70)
content_w = (main_w * 0.60)
content_h = (main_h * 0.70)
disease_w = (main_w * 0.40)
disease_h = (main_h * 0.30)

####### MAIN SIDE FRAMES ########
master_frame = ttk.Frame(window,
                   width= screen_width,
                   height= screen_height)                       # frame under title
master_frame.grid(row = 1)
master_frame.columnconfigure(1, weight=2)
master_frame.rowconfigure(0, weight=1)
master_frame.rowconfigure(1,weight=1)

main_frame = ttk.LabelFrame(master_frame,
                       width = main_w,
                       height= main_h)                          # main side
main_frame.grid(row = 0, column=1)
resize(main_frame, 2,2)

parameter_frame = ttk.LabelFrame(main_frame,
                                 text = "Wave Parameters",
                                 width= par_w,
                                 height= par_h)                 # parameter frame
parameter_frame.grid(row = 0, column=0)                         
parameter_frame.grid_propagate(False)
resize(parameter_frame, 14, 3)

content_area = ttk.Frame(main_frame,
                              width = content_w,
                              height = content_h)               # content frame
content_area.grid(row = 0, column = 1)                         
content_area.grid_propagate(False)
resize(content_area, 2, 2)
disease_frame = ttk.LabelFrame(main_frame,
                               text= "Disease Selection",
                               width= disease_w,
                               height= disease_h)               # disease frame
disease_frame.grid(row =1 , column= 0, rowspan=2)

manual_frame = ttk.LabelFrame(main_frame,
                              text= "Manual Inputs",
                              width= disease_w,
                              height= disease_h)                # manual frame
manual_frame.grid(row = 1, column= 1, rowspan=2)
manual_frame.grid_propagate(False)



############## DASH BOARD ################
dash_frame = ttk.LabelFrame(master_frame, 
                       width = dash_w, 
                       height= dash_h)
dash_frame.grid(row = 0, column = 0)                            # dash side
dash_frame.grid_propagate(False)
# Button to start signal
btn_start = ttk.Button(dash_frame , 
                       text = " Start " ,
                       style='S.TButton',
                       command= ecg_start)                       # start button
btn_x_start = int((dash_w/3))
btn_start.config(width= 7)
btn_start.grid(row = 2, column=0)
#btn_start.place(x= btn_x_start,y = 500)

# Button to set params
btn_update = ttk.Button(dash_frame, 
                        text="Update", 
                        style="S.TButton",                  
                        command=on_click_update)               # update button
btn_x_update = int((dash_w/3))
btn_update.config(width= 7)
btn_update.grid(row = 3, column=0)
#place(x= btn_x_update,y = 550)

# close window
btn_quit = ttk.Button(dash_frame,
                      text="Exit",
                      style="Q.TButton", 
                      command=quit)                             # exit button
btn_x_quit = int((dash_w/3))
btn_quit.config(width= 7)
btn_quit.grid(row= 4, column= 0)
#place(x= btn_x_quit,y=600)

icon = ttk.PhotoImage(file="ecg.png")                           # get icon
icon_label = ttk.Label(dash_frame, image=icon)                  # place icon in gui
icon_label.grid(row = 0, column= 0)               # one column for row


title_dash = ttk.Frame(dash_frame,
                       width= dash_w,
                       height = (dash_h * 0.30))                # frame for switch
title_dash.grid(row = 1, column=0)                               # options 
title_dash.columnconfigure(0, weight= 1)

buttons = [
    ("Electrocardiogram", lambda: 
     switch_frame("Electrocardiogram")),
    ("Print", lambda: switch_frame("Print")),
    ("Simulator", lambda: switch_frame("Simulator"))
]                                                               # buttons for options
btnum = 0
for text, cmd in buttons:
    btn = ttk.Button(title_dash, 
                     text=text, 
                     command=cmd, 
                     width=20,
                     style="Custom.TButton")
    btn.grid(row= btnum, column=0, padx=30)
    btnum += 1
    title_dash.grid_propagate(False)
dash_frame.columnconfigure(0, weight= 1)
dash_frame.rowconfigure(4, weight=1)

ecg_frame = ttk.LabelFrame(content_area,
                           text="LIVE ECG",
                           width= content_w,
                           height=content_h)                    # ecg frame 
print_frame = ttk.LabelFrame(content_area,
                             text="ECG PRINT",
                             width= content_w,
                             height=content_h)                  # print frame
sim_frame = ttk.LabelFrame(content_area,
                           text="Simulation",
                           width= content_w,
                           height=content_h)                    # sim frame

frames = {                                                      # frames in content
    "Electrocardiogram": ecg_frame,
    "Print": print_frame,
    "Simulator": sim_frame
}

################ PARAMETER FRAME ##################
# parameter container
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

#################### ECG SIGNAL ###############
#resize(ecg_frame, 5, 2)
ecg_frame.grid()
ecg_frame.grid_propagate(False)

leadII_label = ttk.Label(ecg_frame, 
                         text="Lead II", 
                         font=("Time", 15),
                         foreground="#84f91c")                             # leadII label
leadII_label.grid(row = 0, column=0, sticky="w", pady=2)

leadII_frame= ttk.Frame(ecg_frame,
                        width= (content_w),
                        height= (content_h*0.3))
leadII_frame.grid(row =1, column=0, columnspan=1, sticky="w")             # main frame for both
leadII_frame.grid_propagate(False)                                        # live II and HR

II_frame = ttk.Frame(leadII_frame,
                    width= (content_w*0.85),
                    height = (content_h * 0.3))                           # II 
II_frame.grid(row = 0, column=0)
HR_frame= ttk.Frame(leadII_frame,
                   width=(content_w*0.15),
                   height=(content_h*0.30))                            # frame for heartrate  
HR_frame.grid(row= 0, column=1, sticky="e")

HR_canvas = tk.Canvas(HR_frame,
                      highlightthickness=0, 
                      bg="#84f91c",
                      width = 100,                                    # Canvas for HR to display numbers
                      height=100)
HR_canvas.grid(row = 0, column=2)
Heart_rate = HR_canvas.create_text(10,
                                   10, 
                                   text="HR", 
                                   font=('Arial', 15), 
                                   fill= "red")                       # label for heartrate

d_canvas = tk.Canvas(HR_frame, 
                     bg="#84f91c",
                     bd=0,
                     highlightcolor="#84f91c",                        # canvas to draw the red circle
                     highlightthickness=0, 
                     width =20, 
                     height=20)
d_canvas.grid(row=0, column=0)
dot = d_canvas.create_oval(2, 2, 15, 15, 
                           fill='red', 
                           outline= "")                               # create the dot
rate = HR_canvas.create_text(50, 50, 
                             text="--", 
                             font=('Arial', 40),
                             fill= "#99f20f")                         # output the HR
leadII_frame.rowconfigure(0, weight=1)
leadII_frame.rowconfigure(1, weight=1)
leadII_frame.columnconfigure(1,weight=5)

#####
leadV1_label = ttk.Label(ecg_frame, 
                            text="V1",
                             font=("Time", 15), 
                             foreground="#84f91c")
leadV1_label.grid(row=2, column=0, sticky="w")
V1_frame = ttk.Frame(ecg_frame, 
                        height= (content_h*0.3), 
                        width= content_w)
V1_frame.grid_propagate(False)
V1_frame.grid(row=3, column=0)
V1_frame.columnconfigure(0, weight=1)
V1_frame.rowconfigure(0, weight = 1)
leadV1_frame = ttk.Frame(V1_frame, 
                            height=(content_h*0.3), 
                            width=content_w)
leadV1_frame.grid(row=0, column=0, sticky="w")

space_frame = ttk.Frame(V1_frame, 
                            width= (content_w*0.15), 
                            height= (content_h*0.30))
space_frame.grid(row=0, column=1, sticky="e")


rate_frames = ttk.Frame(ecg_frame,
                        width= content_w,
                        height= content_h * 0.3)                     # rate_frame
rate_frames.grid(row = 4, column = 0, columnspan=1)                  # pulse, awRR, tperi
rate_frames.grid_propagate(False)

pulse_frame = ttk.Frame(rate_frames,
                        width= (content_w * 0.25),
                        height= content_h * 0.3)                   # pulse frame
pulse_frame.grid(row=0, column=0)
pulse_canvas = tk.Canvas(pulse_frame, 
                         highlightthickness=0, 
                         bd= 0,                                    # establish canvas to draw pulse
                         height= (content_h * 0.4), 
                         width= (content_w * 0.25))                           
pulse_canvas.grid(row = 0, column=0)
pulse = pulse_canvas.create_text(20,20, 
                                 text="Pulse", 
                                 font=('Arial', 15), 
                                 fill= "#0fbef2")                  # create pulse label
pulse_result = pulse_canvas.create_text(70,70, 
                                        text="--",
                                        font=('Arial', 50),
                                        fill= "#0fbef2" )         # create "--" waiting for input

awRR_frame = tk.Frame(rate_frames,
                      height = (content_h * 0.4), 
                      width = (content_w * 0.25))
awRR_frame.grid(row = 0, column= 1)
awRR_canvas = tk.Canvas(awRR_frame, 
                        highlightthickness=0, 
                        bd= 0,                                   # establish canvas to draw awRR
                        height= (content_h * 0.4), 
                        width= (content_w * 0.25))                           
awRR_canvas.grid(row = 0, column= 0)                                                            
awRR = awRR_canvas.create_text(20,20, 
                               text="awRR", 
                               font=('Arial', 15), 
                               fill= "white")                    # create awRR label
awRR_result = awRR_canvas.create_text(70,70, 
                                      text="--", 
                                      font=('Arial', 50), 
                                      fill= "white" )            # create "--" waiting for input

Tperi_frame = tk.Frame(rate_frames,
                       width = (content_w * 0.25), 
                       height = (content_h * 0.4))
Tperi_frame.grid(row = 0, column= 2)
Tperi_canvas = tk.Canvas(Tperi_frame, 
                         highlightthickness=0, 
                         bd= 0,                                 # establish canvas to draw pulse
                         width=(content_w * 0.25), 
                         height= (content_h * 0.4))                           
Tperi_canvas.grid(row = 0, column= 0)                                                          
Tperi = Tperi_canvas.create_text(20,20, 
                                 text="Tperi", 
                                 font=('Arial', 15), 
                                 fill= "#84f91c")                # create pulse label
Tperi_result = Tperi_canvas.create_text(70,70, 
                                        text="--", 
                                        font=('Arial', 50), 
                                        fill= "#84f91c" )         # create "--" waiting for input
resize(rate_frames,1,3)
ecg_frame.grid_columnconfigure(0,weight=1)
#ecg_frame.grid_rowconfigure(0, weight=1)
ecg_frame.grid_rowconfigure(1, weight=3)
#ecg_frame.grid_rowconfigure(2, weight=1)
ecg_frame.grid_rowconfigure(3, weight=3)
ecg_frame.grid_rowconfigure(4, weight=3)

############ DISEASE FRAME #############
disease_frame.grid_propagate(False)
def search(event):                                                        # search in combo
    value = event.widget.get()
    if (value == ''):
        combo['values'] = options
    else:
        name = []
        for option in options:
            if(value.lower() in option.lower()):
                name.append(option)

        combo["values"] = name

                                                                    
options = [                                                       # Options for disease 
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
combo = ttk.Combobox( disease_frame , value= options )          # combo for disease
combo.set("Heart Rhytms")
combo.bind("<KeyRelease>", search)
combo.grid(row= 0, column= 0)
combo.grid_propagate(False)
#place(x = 30, y = 50)

resize(disease_frame, 1, 1)

############ MANUAL INPUTS ##############
def check_inputs():
    if (all_checker.get() == 1):
        hr_entry.config(state="normal")
        pulse_entry.config(state="normal")
        awRR_entry.config(state="normal")
        TP_entry.config(state="normal")
    else:
        if HR_checker.get() == 1:
            hr_entry.config(state="normal")
        if pulse_checker.get() ==1:
            pulse_entry.config(state="normal")
        if awRR_checker.get() ==1:
            awRR_entry.config(state="normal")
        if TP_checker.get() ==1:
            TP_entry.config(state="normal")

HR_checker = tk.IntVar()
HR_checkbutton= ttk.Checkbutton(manual_frame, 
                                text="HR  ", 
                                variable=HR_checker,
                                onvalue= 1, 
                                offvalue= 0, 
                                command= check_inputs)
HR_checkbutton.grid(row = 0, column= 0)
hr_entry = tk.Entry(manual_frame, state="disable", width= 10)
hr_entry.grid(row = 0 , column= 1)

pulse_checker = tk.IntVar()
pulse_checkbutton= ttk.Checkbutton(manual_frame, 
                                text="Pulse", 
                                variable=pulse_checker,
                                onvalue= 1, 
                                offvalue= 0, 
                                command= check_inputs)
pulse_checkbutton.grid(row = 1, column= 0)
pulse_entry = tk.Entry(manual_frame, state="disable", width= 10)
pulse_entry.grid(row = 1, column= 1)

awRR_checker = tk.IntVar()
awRR_checkbutton= ttk.Checkbutton(manual_frame, 
                                text="awRR", 
                                variable=awRR_checker,
                                onvalue= 1, 
                                offvalue= 0, 
                                command= check_inputs)
awRR_checkbutton.grid(row = 2, column= 0)
awRR_entry = tk.Entry(manual_frame, state="disable", width= 10)
awRR_entry.grid(row = 2, column= 1)

TP_checker = tk.IntVar()
TP_checkbutton= ttk.Checkbutton(manual_frame, 
                                text="Tperi", 
                                variable=TP_checker,
                                onvalue= 1, 
                                offvalue= 0, 
                                command= check_inputs)
TP_checkbutton.grid(row = 3, column= 0)
TP_entry = tk.Entry(manual_frame, state="disable", width= 10)
TP_entry.grid(row = 3, column= 1)

all_checker = tk.IntVar()
all_checkbutton= ttk.Checkbutton(manual_frame, 
                                text="Select All", 
                                variable=all_checker,
                                onvalue= 1, 
                                offvalue= 0, 
                                command= check_inputs)
all_checkbutton.grid(row = 4, column= 0, pady= 10,sticky="n")
manual_frame.columnconfigure(0, weight=1)
manual_frame.columnconfigure(1, weight=1)
manual_frame.rowconfigure(4, weight=1)

#***************************PRINT FRAME********************************
print_main_frame = ttk.Frame(print_frame)
print_main_frame.grid(row = 0)

print_main_frame.columnconfigure(0, weight=1)
print_main_frame.rowconfigure(0, weight=1)
print_frame = ttk.LabelFrame(print_frame, borderwidth=10, text="Editor")
print_frame.grid(row = 1)

print_frame.columnconfigure(1, weight= 1)

#plot frame
print_fig, print_ax = plt.subplots(figsize=(4, 2))
print_ax.plot(print_x, print_y)
print_window_size = 5

print_ax.set_xlim([0, print_window_size])
canvas = FigureCanvasTkAgg(print_fig, master=print_frame)
canvas.get_tk_widget().grid(row = 1)

slider_ax = print_fig.add_axes([0.25, 0.02, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(slider_ax, 'Time (s)', 0, 720 - print_window_size, valinit=0)

slider.on_changed(print_update)

label_range = ttk.Label(print_frame, text="Range")
label_range.grid(row= 2, column=0)

input_frame = ttk.Frame(print_frame)
input_frame.grid(row = 3, column=0)
resize(input_frame, 1, 4)

label_from = ttk.Label(input_frame, text="From:")
label_from.grid(row = 0, column=0)
entry_from = ttk.Entry(input_frame, width=10)
entry_from.grid(row = 0, column=1)


label_to = ttk.Label(input_frame, text="To:")
label_to.grid(row =0, column= 2)
entry_to = ttk.Entry(input_frame)
entry_to.grid(row = 0, column= 3)

label_filename = ttk.Label(print_frame, text="Filename:")
label_filename.grid(row = 4, column=0)  
filename_entry = ttk.Entry(print_frame, width=30) 
filename_entry.grid(row = 5, column= 0)

btn_print_frame= ttk.Frame(print_frame)
btn_print_frame.grid(row= 6, column= 0)
submit_button = ttk.Button(btn_print_frame, text="Print", command=print_onPrint_click)
submit_button.grid(row = 0, column= 0, padx= 5)
save_button = ttk.Button(btn_print_frame, text="Save", command=save_to_csv)
save_button.grid(row = 0, column=1, padx= 5)
btn_print_frame.columnconfigure(0, weight=1)
btn_print_frame.columnconfigure(1, weight=1)

resize(print_frame, 7, 1)
#***************************SIMULATOR FRAME********************************
sim_main_frame = ttk.Frame(sim_frame)
sim_main_frame.grid(row = 0, column=0) 

sim_main_label = ttk.Label(sim_main_frame, text="Saved ECG's", font=('Time', 30), foreground="white")
sim_main_label.grid(row = 0, column=0) 

simulator_frame = ttk.LabelFrame(sim_frame, borderwidth=10, text="Simulations", height=content_h * 0.6, width=content_w*0.7)
simulator_frame.grid(row = 1, column=0)
simulator_frame.grid_propagate(False)

def get_file_names(folder_path):
    return [file.stem for file in Path(folder_path).iterdir() if file.is_file()]

options_sim = get_file_names('./simulations')
clicked_sim_menu = tk.StringVar()
clicked_sim_menu.set( " Rhythms " ) 
save_sim_drop = ttk.OptionMenu( simulator_frame , clicked_sim_menu , *options_sim, command=load_saved_simulation)
save_sim_drop.grid(row= 3, column=0)

sim_sub_frame = ttk.Frame(sim_frame)
sim_sub_frame.grid(row = 2, column=0) 
sim_sub_label = ttk.Label(sim_sub_frame, text="Create Simulation", font=('Time', 30), foreground="white")
sim_sub_label.grid(row = 0, column=0)
simulator_subframe = ttk.LabelFrame(sim_frame, borderwidth=10, text="Simulations", height=500, width=500)
simulator_subframe.grid(row = 3, column=0)

sim_label_from = ttk.Label(simulator_subframe, text="Rhythm:")
sim_label_from.grid(row=0, column=0)
sim_entry_from = ttk.Entry(simulator_subframe, width=10)
sim_entry_from.grid(row = 0, column=1)

sim_label_time = ttk.Label(simulator_subframe, text="Time:")
sim_label_time.grid(row = 0, column=2)
sim_entry_time = ttk.Entry(simulator_subframe)
sim_entry_time.grid(row = 0, column=3)
sim_time_options = [option.lower() for option in options]
sim_time_options.append("current")
simulator_subframe.columnconfigure(0, weight= 1)
simulator_subframe.columnconfigure(1, weight= 3)
simulator_subframe.columnconfigure(2, weight= 1)
simulator_subframe.columnconfigure(3, weight= 3)

sim_submit_button = ttk.Button(simulator_subframe, text="Submit", command=sim_from_to_time)
sim_submit_button.grid(row= 2, column= 0)
       
sim_delete_button = ttk.Button(simulator_subframe, text="Delete", command=delete_csv_file)
sim_delete_button.grid(row = 2 , column = 1)


resize(sim_sub_frame, 3, 4)
resize(sim_main_frame, 2, 4)

resize(sim_frame, 3, 1)
#clicked_sim_menu.trace_add("write", load_saved_simulation)

#***************************OTHER FRAME********************************
widgets = {
    "leadII_label": leadII_label,
    "leadII_frame": leadII_frame,
    "leadV1_frame": leadV1_frame,
    "II_frame": II_frame,
    "HR_frame": HR_frame,
    "HR_canvas": HR_canvas,
    "Heart_rate": Heart_rate,
    "d_canvas": d_canvas,
    "dot": dot,
    "rate": rate,
    "pulse_frame": pulse_frame,
    "pulse_canvas": pulse_canvas,
    "pulse": pulse,
    "pulse_result": pulse_result,
    "awRR_frame": awRR_frame,
    "awRR_canvas": awRR_canvas,
    "awRR": awRR,
    "awRR_result": awRR_result,
    "Tperi_frame": Tperi_frame,
    "Tperi_canvas": Tperi_canvas,
    "Tperi": Tperi,
    "Tperi_result": Tperi_result,
}


window.mainloop()                                                 # run the gui
