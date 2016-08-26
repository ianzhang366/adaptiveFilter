import numpy as np
import matplotlib.pyplot as plt
import pdb
import lms_filter
import nlms_filter

Fs = 1000.0 #sampling rate
Ts = 1.0/ Fs # sampling interval
t = np.arange(0,1, Ts) # time vector
ff = 5 # frequency of the signal
y = np.sin(2 *np.pi* ff* t)

pure = np.linspace(-1, 1, 1000)
noise = np.random.normal(0, 1, 1000)
y = y + noise
plt.plot(y,'b', label= 'signal with noise')

np,weight,er = lms_filter.lms_filter(y,5,0.15)
print weight
# np,weight,er = nlms_filter.nlms_filter(y,5,1)
# print weight

plt.plot(np,'r', label= 'lsm')
plt.plot(er,'g', label= 'MSE')
plt.grid()
plt.legend()
plt.show()
