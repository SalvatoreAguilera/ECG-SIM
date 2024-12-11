import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import normal

def plot_ecg(y_lead2, end, filename="ecg_plot.pdf"):
    s_y = len(y_lead2)
    x = np.linspace(0, end, s_y)
    
    offset_lead1 = y_lead2[0] - (0.5 * y_lead2[0]) 
    offset_lead3 = y_lead2[0] - (0.5 * y_lead2[0])
    offset_avr = y_lead2[0] - (-0.5 * y_lead2[0])
    offset_avl = y_lead2[0] - (0.5 * y_lead2[0])
    offset_avf = y_lead2[0] - y_lead2[0] 
    offset_v1 = y_lead2[0] - (-1 * y_lead2[0])
    offset_v2 = y_lead2[0] - (-0.7 * y_lead2[0])
    offset_v3 = y_lead2[0] - (-1 * y_lead2[0])  
    offset_v6 = y_lead2[0] - y_lead2[0]  

    y_lead1 = (0.5 * y_lead2) + offset_lead1                # Lead I approximation
    y_lead3 = (0.5 * y_lead2) + offset_lead3          # Lead III approximation
    y_avr = (-0.5 * y_lead2) + offset_avr              # aVR approximation
    y_avl = (0.5 * y_lead2) + offset_avl               # aVL approximation
    y_avf = y_lead2 + offset_avf                        # aVF approximation
    y_v1 = (-1 * y_lead2) + offset_v1                # V1 approximation
    y_v2 = (-0.7 * y_lead2) + offset_v2                 # V2 approximation
    y_v3 = (-1 * y_lead2) + offset_v3                          # V3 approximation
    y_v6 = y_lead2 + offset_v6                          # V6 approximation
    
    fig, ax = plt.subplots(figsize=(10, 6))
    #bottom to top of print out
    # Lead II
    plt.text(0, 2, "II", fontsize=12, color='black')
    ax.plot(x, y_lead2+.5, lw=0.5, color='black')  

    # Lead III, aVF, V3, V6
    plt.text(0, 4.5, "III", fontsize=12, color='black')
    ax.plot(x[0:int(s_y * 0.225)], y_lead3[0:int(s_y * 0.225)] + 3, lw=0.5, color='black')  
    plt.text(2.5, 4.5, "VF", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.25):int(s_y * 0.475)], y_avf[0:int(s_y * 0.225)] + 3, lw=0.5, color='black')  
    plt.text(5, 4.5, "V3", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.5):int(s_y * 0.725)], y_v3[0:int(s_y * 0.225)] + 3, lw=0.5, color='black')  
    plt.text(7.5, 4.5, "V6", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.75):int(s_y * 0.975)], y_v6[0:int(s_y * 0.225)] + 3, lw=0.5, color='black')  

    # Lead II, aVL, V2, V5
    plt.text(0, 7, "II", fontsize=12, color='black')
    ax.plot(x[0:int(s_y * 0.225)], y_lead2[0:int(s_y * 0.225)] + 5.5, lw=0.5, color='black') 
    plt.text(2.5, 7, "aVL", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.25):int(s_y * 0.475)], y_avl[0:int(s_y * 0.225)] + 5.5, lw=0.5, color='black') 
    plt.text(5, 7, "V2", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.5):int(s_y * 0.725)], y_v2[0:int(s_y * 0.225)] + 5.5, lw=0.5, color='black') 
    plt.text(7.5, 7, "V5", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.75):int(s_y * 0.975)], y_lead2[0:int(s_y * 0.225)] + 5.5, lw=0.5, color='black')  

    # Lead I, aVR, V1, V4
    plt.text(0, 9.5, "I", fontsize=12, color='black')
    ax.plot(x[0:int(s_y * 0.225)], y_lead1[0:int(s_y * 0.225)] + 8, lw=0.5, color='black') 
    plt.text(2.5, 9.5, "aVR", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.25):int(s_y * 0.475)], y_avr[0:int(s_y * 0.225)] + 8, lw=0.5, color='black')
    plt.text(5, 9.5, "V1", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.5):int(s_y * 0.725)], y_v1[0:int(s_y * 0.225)] + 8, lw=0.5, color='black') 
    plt.text(7.5, 9.5, "V4", fontsize=12, color='black')
    ax.plot(x[int(s_y * 0.75):int(s_y * 0.975)], y_lead1[0:int(s_y * 0.225)] + 8, lw=0.5, color='black') 


    ax.set_xticks(np.arange(0, 10, 1), minor=False)
    ax.set_yticks(np.arange(0, 10, .5), minor=False)
    ax.set_xticks(np.arange(0, 10, 0.25), minor=True)
    ax.set_yticks(np.arange(0, 10, 0.1), minor=True)
    
    ax.grid(True, which='both', color='red', linestyle='-', linewidth=0.5)
    ax.grid(True, which='minor', color='red', linestyle=':', linewidth=0.2)
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0,10)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)
    
    if not filename.endswith('.pdf'):
        filename += '.pdf'
    
    ax.legend(loc="upper right")
    plt.savefig(filename, format='pdf')
    plt.close()
    


