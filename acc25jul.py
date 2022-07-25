#!/usr/bin/python3
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy import signal
import datetime

d = np.loadtxt("/tmp/nn_24_23_45.tsv")
a = int(5E6)
a1 = np.abs(d[a:,11])
a2 = np.abs(d[a:,12])
a3 = np.abs(d[a:,13])

fs = 250

customdate = datetime.datetime.fromtimestamp(1658702690)
x = [customdate + datetime.timedelta(seconds=(i+a)/fs) for i in range(len(a1))]

t = "Acceleration - "+customdate.strftime("%c")

print(t)

plt.figure(t)
plt.title(t)
plt.plot(x,a1)
plt.plot(x,a2)
plt.plot(x,a3)
plt.xlabel("Date/time")
plt.ylabel("acceleration m/s^2")
plt.show()
