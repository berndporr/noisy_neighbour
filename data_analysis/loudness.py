#!/usr/bin/python3
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy import signal
import datetime

def detthuds(fs,customdate,y):
    thudno = 1
    cooloff = 0
    for i in range(len(y)):
        if (y[i] > 0.1) and (cooloff < 1):
           x = customdate + datetime.timedelta(seconds=i/fs)
           print("Thud #{} at {}".format(thudno,x))
           thudno = thudno + 1
           cooloff = fs
        if cooloff > 0:
            cooloff = cooloff - 1


f = wavfile.read('STE-038_2_27_5jul_500Hz.wav');
fs = f[0]
y = f[1] / 32768.0

y = np.abs(y)

customdate = datetime.datetime(2022, 7, 5, 2, 27)
x = [customdate + datetime.timedelta(seconds=i/fs) for i in range(len(y))]

t = "Loudness - 5 July from 2:27"

print(t)
detthuds(fs,customdate,y)

plt.figure(t)
plt.title(t)
plt.plot(x,y)
plt.xlabel("Date/time")
plt.ylabel("Loudness (Zoom H4, sens high)")
plt.ylim([0,1])


print("----------------------------")


########################################################

f = wavfile.read('STE-039_4_38_5jul_500Hz.wav');
fs = f[0]
y = f[1] / 32768.0

y = np.abs(y)

customdate = datetime.datetime(2022, 7, 5, 4, 38)
x = [customdate + datetime.timedelta(seconds=i/fs) for i in range(len(y))]

t = "Loudness - 5 July from 4:38"
print(t)
detthuds(fs,customdate,y)

plt.figure(t)
plt.title(t)
plt.plot(x,y)
plt.xlabel("Date/time")
plt.ylabel("Loudness (Zoom H4, sens high)")
plt.ylim([0,1])



##################################################


f = wavfile.read('STE_5_jul_23_49_500Hz.wav');
fs = f[0]
y = f[1] / 32768.0

y = np.abs(y)

customdate = datetime.datetime(2022, 7, 5, 23, 49)
x = [customdate + datetime.timedelta(seconds=i/fs) for i in range(len(y))]

t = "Loudness - 5 July from 23:49"
print(t)
detthuds(fs,customdate,y)

plt.figure(t)
plt.title(t)
plt.plot(x,y)
plt.xlabel("Date/time")
plt.ylabel("Loudness (Zoom H4, sens high)")
plt.ylim([0,1])







plt.show()
