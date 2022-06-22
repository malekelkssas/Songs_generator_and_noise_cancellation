import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft

# Milestone_1

𝑡 = np. linspace(0 ,3, 12*1024)
freq = [146.83*3,261.63*3,246.93*3,220*3,246.93*3,261.63*3,261.63*3,246.93*3,220*3,246.93*3]
timest =[0,0.5,0.8,1.1,1.4,1.7,2,2.3,2.6,2.8]
timend =[0.4,0.7,1,1.3,1.6,1.9,2.2,2.5,2.8,3]
y=0
for i in range(10):
   y+=np.where(np.logical_and(t>=timest[i],t<=timend[i]),np.sin(t*np.pi*2*freq[i]),0)
plt.plot(t, y)
#sd.play(y, 3*1024)   the song before adding the noises

# ______________________________________________________________
# Milestone_2

N = 3*1024  # number of samples per seconds 
f = np.linspace(0, 512, int(N/2))   #set freq range
xfour = fft(y)              # convert to freq domain using fouri
xfour = 2/N * np.abs(xfour[0:int(N/2)])
f1 = np.random.randint(0,512)   #ranom frq for noise
f2 = np.random.randint(0,512)
n = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)   #noise add
xn = y+n


xnfour = fft(xn)    # freq domain result seignals
xnfour = 2/N * np.abs(xnfour[0:int(N/2)])

randomnoise = np.where(xnfour >np.ceil(np.max(y)))
peek1 = randomnoise[0][0]
peek2 = randomnoise[0][1]

var = np.sin(2*np.pi*int(f[peek1])*t)+np.sin(2*np.pi*int(f[peek2])*t)
filte =xn - var

sd.play(filte, 3*1024)

filtefour = fft(filte)
filtefour = 2/N * np.abs(filtefour[0:int(N/2)])

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, y)
plt.subplot(3, 1, 2)
plt.plot(t, xn)
plt.subplot(3, 1, 3)
plt.plot(t, filte)

plt.figure()
plt.subplot(3, 1, 1)
plt.plot(f, xfour)
plt.subplot(3, 1, 2)
plt.plot(f, xnfour)
plt.subplot(3, 1, 3)
plt.plot(f, filtefour)




