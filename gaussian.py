# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:09:46 2018

@author: VP LAB
"""

from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt

window = signal.gaussian(51, std=7)
plt.plot(window)
plt.title(r"Gaussian window ($\sigma$=7)")
plt.ylabel("Amplitude")
plt.xlabel("Sample")


