import numpy as np
import matplotlib.pyplot as plt



x = np.arange(-1000, 1001, 1)
y = np.sin(5*x) + np.sin(x)



plt.figure(figsize=(10, 6))
plt.plot(x,y)
plt.title('Noisy Wave vs Original Cosine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.xlim(-200,200)
plt.ylim(-2.5, 2.5)
plt.show()
