import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy import signal
import datetime

f = wavfile.read('STE-038_2_27_5jul_500Hz.wav');
fs = f[0]
print("Sampling rate is=",fs)
y = f[1] / 32768.0

y = np.abs(y)

customdate = datetime.datetime(2022, 7, 5, 2, 27)
x = [customdate + datetime.timedelta(seconds=i/fs) for i in range(len(y))]

plt.figure("Loudness, 5 July from 2:27")
plt.title("Loudness, 5 July from 2:27")
plt.plot(x,y)
plt.xlabel("Date/time")
plt.ylabel("Loudness (Zoom H4, sens high)")
plt.ylim([0,1])




########################################################

f = wavfile.read('STE-039_4_38_5jul_500Hz.wav');
fs = f[0]
print("Sampling rate is=",fs)
y = f[1] / 32768.0

y = np.abs(y)

customdate = datetime.datetime(2022, 7, 5, 4, 38)
x = [customdate + datetime.timedelta(seconds=i/fs) for i in range(len(y))]

plt.figure("Loudness, 5 July from 4:38")
plt.title("Loudness, 5 July from 4:38")
plt.plot(x,y)
plt.xlabel("Date/time")
plt.ylabel("Loudness (Zoom H4, sens high)")
plt.ylim([0,1])








plt.show()
