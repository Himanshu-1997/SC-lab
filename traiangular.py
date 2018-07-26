# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:11:53 2018

@author: VP LAB
"""

from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt
window = signal.triang(51)
plt.plot(window)
plt.title("Triangular window")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

