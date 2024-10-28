import numpy as np
import matplotlib.pyplot as plt

def plot_ecg(y, end,filename="ecg_plot.pdf"):
    x = np.linspace(0, end, len(y))
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(x, y, color='b', lw=2)

    ax.set_xticks(np.arange(0, 9, 1), minor=False)  
    ax.set_yticks(np.arange(0, 2.6, 0.5), minor=False)  

    ax.set_xticks(np.arange(0, 8.25, 0.25), minor=True) 
    ax.set_yticks(np.arange(0, 2.6, 0.1), minor=True)  

    ax.grid(True, which='both', color='red', linestyle='-', linewidth=0.5)

    ax.grid(True, which='minor', color='red', linestyle=':', linewidth=0.2)

    ax.set_xlim(0, 8)
    ax.set_ylim(0, 2.5)

    plt.title('Simulated ECG Printout', fontsize=16)
    plt.xlabel('Time (seconds)', fontsize=12)
    plt.ylabel('Amplitude', fontsize=12)

    plt.savefig(filename, format='pdf')

    plt.close()

