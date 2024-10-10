import numpy as np
import matplotlib.pyplot as plt

def p_wav(x, a_pwav, d_pwav, t_pwav, li):
    l = li
    a = a_pwav
    x = x + t_pwav
    b = (2 * l) / d_pwav
    n = 100
    p1 = 1 / l
    p2 = 0
    for i in range(1, n+1):
        harm1 = (((np.sin((np.pi / (2 * b)) * (b - (2 * i)))) / (b - (2 * i)) + 
                  (np.sin((np.pi / (2 * b)) * (b + (2 * i)))) / (b + (2 * i))) * 
                  (2 / np.pi)) * np.cos((i * np.pi * x) / l)
        p2 += harm1
    pwav1 = p1 + p2
    pwav = a * pwav1
    return pwav

def qrs_wav(x, a_qrswav, d_qrswav, li):
    l = li  #time period
    a = a_qrswav #amp
    b = (2 * l) / d_qrswav #distance
    n = 100
    qrs1 = (a / (2 * b)) * (2 - b)
    qrs2 = 0
    for i in range(1, n+1):
        harm = (((2 * b * a) / (i * i * np.pi * np.pi)) * 
                (1 - np.cos((i * np.pi) / b))) * np.cos((i * np.pi * x) / l)
        qrs2 += harm
    qrswav = qrs1 + qrs2
    return qrswav
def q_wav(x, a_qwav, d_qwav, t_qwav, li):
    l = li
    x = x + t_qwav
    a = a_qwav
    b = (2 * l) / d_qwav
    n = 100
    q1 = (a / (2 * b)) * (2 - b)
    q2 = 0
    for i in range(1, n+1):
        harm5 = (((2 * b * a) / (i * i * np.pi * np.pi)) * 
                 (1 - np.cos((i * np.pi) / b))) * np.cos((i * np.pi * x) / l)
        q2 += harm5
    qwav = -1 * (q1 + q2)
    return qwav

def s_wav(x, a_swav, d_swav, t_swav, li):
    l = li
    x = x - t_swav
    a = a_swav
    b = (2 * l) / d_swav
    n = 100
    s1 = (a / (2 * b)) * (2 - b)
    s2 = 0
    for i in range(1, n+1):
        harm3 = (((2 * b * a) / (i * i * np.pi * np.pi)) * 
                 (1 - np.cos((i * np.pi) / b))) * np.cos((i * np.pi * x) / l)
        s2 += harm3
    swav = -1 * (s1 + s2)
    return swav
def t_wav(x, a_twav, d_twav, t_twav, li):
    l = li
    a = a_twav
    x = x - t_twav - 0.045
    b = (2 * l) / d_twav
    n = 100
    t1 = 1 / l
    t2 = 0
    for i in range(1, n+1):
        harm2 = (((np.sin((np.pi / (2 * b)) * (b - (2 * i)))) / (b - (2 * i)) + 
                  (np.sin((np.pi / (2 * b)) * (b + (2 * i)))) / (b + (2 * i))) * 
                  (2 / np.pi)) * np.cos((i * np.pi * x) / l)
        t2 += harm2
    twav1 = t1 + t2
    twav = a * twav1
    return twav

def u_wav(x, a_uwav, d_uwav, t_uwav, li):
    l = li
    a = a_uwav
    x = x - t_uwav
    b = (2 * l) / d_uwav
    n = 100
    u1 = 1 / l
    u2 = 0
    for i in range(1, n+1):
        harm4 = (((np.sin((np.pi / (2 * b)) * (b - (2 * i)))) / (b - (2 * i)) + 
                  (np.sin((np.pi / (2 * b)) * (b + (2 * i)))) / (b + (2 * i))) * 
                  (2 / np.pi)) * np.cos((i * np.pi * x) / l)
        u2 += harm4
    uwav1 = u1 + u2
    uwav = a * uwav1
    return uwav

params = {
    'p': {'a': 0.25,    'd': 0.09,  't': 0.16},
    'q': {'a': 0.025,   'd': 0.066, 't': 0.166},          #DO NOT CHANGE THE AMPLITUDED OF Q WAVE
    'r': {'a': 1.6,     'd': 0.11,   't': 0.4},
    's': {'a': 0.25,   'd': 0.066, 't': 0.09},
    't': {'a': .35,     'd': 0.142, 't': 0.2}         #DO NOT CHANGE THE AMPLITUDE OF T WAVE
    #'u': {'a': 0.035,   'd': 0.0476, 't': 0.433}
}

li = 30/72  # Length of the interval (1 second)
time = np.linspace(-2, 2, 1200)  

