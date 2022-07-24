#!/usr/bin/python3
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy import signal
import ABC_weighting
 
#    Daytime 07.00 - 19.00 hours L Aeq 41dB (31dB)
#    Evening 19.00 - 23.00 hours L Aeq 37dB (27dB)
#    Night-time 23.00 - 07.00 hours L Aeq 31dB (21dB)
#    In brackets if the noise level is below 21dB.
#    The parameter to be used is the L Aeq, 5min.
# https://www.gov.scot/publications/antisocial-behaviour-etc-scotland-act-2004-guidance-noise-nuisance/pages/1/

weighting = "A"

def rms(s):
    return np.sqrt(np.mean(np.absolute(s)**2))

def zoom_norm_rms():
    fref = wavfile.read('ref_1khz_88_6_dB_zoom_high.wav');
    yref = fref[1] / 32768.0
    fs = fref[0]
    z, p, k =  ABC_weighting.get_zpk(weighting,fs)
    sos = signal.zpk2sos(z, p, k)
    yref = signal.sosfilt(sos,yref)
    return rms(yref[fs:])

def p0():
    return zoom_norm_rms() / np.power(10,88.6/20)

def Leq(zoom_wav,fs):
    z, p, k =  ABC_weighting.get_zpk(weighting,fs)
    sos = signal.zpk2sos(z, p, k)
    zoom_wav = signal.sosfilt(sos,zoom_wav)
    return 20 * np.log10(rms(zoom_wav[fs:])/p0())

# sanity check
if __name__ == '__main__':
    f2 = wavfile.read('ref_1khz_88_6_dB_zoom_high.wav');
    fs2 = f2[0]
    y2 = f2[1] / 32768.0
    db = Leq(y2,fs2)
    print("Sanity check: db of ref WAV =",db)
    if (db < 88) or (db > 89):
        raise ValueError("Reference dB out of range")
