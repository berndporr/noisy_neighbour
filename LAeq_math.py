#!/usr/bin/python3
import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import scipy
import numpy as np
from scipy import signal
import ABC_weighting
 
# Sound level measurement with a zoom recorder (mic gain "high").
# It's been calibrated by playing a 1kHz sine-wave at 88.6dB.
# The file ref_1khz_88_6_dB_zoom_high.wav contains the reference
# recording. The unit test checks that feeding that into
# Leq() actually then yields 88.6dB again.

weighting = "A"

# RMS calc
def rms(s):
    return np.sqrt(np.mean(np.absolute(s)**2))

# Calculates the A weighted RMS from my zoom recorder at 88.6dB
def zoom_norm_rms():
    fref = wavfile.read('ref_1khz_88_6_dB_zoom_high.wav');
    yref = fref[1] / 32768.0
    fs = fref[0]
    z, p, k =  ABC_weighting.get_zpk(weighting,fs)
    sos = signal.zpk2sos(z, p, k)
    yref = signal.sosfilt(sos,yref)
    return rms(yref[fs:])

# Calculates the reference value from the zoom recorder for 0dB.
def p0():
    return zoom_norm_rms() / np.power(10,88.6/20)

# Calculates Leq by weithing the zoom_wav against
# the 0dB value p0.
def Leq(zoom_wav,fs):
    z, p, k =  ABC_weighting.get_zpk(weighting,fs)
    sos = signal.zpk2sos(z, p, k)
    zoom_wav = signal.sosfilt(sos,zoom_wav)
    return 20 * np.log10(rms(zoom_wav[fs:])/p0())

# Unit test that the reference file ref_1khz_88_6_dB_zoom_high.wav
# actually yields 88.6dB as recorded.
if __name__ == '__main__':
    f2 = wavfile.read('ref_1khz_88_6_dB_zoom_high.wav');
    fs2 = f2[0]
    y2 = f2[1] / 32768.0
    db = Leq(y2,fs2)
    print("Sanity check: db of ref WAV =",db)
    if (db < 88) or (db > 89):
        raise ValueError("Reference dB out of range")
