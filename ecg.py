import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
import matplotlib.pylab as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg) 
import numpy as np
import normal
import sinusBrady
import sinusTachy
import sinusArr
import vFib

spinboxes = []
def set_parameters(wave_f, wave, num):
    wave_var = wave + " Wave"
    wave_label = ttk.Label(wave_f,borderwidth=10, text = wave_var, font=('Time', 20), foreground="white")
    wave_label.pack(side = "top", anchor="w",expand=False)
    
    for i in range(num):
        if i == 0:
            amp_label = ttk.Label(wave_f, text="Amplitude", font=('Time', 12), foreground="#6082B6")
            amp_label.pack(side="left")
        elif i == 1:
            period_label = ttk.Label(wave_f, text="Period", font=('Time', 12), foreground="#6082B6")
            period_label.pack(side="left")
        else:
            time_label = ttk.Label(wave_f, text="Time", font=('Time', 12), foreground="#6082B6")
            time_label.pack(side="left")
        spinbox = ttk.Spinbox(wave_f, from_=0, to=10, increment= 0.01, width = 4)
        spinbox.pack(side="left")
        spinboxes.append(spinbox)

# exit function
def exit_ecg():
    window.destroy()
    exit()

# FUNCTION starts THE LIVE ECG
def ecg_start():
    # disease list need to update since chart shouldnt be next to the ecg signal 
    ecg_list = [["Atrial Flutter", 0],["VF", 1],["Atrial Tachycardia",2],["Sinus Arrhythmia",1],["A Fib",0],["Normal Rhythm", 2],["VT", 6],["Multifocal Atrial Tachycardia",7],
                ["VFib",1], ["Bradycardia",4], ["Tachycardia", 5]]
    
    for i in range(0,len(ecg_list)):
        if ( clicked.get() == ecg_list[i][0]):
            ecg_num = ecg_list[i][1]
    
    # color of background for the main window
    ecg_frame.config(text=clicked.get())
    animation(ecg_num)

####################################
####### ANIMATION FUNCTION #########
def animation(ecg_num):
    # data for graphing the signal
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

    # mockup
    t2 = np.linspace(-2,2,1000)
    y2 = np.linspace(1,1, 1000)
    fig2, axis2 = plt.subplots(figsize=(7,2),facecolor="black")
    # function for Funcanimation 
    def update(frame):
    # update the new points after each frame
        animated_plot.set_data(t[:frame], y[:frame])
        animated_plot2.set_data(t2[:frame], y2[:frame])
        return animated_plot, animated_plot2
        
    
    axis.set_xlim([min(t),max(t)])                                # set the limits of time for x
    axis.set_ylim([min(y),max(y)]) 
    axis2.set_xlim([-.1,.1])                                # set the limits of time for x
    axis2.set_ylim([-2,2])                                        # Set limit for amplitude for y 
    plt.xticks(np.arange(min(t), max(t)+1, 0.25))
    plt.yticks(np.arange(min(y)-1,max(y), 0.25)) 
    animated_plot, = axis.plot([],[],color="#84f91c")
    animated_plot2, = axis2.plot([],[],color="#84f91c")
    
    axis.set_facecolor("black")                                   # set background of graph as black
    axis2.set_facecolor("black")
    # call animation
    animate = FuncAnimation(fig= fig, func= update,frames=len(t),interval=10, repeat="False")
    animate2 = FuncAnimation(fig= fig2, func= update,frames=len(t),interval=10, repeat="False")
    
    # Embed fig in canvas
    canvas = FigureCanvasTkAgg(fig, ecg_signal_frame)  
    canvas2 = FigureCanvasTkAgg(fig2, btm3_frame)
    # draw ecg signal
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", fill="both", expand=True)
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
        HR_canvas.itemconfig(rate, text=str(HR))

    if (ecg_num == 2):
            HR = int(normal.Hr)
    elif (ecg_num ==4):
        HR = int(sinusBrady.Hr)
    # add more heartrates for dieseas
    # ...
    #
    HR_canvas.after(11000,update_rate)


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

