# GUI UPDATED 
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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
     
# FUNCTION CREATES NEW WINDOW FOR THE LIVE ECG
def new_ecg_signal():
        ecg_signal_frame = tk.Frame(btm2_frame, height=frame_size_height,                                      # ecg signal frame inside btm2
                            width=(frame_size_width))
        ecg_signal_frame.grid(row = 0, column=0, columnspan=2)


def ecg_start():
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
    ecg_frame.config(text=clicked.get())
    animation(ecg_num)

    
t = np.linspace(-2,2,1200)
y = normal.normal()

def animation(ecg_num):
    global t, y

    queue_anim = 0
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
    # mockup
    t2 = np.linspace(-2,2,1000)
    y2 = np.linspace(1,1, 1000)
    fig2, axis2 = plt.subplots(figsize=(7,2),facecolor="black")
    
    # function for Funcanimation 
    def update(frame):
        nonlocal queue_anim
        # update the new points after each frame
        animated_plot.set_data(t[:frame], y[:frame])
        animated_plot2.set_data(t2[:frame], y2[:frame])
        if(frame == len(t)-1 and queue_anim > 0):
            queue_anim -= 1
            
        
        return animated_plot, animated_plot2
    
    axis.set_xlim([min(t),max(t)])                                # set the limits of time for x
    axis.set_ylim([min(y),max(y)])                                         # Set limit for amplitude for y 
    axis2.set_xlim([-.1,.1])                                # set the limits of time for x
    axis2.set_ylim([-2,2]) 
    plt.xticks(np.arange(min(t), max(t)+1, 0.25))
    plt.yticks(np.arange(min(y)-1,max(y), 0.25)) 
    animated_plot, = axis.plot([],[],color="#84f91c")
    animated_plot2, = axis2.plot([],[],color="#84f91c")
    axis.set_facecolor("black")
    axis2.set_facecolor("black")                                   # set background of graph as black



    # call animation
    animate = FuncAnimation(fig= fig1, func= update,frames=len(t),interval=10, repeat="False")
    #animate2 = FuncAnimation(fig= fig2, func= update,frames=len(t),interval=10, repeat="False")
    
    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig1, ecg_signal_frame)
    canvas2 = FigureCanvasTkAgg(fig2, btm3_frame)
    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(side="left")
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", anchor="w", fill="both", expand=True)


    # dot blicking
    def blicking():
        cur_color = d_canvas.itemcget(dot, 'fill')
        new_color = 'red' if cur_color == 'black' else 'black'
        d_canvas.itemconfig(dot, fill=new_color)
        d_canvas.after(1000,blicking)

    blicking()

    def update_rate():
        HR_canvas.itemconfig(rate, text=str(hr))

    hr = normal.get_HR()
    HR_canvas.after(11000,update_rate)

    #stop animation and update 
    def on_click_update():
        global y
        nonlocal hr, queue_anim
        queue_anim += 1
        y = normal.update_ecg()
        hr= normal.get_HR()
        update_rate()

    # buttom frame
    def on_click_exit():
        clicked.set(" Heart Rhythms ")
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

########Main window for ECG###############
window = ttk.Window(themename = "cyborg")
window.title("ECG Simulator")
window.attributes('-fullscreen',True)

#screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# size for frames
pf_width_size = int(screen_width * .25)
pf_height_size = int(screen_height * .70)
df_width_size = int(screen_width * .15)
df_height_size = int(screen_height * .70)
ecg_width_size = int(screen_width * .60)
ecg_height_size = int(screen_height * .70)
save_width_size = int(screen_width * .20)
save_height_size = int(screen_height * .30)

#quit
def on_escape(event):
    window.quit() 
window.bind('<Escape>', on_escape)

### TOP / BOTTOM FRAMES ######
top_frame = ttk.Frame(width = screen_width, height= (screen_height* .75))
top_frame.grid(row = 0)
bottom_frame = ttk.Frame(width = screen_width, height= (screen_height* .25))
bottom_frame.grid(row = 1)

# parameter container
parameter_frame = ttk.LabelFrame(top_frame, text="PARAMETERS",takefocus="1", width= pf_width_size, height=pf_height_size)
parameter_frame.grid(row= 1,column=0, rowspan= 2,columnspan= 1,padx=5, pady=5, sticky="w")
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

# disease container 
disease_frame = ttk.LabelFrame(top_frame, borderwidth=10, text="DISEASES",height=df_height_size, width=df_width_size)
disease_frame.grid(row= 1,column=1,columnspan=1, rowspan=2, padx=10, pady=5)

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
# menu for disease 
clicked = tk.StringVar()  
clicked.set( " Heart Rhytms " ) 
drop = ttk.OptionMenu( disease_frame , clicked , *options )
drop.place(x = 50, y = 50)

# Button to start signal
btn_start = ttk.Button(disease_frame , text = " Start " ,style='S.TButton', command= ecg_start)
btn_x_start = int((df_width_size/3))
btn_start.config(width= 7)
btn_start.place(x= btn_x_start,y = 400)
# close window
btn_quit = ttk.Button(disease_frame, text="Exit", style="Q.TButton", command=quit)
btn_x_quit = int((df_width_size/3))
btn_quit.config(width= 7)
btn_quit.place(x= btn_x_quit,y=450)


