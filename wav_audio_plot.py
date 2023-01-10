#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:40:48 2023

@author: paulbergeron
"""

import wave

from scipy.io import wavfile

from IPython.display import Audio

from matplotlib import pyplot as plt

good_morning = "/Users/paulbergeron/Desktop/good-morning.wav"
fs, wav = wavfile.read(good_morning)

print(wav)
plt.plot(wav)

obj = wave.open("/Users/paulbergeron/Desktop/good-morning.wav", 'rb')