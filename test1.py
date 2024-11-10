from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
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
    
print_x = []
print_y = []
t = np.linspace(-2,2,1200)
y = normal.normal()

def animation(window,ecg_num):
    global t, y, print_y, print_x
    print_y = []
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
    print_y.extend(y)
    # create figure 
    fig1, axis = plt.subplots(figsize=(7,2),facecolor="black")                   # background of fig black
    fig2, axis2 = plt.subplots(figsize=(7,2),facecolor="black")
    
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

        
        animated_plot.set_data(t[:frame], y[:frame])
        
        
        return animated_plot
    axis.set_xlim([-2,2])                                # set the limits of time for x
    axis.set_ylim([0,2.5])                                         # Set limit for amplitude for y 
    plt.xticks(np.arange(min(t), max(t)+1, 0.25))
    plt.yticks(np.arange(min(y)-1,max(y), 0.25)) 
    animated_plot, = axis.plot([],[],color="#84f91c")
    axis.set_facecolor("black")
                                   
    animate = FuncAnimation(fig= fig1, func= update,frames=len(t),interval=10, repeat="False")
    canvas = FigureCanvasTkAgg(fig1, btm2_frame)
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
        nonlocal update_requested
        update_requested = True
        
        

    # buttom frame
    def on_click_exit():
        global print_y, print_x
        clicked.set(" Heart Rhythms ")
        print_x = np.linspace(0, 4*(len(print_y)/1200), len(print_y))
        print_onECG_change()
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

  
def switch_frame(frame):
    for f in frames.values():
        f.pack_forget()  
    frames[frame].pack(fill="both", expand=True)  

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
    global print_x, print_y, options_sim
    
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
    options_sim = get_file_names('./simulations')



def load_saved_simulation(*args):
    global print_x, print_y, y, t
    x_values = []
    y_values = []
    if clicked_sim_menu.get() == " Simulations ":  
        return
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
    

# **************** CREATE MAIN WINDOW ********************
root = ttk.Window(themename="superhero")
root.title("ECG Simulator")
root.geometry("1000x800")

sidebar = ttk.Frame(root, width= 200)
sidebar.pack(side="left", fill="y")

icon = tk.PhotoImage(file="ecg.png")  

icon_label = tk.Label(sidebar, image=icon)  
icon_label.pack(pady=50)  


content_area = ttk.Frame(root)
content_area.pack(side="right", fill="both", expand=True)

style = ttk.Style()
style.configure("Custom.TButton",
                background="darkblue",
                foreground="white", 
                font=('Helvetica', 12, 'bold'))

buttons = [
    ("Electrocardiogram", lambda: switch_frame("Electrocardiogram")),
    ("Print", lambda: switch_frame("Print")),
    ("Simulator", lambda: switch_frame("Simulator"))
]

for text, cmd in buttons:
    btn = ttk.Button(sidebar, text=text, command=cmd, width=20, style="Custom.TButton")
    btn.pack(fill="x", padx=10,ipady=20)

ecg_frame = ttk.Frame(content_area)
print_frame = ttk.Frame(content_area)
simulator_frame = ttk.Frame(content_area)



frames = {
    "Electrocardiogram": ecg_frame,
    "Print": print_frame,
    "Simulator": simulator_frame
}

ecg_frame.pack(fill="both", expand=True)

# ****************************ECG FRAME********************************
main_frame = Frame(ecg_frame, highlightbackground="white", highlightthickness=2)
main_frame.pack(padx=10, pady=5) 

main_label = Label(main_frame, text="Electrocardiogram Simulator", font=('Time', 30), foreground="white")
main_label.pack(padx=10)  

disease_frame = ttk.LabelFrame(ecg_frame, borderwidth=10, text="DISEASES", height=300, width=300)
disease_frame.pack(padx=10, pady=10, side="right", fill="y") 

parameter_frame = ttk.LabelFrame(ecg_frame, borderwidth=10, text="PARAMETERS",takefocus="1", height=500, width=500)
parameter_frame.pack(padx=10, pady=10, side="right", fill="y")

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

clicked = StringVar()  
clicked.set( " Heart Rhytms " ) 
drop = OptionMenu( disease_frame , clicked , *options )
drop.place(x = 60, y = 50)

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

btn_start = ttk.Button( disease_frame , text = " Start " ,bootstyle='danger', command = newWindow)
btn_start.place(x= 100,y = 400)

#button = ttk.Button(root, text="Exit", bootstyle="danger", command=quit)
#button.place(x= 500,y=700)
root.protocol("WM_DELETE_WINDOW", lambda: (root.quit(), root.destroy()))


#***************************PRINT FRAME********************************
print_main_frame = Frame(print_frame, highlightbackground="white", highlightthickness=2)
print_main_frame.pack(padx=10, pady=5) 

print_main_label = Label(print_main_frame, text="Print ECG", font=('Time', 30), foreground="white")
print_main_label.pack(padx=10) 

print_frame = ttk.LabelFrame(print_frame, borderwidth=10, text="Editor", height=200, width=500)
print_frame.pack(padx=10, pady=10, side="top", fill="y")


#plot frame
print_fig, print_ax = plt.subplots(figsize=(6, 4))
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

save_button = ttk.Button(print_frame, text="Save", command=save_to_csv)
save_button.pack(pady=0, padx=20)

#***************************SIMULATOR FRAME********************************
sim_main_frame = Frame(simulator_frame, highlightbackground="white", highlightthickness=2)
sim_main_frame.pack(padx=10, pady=5) 

sim_main_label = Label(sim_main_frame, text="Simulator ECG", font=('Time', 30), foreground="white")
sim_main_label.pack(padx=10) 

simulator_frame = ttk.LabelFrame(simulator_frame, borderwidth=10, text="Simulations", height=500, width=500)
simulator_frame.pack(padx=10, pady=10, side="top", fill="y")

def get_file_names(folder_path):
    return [file.stem for file in Path(folder_path).iterdir() if file.is_file()]

options_sim = get_file_names('./simulations')
clicked_sim_menu = StringVar()
clicked_sim_menu.set( " Simulations " ) 
save_sim_drop = OptionMenu( simulator_frame , clicked_sim_menu , *options_sim, command=load_saved_simulation)
save_sim_drop.place(x = 60, y = 50)

#clicked_sim_menu.trace_add("write", load_saved_simulation)
root.mainloop()