########live ecg frame############
ecg_frame = ttk.LabelFrame(top_frame, text="LIVE ECG", width= ecg_width_size,height=ecg_height_size)
ecg_frame.grid(row =1, column= 2)

frame_size_width = ecg_width_size * .80                                                                # width for signal frame
frame_size_height = ecg_height_size * .35                                                              # height for signal frame
bot_frame_size_w = ecg_width_size * .20                                                                # bottom frames width
bot_frame_size_h = ecg_height_size * .30                                                               # bottom frames height
hr_width_side = ecg_width_size * .20                                                                   # heatrate width for frame

leadII_label = ttk.Label(ecg_frame,text="LEAD II", foreground="#84f91c")                                                      # Label for LeadII
leadII_label.grid(row = 0, column = 0, sticky="w")                                                                 # placing leadII
btm2_frame = ttk.Frame(ecg_frame, height=frame_size_height,width= frame_size_width)                     # frame for leadII signal
btm2_frame.grid(row = 1, column=0, columnspan=2)

leadV1_frame = ttk.Label(ecg_frame,text="V1", foreground="#84f91c")                                                           # Label for LeadV1
leadV1_frame.grid(row = 2, column=0, sticky= "w")
btm3_frame = tk.Frame(ecg_frame,bg="black",height=frame_size_height,                                   # frame for V1
                      width=ecg_width_size)
btm3_frame.grid(row = 3, column=0, columnspan=2)

btm4_frame = tk.Frame(ecg_frame, bg="black",height=bot_frame_size_h,                                   # frame for bottom frames
                      width=bot_frame_size_w)
btm4_frame.grid(row = 4)

ecg_signal_frame = tk.Frame(btm2_frame, bg= "black",height=frame_size_height,                                      # ecg signal frame inside btm2
                            width=(frame_size_width))
ecg_signal_frame.grid(row = 0, column=0, columnspan=2)

HR_frame= tk.Frame(btm2_frame,width=hr_width_side,height=100)                                          # frame for heartrate  
HR_frame.grid(row= 0, column=3)
HR_canvas = tk.Canvas(HR_frame,highlightthickness=0, bg="black",width = 100,                          # Canvas for HR to display numbers
                     height=100)
HR_canvas.grid(row = 0, column=2)
Heart_rate = HR_canvas.create_text(10,10, text="HR", font=('Arial', 15), fill= "red")                   # label for heartrate

d_canvas = tk.Canvas(HR_frame, bg="black",bd=0,highlightcolor="black",                                 # canvas to draw the red circle
                     highlightthickness=0, width = 18, height=20)
d_canvas.grid(row=0, column=0)
dot = d_canvas.create_oval(2, 2, 18, 18, fill='red', outline= "")                                      # create the dot
rate = HR_canvas.create_text(50, 50, text="--", font=('Arial', 40), fill= "#99f20f")                    # output the HR

x_frame = tk.Frame(btm4_frame,width =350, height= bot_frame_size_h)
x_frame.grid(row=0, column=0)

pulse_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h, padx= 15)
pulse_frame.grid(row = 0, column=1)
pulse_canvas = tk.Canvas(pulse_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw pulse
                         height= bot_frame_size_h, width=100)                           
pulse_canvas.grid(row = 0, column=0)                                                            
pulse = pulse_canvas.create_text(20,20, text="Pulse", font=('Arial', 15), fill= "#0fbef2")              # create pulse label
pulse_result = pulse_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "#0fbef2" )         # create "--" waiting for input

awRR_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h, padx= 15)
awRR_frame.grid(row = 0, column= 2)
awRR_canvas = tk.Canvas(awRR_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw awRR
                         width= 100, height= bot_frame_size_h)                           
awRR_canvas.grid(row = 0, column= 0)                                                            
awRR = awRR_canvas.create_text(20,20, text="awRR", font=('Arial', 15), fill= "white")                                  # create awRR label
awRR_result = awRR_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "white" )         # create "--" waiting for input

Tperi_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h, padx= 15)
Tperi_frame.grid(row = 0, column= 3)
Tperi_canvas = tk.Canvas(Tperi_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw pulse
                         width=100, height= bot_frame_size_h)                           
Tperi_canvas.grid(row = 0, column= 0)                                                          
Tperi = Tperi_canvas.create_text(20,20, text="Tperi", font=('Arial', 15), fill= "#84f91c")              # create pulse label
Tperi_result = Tperi_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "#84f91c" )         # create "--" waiting for input

########save test frame###########
save_frame = ttk.LabelFrame(bottom_frame, text="History", width= save_width_size, height=save_height_size)
save_frame.grid(row = 0, column= 0)

placeholder = ttk.LabelFrame(bottom_frame, width=save_width_size, height=save_height_size)
placeholder.grid(row = 0, column= 1)
placeholder = ttk.LabelFrame(bottom_frame, width=save_width_size, height=save_height_size)
placeholder.grid(row = 0, column= 2)
placeholder = ttk.LabelFrame(bottom_frame, width=save_width_size, height=save_height_size)
placeholder.grid(row = 0, column= 3)

window.mainloop()