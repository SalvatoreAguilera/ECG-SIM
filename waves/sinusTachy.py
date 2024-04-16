import numpy as np
from scipy.integrate import quad

def r_wave(n,b,amp, p1,p2):
    period = abs(p1)+abs(p2)
    c = -1
    def a0(x):
        return (c*b*amp*(x))/(period) + amp
        
    R_a0, _ = quad(a0, 0, p2)
    c = 1
    R1_a0, _ = quad(a0,p1,0)
    R_a0 = 1/500*(R_a0+R1_a0)
    
    
    
    def aN(low, high):
        arr = np.zeros((n))
        for i in range(1,n+1):
            f = lambda x : (a0(x))*np.cos((i*np.pi*x)/500)
            arr[i-1], _ = quad(f, low, high)
        return arr
    
    R_an = []
    R_an = aN(p1,0)
    c = -1
    R1_an = []
    R1_an = aN(0, p2)
    a_N = 1/500*(R_an+R1_an)
    return a_N, R_a0

def s_wave(n, b, amp, period, p1, p2, c2):
    
    f1 = lambda x : ((-1*b*amp*(x))/(period) + amp)
    f2 = lambda x : ((b*amp*(x+c2))/(period) + amp)
      
    R_a0, _ = quad(f1 ,20, 30)#p1, (p2/2)+(p1/2))
    R1_a0, _ = quad(f2 , 30, 40)#(p2/2)+(p1/2),p2)
    R_a0 = (1/500)*(R_a0+R1_a0)
    
    
    
    def aN(low, high, f):
        arr = np.zeros((n))
        for i in range(1,n+1):
            f3 = lambda x : (f(x))*np.cos((i*np.pi*x)/500)
            arr[i-1], _ = quad(f3, low, high)
        return arr
    
    R1_an = aN(20,30, f1)#p1, (p2/2)+(p1/2))
    R_an = aN(30,40, f2)#(p2/2)+(p1/2),p2)

    
    a_N = (1/500)*(R_an+R1_an)
    return a_N, R_a0
    


def T_wave(n, low, high, amp, c1):
    def a0(x):
        return -0.00009375 * ((x + c1)**2) + amp
    T_a0, _ = quad(a0, a=low, b=high)
    
    def aN():
        arr = np.zeros((n))
        for i in range(1,n+1):
            f = lambda x : (-9.375e-5 * ((x + c1)**2) + amp)*(np.cos((i*np.pi*x)/(500)))
            arr[i-1], _ = quad(f, a=low, b=high)
        return arr
    
    def bN():
        arr = np.zeros(n)
        for i in range(1, n + 1):
            f = lambda x: (-(9.375e-5 * (x + c1)**2) + amp) * np.sin((i * np.pi * x) / 500)
            arr[i - 1], _ = quad(f, low, high)
        return arr
    T_a0 = T_a0 * (1/500)
    T_aN = aN()*(1/500)
    T_bN = bN()*(1/500)
    return T_aN, T_a0, T_bN


def fourier():
    #R-WAVE
    n, b, amp, p1, p2 = 40, 2, 2.5, -20, 20
    R_an, R_a0 = r_wave(n,b,amp, p1,p2)
    #Q_an, Q_a0 = coefficients(n, b, amp, 20, 40, -60)
    S_an, S_a0 = s_wave(n, b, amp, abs(p1)+abs(p2), 20, 40, -60)
    T_an, T_a0, T_bn = T_wave(n, 200, 360, .6,-280)
    P_an, P_a0, P_bn = T_wave(n, -260, -143, .3, 200)
    #R_an +=  Q_an + S_an  
    R_a0 +=  T_a0 + S_a0 + P_a0
    
    x = np.arange(-10000, 10000, 1)
    
    y = np.zeros(len(x))
    for j in range (len(x)):
        for i in range(1,n+1):
            y[j] +=  (np.cos((np.pi*i*x[j])/350) * T_an[i-1]) + (np.sin((np.pi*i*x[j])/350) * T_bn[i-1])
            y[j] +=  (np.cos((np.pi*i*x[j])/350) * R_an[i-1])
            y[j] +=  (np.cos((np.pi*i*x[j])/350) * S_an[i-1])
            y[j] +=  (np.cos((np.pi*i*x[j])/350) * P_an[i-1]) + (np.sin((np.pi*i*x[j])/350) * P_bn[i-1])
        y[j] += (R_a0/2)
    return x, y

x, y = fourier()