### TOP / BOTTOM FRAMES ######
top_frame = tk.Frame(width = screen_width, height= (screen_height* .75))
top_frame.pack(side = "top", expand=False, fill = "both")
bottom_frame = tk.Frame(width = screen_width, height= (screen_height* .25))
bottom_frame.pack(side="top", fill='both', expand=False)

############# Parameter frame ############
parameter_f  = tk.LabelFrame(top_frame,text="Parameter", width= pf_width_size, height= pf_height_size)
parameter_f.pack(side="left", anchor= "ne", padx = 5, pady=5, fill= "both", expand=False)
wave_p = tk.Frame(parameter_f, width = pf_width_size, height= (pf_height_size* .15), padx = 5, pady= 5)
wave_p.pack(expand=False)
set_parameters(wave_p, "P", 3)
wave_q = tk.Frame(parameter_f, width = pf_width_size, height= (pf_height_size* .15), padx = 5, pady= 5)
wave_q.pack(expand=False)
set_parameters(wave_q, "Q", 3)
wave_r = tk.Frame(parameter_f, width = pf_width_size, height= (pf_height_size* .15), padx = 5, pady= 5)
wave_r.pack(expand=False)
set_parameters(wave_r, "R", 3)
wave_s = tk.Frame(parameter_f, width = pf_width_size, height= (pf_height_size* .15), padx = 5, pady= 5)
wave_s.pack(expand=False)
set_parameters(wave_s, "S", 3)
wave_t = tk.Frame(parameter_f, width = pf_width_size, height= (pf_height_size* .15), padx = 5, pady= 5)
wave_t.pack(expand=False)
set_parameters(wave_t, "T", 3)
wave_u = tk.Frame(parameter_f, width = pf_width_size, height= (pf_height_size* .15), padx = 5, pady= 5)
wave_u.pack(expand=False)
set_parameters(wave_u, "U", 3)

###### disease frame ################
disease_frame = ttk.LabelFrame(top_frame, text="Disease Control", width= df_width_size, height=df_height_size)
disease_frame.pack(side="left", anchor= "ne", padx= 5, pady= 5)

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
clicked.set("Heart Rhytms") 
drop = ttk.OptionMenu( disease_frame , clicked , *options )
drop.config(width=10)
drop.place(x = 42, y = 50)

########live ecg frame############
ecg_frame = ttk.LabelFrame(top_frame, text="LIVE ECG", width= ecg_width_size,                          # ECG main frame
                           height=ecg_height_size)
ecg_frame.pack(side="left", anchor="ne", padx = 5, pady= 5, expand=False,                              # placement of ecg_frame
               fill="both")

frame_size_width = ecg_width_size * .80                                                                # width for signal frame
frame_size_height = ecg_height_size * .35                                                              # height for signal frame
bot_frame_size_w = ecg_width_size * .20                                                                # bottom frames width
bot_frame_size_h = ecg_height_size * .30                                                               # bottom frames height
hr_width_side = ecg_width_size * .20                                                                   # heatrate width for frame

leadII_label = tk.Label(ecg_frame,text="LEAD II")                                                      # Label for LeadII
leadII_label.pack(side="top",anchor="nw", expand=False)                                                # placing leadII
btm2_frame = tk.Frame(ecg_frame, bg="black",bd=0, height=frame_size_height,                             # frame for leadII signal
                      width=bot_frame_size_w)
btm2_frame.pack(side="top", expand=True)                                                              # placement of leadII signal

leadV1_frame = tk.Label(ecg_frame,text="V1")                                                           # Label for LeadV1
leadV1_frame.pack(side="top",anchor="nw", expand=False)
btm3_frame = tk.Frame(ecg_frame,bg="black",height=frame_size_height,                                   # frame for V1
                      width=ecg_width_size)
btm3_frame.pack(side="top", expand=False, fill="both")

btm4_frame = tk.Frame(ecg_frame, bg="black",height=bot_frame_size_h,                                   # frame for bottom frames
                      width=bot_frame_size_w)
btm4_frame.pack(side="top", expand=False)

ecg_signal_frame = tk.Frame(btm2_frame, height=frame_size_height,                                      # ecg signal frame inside btm2
                            width=(frame_size_width))
ecg_signal_frame.pack(side="left", expand=False, fill="both")

