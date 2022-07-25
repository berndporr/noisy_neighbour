#!/usr/bin/python3
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy import signal
import ABC_weighting
import sys
import datetime
import leq_math
 
#    Daytime 07.00 - 19.00 hours L Aeq 41dB (31dB)
#    Evening 19.00 - 23.00 hours L Aeq 37dB (27dB)
#    Night-time 23.00 - 07.00 hours L Aeq 31dB (21dB)
#    In brackets if the noise level is below 21dB.
#    The parameter to be used is the L Aeq, 5min.
#    https://www.gov.scot/publications/antisocial-behaviour-etc-scotland-act-2004-guidance-noise-nuisance/pages/1/

chunk_duration = 10 # secs

f = wavfile.read("/tmp/ste-25jul_05_38_16kHz.wav")
fs = f[0]
y = f[1] / 32768.0
print("nsamples in recording =",len(y))
chunk = fs * chunk_duration
print("nsamples in a chunk of {} secs = {}".format(chunk_duration,chunk))

customdate = datetime.datetime(2022, 7, 25, 5, 38, 30)
t = "L_Aeq - "+customdate.strftime("%c")

ts = []
dbs = []

for i in range(len(y)//chunk - 1):
    db = leq_math.Leq(y[i*chunk:(i+1)*chunk],fs)
    print(customdate,":",db,"L_Aeq")
    ts.append(customdate)
    dbs.append(db)
    customdate = customdate + datetime.timedelta(seconds=chunk/fs)

plt.figure(t)
plt.title(t)
plt.plot(ts,dbs,label="L_Aeq(db)")
plt.plot(ts,np.ones(len(ts))*31,label="permitted noise level (db)")
plt.xlabel("Date/time")
plt.ylabel("L_Aeq (db)")
plt.ylim([20,60])
plt.legend()

plt.show()
