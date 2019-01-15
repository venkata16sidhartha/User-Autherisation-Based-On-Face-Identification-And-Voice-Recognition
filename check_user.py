import pyaudio
import wave
import os
import time
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
id=int(input("enter your id"))
print("Tell your secret word")
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 3
WAVE_OUTPUT_FILENAME ='test'+'.wav'

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
    
print("* recording...")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
    
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)    
wf.writeframes(b''.join(frames))
wf.close()

import os

files = folders = 0

for _, dirnames, filenames in os.walk('datasetad'):
    folders += len(dirnames)

os.rename('test.wav','datasetad/'+str(id)+'/test.wav')
for m in range(folders):
    samplerate, datat = wavfile.read('datasetad/'+str(id)+'/test.wav')
    samplerate, data1 = wavfile.read('datasetad/'+str(id)+'/usradip.1.wav')
    samplerate, data2 = wavfile.read('datasetad/'+str(id)+'/usradip.2.wav')
    samplerate, data3 = wavfile.read('datasetad/'+str(id)+'/usradip.3.wav')
    samplerate, data4 = wavfile.read('datasetad/'+str(id)+'/usradip.4.wav')
    samplerate, data5 = wavfile.read('datasetad/'+str(id)+'/usradip.5.wav')
    samplerate, data6 = wavfile.read('datasetad/'+str(id)+'/usradip.6.wav')
    samplerate, data7 = wavfile.read('datasetad/'+str(id)+'/usradip.7.wav')
    samplerate, data8 = wavfile.read('datasetad/'+str(id)+'/usradip.8.wav')
    k=[]
    a=0
    for j in range(len(data1)):
        if(datat[j]==data2[j]):
           a+=1
    k.append(a)
    a=0
    for j in range(len(data1)):
        if(datat[j]==data3[j]):
           a+=1
    k.append(a)
    a=0
    for j in range(len(data1)):
        if(datat[j]==data4[j]):
           a+=1
    k.append(a)
    a=0
    for j in range(len(data1)):
        if(datat[j]==data5[j]):
           a+=1
    k.append(a)
    a=0
    for j in range(len(data1)):
        if(datat[j]==data6[j]):
           a+=1
    k.append(a)
    a=0
    for j in range(len(data1)):
        if(datat[j]==data7[j]):
           a+=1
    k.append(a)
    a=0
    for j in range(len(data1)):
        if(datat[j]==data8[j]):
           a+=1
    k.append(a)
    a=0
    for i in range(len(k)):
        a=a+k[i]
    a=a/len(k)
file=open('datasetad/'+str(id)+'/output.txt','r')
l=file.read()
file.close()
print(l,a)
if(l<=str(a+5) or l<=str(a-5)):
    print("Congratulations you are verified")
else:
    print("sorry plz try again")
os.remove('datasetad/'+str(id)+'/test.wav')
    