HR_frame= tk.Frame(btm2_frame,width=hr_width_side,height=100)                                          # frame for heartrate  
HR_frame.pack(side="left")
HR_canvas = tk.Canvas(HR_frame,highlightthickness=0, bg="black",width = 100,                          # Canvas for HR to display numbers
                     height=100)
HR_canvas.pack(expand=False)
Heart_rate = HR_canvas.create_text(10,10, text="HR", font=('Arial', 15), fill= "red")                   # label for heartrate
d_canvas = tk.Canvas(HR_frame, bg="black",bd=0,highlightcolor="black",                                 # canvas to draw the red circle
                     highlightthickness=0, width = 18, height=20)
d_canvas.pack(side="left", anchor="nw", expand=False)
dot = d_canvas.create_oval(2, 2, 18, 18, fill='red', outline= "")                                      # create the dot
rate = HR_canvas.create_text(50, 50, text="--", font=('Arial', 40), fill= "#99f20f")                    # output the HR

x_frame = tk.Frame(btm4_frame,width =350, height= bot_frame_size_h)
x_frame.pack(side="left")

pulse_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h)
pulse_frame.pack(side="left", padx = 25)
pulse_canvas = tk.Canvas(pulse_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw pulse
                         height= bot_frame_size_h, width=100)                           
pulse_canvas.pack(side="left", expand=False)                                                            
pulse = pulse_canvas.create_text(20,20, text="Pulse", font=('Arial', 15), fill= "#0fbef2")              # create pulse label
pulse_result = pulse_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "#0fbef2" )         # create "--" waiting for input

awRR_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h)
awRR_frame.pack(side="left", padx= 25)
awRR_canvas = tk.Canvas(awRR_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw awRR
                         width= 100, height= bot_frame_size_h)                           
awRR_canvas.pack(side="left", expand=False)                                                            
awRR = awRR_canvas.create_text(20,20, text="awRR", font=('Arial', 15), fill= "white")                                  # create awRR label
awRR_result = awRR_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "white" )         # create "--" waiting for input

Tperi_frame = tk.Frame(btm4_frame,width = bot_frame_size_w, height = bot_frame_size_h)
Tperi_frame.pack(side="left",padx=25)
Tperi_canvas = tk.Canvas(Tperi_frame, highlightthickness=0, bd= 0, bg="black",                           # establish canvas to draw pulse
                         width=100, height= bot_frame_size_h)                           
Tperi_canvas.pack(side="left", expand=False)                                                            
Tperi = Tperi_canvas.create_text(20,20, text="Tperi", font=('Arial', 15), fill= "#84f91c")              # create pulse label
Tperi_result = Tperi_canvas.create_text(70,70, text="--", font=('Arial', 50), fill= "#84f91c" )         # create "--" waiting for input

# Button to start signal
btn_start = ttk.Button(disease_frame , text = " Start " ,style='S.TButton', command= ecg_start)
btn_x_start = int((df_width_size/3))
btn_start.config(width= 7)
btn_start.place(x= btn_x_start,y = 400)
# close window
btn_quit = ttk.Button(disease_frame, text="Exit", style="Q.TButton", command=exit_ecg)
btn_x_quit = int((df_width_size/3))
btn_quit.config(width= 7)
btn_quit.place(x= btn_x_quit,y=450)

########save test frame###########
save_frame = ttk.LabelFrame(bottom_frame, text="History", width= save_width_size, height=save_height_size)
save_frame.pack(side="left", anchor="ne", padx =5, pady = 5)


############frame#################
placeholder = ttk.LabelFrame(bottom_frame, width=save_width_size, height=save_height_size)
placeholder.pack(side='left', anchor='ne', padx =5, pady = 5, expand=False, fill="both")
placeholder2 = ttk.LabelFrame(bottom_frame, width=200, height=save_height_size)
placeholder2.pack(side='left', anchor='ne', padx =5, pady = 5, expand=False, fill="both")
placeholder3 = ttk.LabelFrame(bottom_frame, width=650, height=save_height_size)
placeholder3.pack(side='left', anchor='ne', padx =5, pady = 5, expand=False, fill="both")

window.mainloop()