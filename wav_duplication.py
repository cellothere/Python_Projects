#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 09:49:52 2023

@author: paulbergeron
"""


import wave

good_morning = wave.open('/Users/paulbergeron/Desktop/good-morning.wav', 'rb')

print('No. of Channels', good_morning.getnchannels())
print('Sample width', good_morning.getsampwidth())
print('Frame rate', good_morning.getframerate())
print("No. of frames", good_morning.getnframes())
print("Parameters", good_morning.getparams())

audio_time = good_morning.getnframes() /  good_morning.getframerate()

print(audio_time, "seconds")

frames = good_morning.readframes(-1)

good_morning.close()

good_morning_new = wave.open('/Users/paulbergeron/Desktop/good-morning_new.wav', 'wb')

good_morning_new.setnchannels(1)
good_morning_new.setsampwidth(2)
good_morning_new.setframerate(48000.0)

good_morning_new.writeframes

good_morning_new.close()
