print("your audio would be registered ,so please be closer and clear to mic")
import pyaudio
import wave
import os
import time
from scipy.io import wavfile
from matplotlib import pyplot as plt
import numpy as np
id=int(input("enter your id that was given for face dataset"))
print("Tell your secret word")
os.mkdir(r'datasetadad/'+str(id))
CHUNK = 2048
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000
RECORD_SECONDS = 3
for i in range(8):
    
    WAVE_OUTPUT_FILENAME ='usradip.'+str(i+1)+'.wav'

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("take ",i+1)
    
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
    
os.rename('usradip.1.wav','datasetad/'+str(id)+'/usradip.1.wav')
os.rename('usradip.2.wav','datasetad/'+str(id)+'/usradip.2.wav')
os.rename('usradip.3.wav','datasetad/'+str(id)+'/usradip.3.wav')
os.rename('usradip.4.wav','datasetad/'+str(id)+'/usradip.4.wav')
os.rename('usradip.5.wav','datasetad/'+str(id)+'/usradip.5.wav')
os.rename('usradip.6.wav','datasetad/'+str(id)+'/usradip.6.wav')
os.rename('usradip.7.wav','datasetad/'+str(id)+'/usradip.7.wav')
os.rename('usradip.8.wav','datasetad/'+str(id)+'/usradip.8.wav')

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
    if(data1[j]==data2[j]):
       a+=1
k.append(a)
a=0
for j in range(len(data1)):
    if(data1[j]==data3[j]):
       a+=1
k.append(a)
a=0
for j in range(len(data1)):
    if(data1[j]==data4[j]):
       a+=1
k.append(a)
a=0
for j in range(len(data1)):
    if(data1[j]==data5[j]):
       a+=1
k.append(a)
a=0
for j in range(len(data1)):
    if(data1[j]==data6[j]):
       a+=1
k.append(a)
a=0
for j in range(len(data1)):
    if(data1[j]==data7[j]):
       a+=1
k.append(a)
a=0
for j in range(len(data1)):
    if(data1[j]==data8[j]):
       a+=1
k.append(a)
a=0
for i in range(len(k)):
    a=a+k[i]
a=a/len(k)
file=open('datasetad/'+str(id)+'/output.txt','w')
file.write(str(a))
file.close()
print("thank you for registration ,please remeber your magical word")