p_wave = p_wav(time, params['p']['a'], params['p']['d'], params['p']['t'], li)
q_wave = q_wav(time, params['q']['a'], params['q']['d'], params['q']['t'], li)
r_wave = qrs_wav(time, params['r']['a'], params['r']['d'], li)
s_wave = s_wav(time, params['s']['a'], params['s']['d'], params['s']['t'], li)
t_wave = t_wav(time, params['t']['a'], params['t']['d'], params['t']['t'], li)
#u_wave = u_wav(time, params['u']['a'], params['u']['d'], params['u']['t'], li)


ecg_waveform = []

#Updated code to a function
#Previous code: ecg_waveform = p_wave + q_wave + r_wave + s_wave + t_wave + u_wave
#function to call to update ecg live
def update_ecg():
    global ecg_waveform  
    time = np.linspace(-2, 2, 1200)  
    p_wave = p_wav(time, params['p']['a'], params['p']['d'], params['p']['t'], li)
    q_wave = q_wav(time, params['q']['a'], params['q']['d'], params['q']['t'], li)
    r_wave = qrs_wav(time, params['r']['a'], params['r']['d'], li)
    s_wave = s_wav(time, params['s']['a'], params['s']['d'], params['s']['t'], li)
    t_wave = t_wav(time, params['t']['a'], params['t']['d'], params['t']['t'], li)
    #u_wave = u_wav(time, params['u']['a'], params['u']['d'], params['u']['t'], li)
    ecg_waveform = p_wave + q_wave + r_wave + s_wave + t_wave #+ u_wave
    
    return ecg_waveform


#updated code to a function
#reason: to change the haeart when the person inputs different params
def get_HR():
    max_y = np.max(ecg_waveform)
    index = []

    for i in range(len(ecg_waveform)):
        if (ecg_waveform[i] >= max_y-.01):
            index.append(i)

    Hr = 300 / ((index[3]-index[2])/50)
    return Hr


def normal():
    global params, li
    params = {
        'p': {'a': 0.25,    'd': 0.09,  't': 0.16},
        'q': {'a': 0.025,   'd': 0.066, 't': 0.166},          
        'r': {'a': 1.6,     'd': 0.11,   't': 0.4},
        's': {'a': 0.25,   'd': 0.066, 't': 0.09},
        't': {'a': .35,     'd': 0.142, 't': 0.2}         
        #'u': {'a': 0.035,   'd': 0.0476, 't': 0.433}
    }
    
    li = 30/72
    return update_ecg()

def sinus_arrythmia():
    global params, li
    params = {
        'p': {'a': 0.25, 'd': 0.09, 't': 0.18},
        'q': {'a': 0.025, 'd': 0.066, 't': 0.17},
        'r': {'a': 1.6, 'd': 0.11, 't': 0.42},
        's': {'a': 0.25, 'd': 0.066, 't': 0.10},
        't': {'a': 0.35, 'd': 0.142, 't': 0.22},
        # 'u': {'a': 0.035, 'd': 0.0476, 't': 0.433}
    }
    li = 30/72
    return update_ecg()
    
def sinus_brady():
    global params, li
    params = {
        'p': {'a': 0.25, 'd': 0.09, 't': 0.25},
        'q': {'a': 0.025, 'd': 0.066, 't': 0.20},
        'r': {'a': 1.6, 'd': 0.11, 't': 0.50},
        's': {'a': 0.25, 'd': 0.066, 't': 0.12},
        't': {'a': 0.35, 'd': 0.142, 't': 0.30},
        # 'u': {'a': 0.035, 'd': 0.0476, 't': 0.433}
    } 
    li = 30/72
    return update_ecg()
    
def sinus_tachy():
    global params, li
    params = {
        'p': {'a': 0.25, 'd': 0.09, 't': 0.12},
        'q': {'a': 0.025, 'd': 0.066, 't': 0.10},
        'r': {'a': 1.6, 'd': 0.11, 't': 0.25},
        's': {'a': 0.25, 'd': 0.066, 't': 0.08},
        't': {'a': 0.35, 'd': 0.142, 't': 0.15},
        # 'u': {'a': 0.035, 'd': 0.0476, 't': 0.433}
    }
    
    li = 30/72 
    return update_ecg()
    
def vfib():
    global params, li
    params = {
        'p': {'a': 0.1, 'd': 0.04, 't': 0.05},
        'q': {'a': 0.1, 'd': 0.03, 't': 0.05},
        'r': {'a': 0.8, 'd': 0.05, 't': 0.1},
        's': {'a': 0.1, 'd': 0.03, 't': 0.05},
        't': {'a': 0.1, 'd': 0.03, 't': 0.05},
        # 'u': {'a': 0.035, 'd': 0.0476, 't': 0.433}
    }
    li = 30/72
    return update_ecg()

