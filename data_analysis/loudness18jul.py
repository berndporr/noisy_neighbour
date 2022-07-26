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
        if (y[i] > 0.06) and (cooloff < 1):
           x = customdate + datetime.timedelta(seconds=i/fs)
           print("Thud #{} at {}".format(thudno,x))
           thudno = thudno + 1
           cooloff = fs
        if cooloff > 0:
            cooloff = cooloff - 1


f = wavfile.read('STE-18jul_6_54am_500hz.wav');
fs = f[0]
y = f[1] / 32768.0

y = np.abs(y)

customdate = datetime.datetime(2022, 7, 18, 6, 54)
x = [customdate + datetime.timedelta(seconds=i/fs) for i in range(len(y))]

t = "Loudness - "+customdate.strftime("%c")

print(t)
detthuds(fs,customdate,y)

plt.figure(t)
plt.title(t)
plt.plot(x,y)
plt.xlabel("Date/time")
plt.ylabel("Loudness (Zoom H4, sens high)")
plt.ylim([0,1])

plt.show()
