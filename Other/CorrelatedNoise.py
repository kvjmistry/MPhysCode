# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:33 2016

@author: User
"""

'Run this for splitting the two correlated noise'


"Import Library"
from xml.dom import minidom
import matplotlib.pyplot as plt # Plottting Software
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
import matplotlib.patches as mpatches


font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 13}
plt.rc('font', **font)


#%%

VoltsOLD = []
AverageWaveform = []
PeakList1 = []
PeakList2 = []
Baseline = []
Rows     = 1000
BaselineLength = 1900

xmldoc   = minidom.parse("SIPMonetwo1.xml")

# Loop over and add all the arrays to variable Volts
for j in range(0,Rows):   
    VoltsOLD = xmldoc.getElementsByTagName("trace")[j].firstChild.data # grabs the data in the trace domain
    VoltsOLD = VoltsOLD.split()
    
    for i in range(len(VoltsOLD)):
        VoltsOLD[i] = float(VoltsOLD[i])
    
    if (j==999999):
        Baseline.append(0);
        continue;
        
    Baseline.append(sum(VoltsOLD[0:BaselineLength])/BaselineLength)  
    VoltsOLD    = np.array(VoltsOLD) - Baseline[j]
    
    VoltsNew = VoltsOLD
    
    print(j);
    
    "Store the peak into a list"
    
    if (j % 2 == 0 ):
        VoltsNew = savgol_filter(VoltsOLD,51,3)
        PeakList1.append(VoltsNew)    
    else:
        VoltsNew = savgol_filter(VoltsOLD,51,3) #custom
        #VoltsNew = savgol_filter(VoltsOLD,91,3) #hamamatsu
        PeakList2.append(VoltsNew)
    
   
AverageWaveform1 = [sum(x) for x in zip(*PeakList1)]                  
AverageWaveform1 = np.array(AverageWaveform1)/(Rows*2)   # average waveform

AverageWaveform2 = [sum(x) for x in zip(*PeakList2)]                  
AverageWaveform2 = np.array(AverageWaveform2)/(Rows*2)   # average waveform

plt.figure()      
plt.plot(AverageWaveform1,'k')          
plt.xlabel("Time (ns)",weight = 'bold', fontsize = 13) #xlabel
plt.ylabel("ADC",weight = 'bold', fontsize = 13) #yabel   
plt.title("Commercial",weight = 'bold', fontsize = 13)
plt.show()

plt.figure()      
plt.plot(AverageWaveform2,'k')          
plt.xlabel("Time (ns)",weight = 'bold', fontsize = 13) #xlabel
plt.ylabel("ADC",weight = 'bold', fontsize = 13) #yabel   
plt.title("Hamamatsu",weight = 'bold', fontsize = 13)
plt.show()



#%%
for i in range(46,47): 
    plt.figure('%i Com' %(i+1))
    #plt.plot(PeakList1[i],alpha = 1)
    plt.plot(PeakList1[i],alpha = 1)
    #plt.plot(savgol_filter(PeakList2[i],51,3),alpha = 0.75)
    
#%%
for i in range(46,47): 
    plt.figure('%i Cust' %(i+1))
    #plt.plot(PeakList1[i],alpha = 1)
    plt.plot(PeakList2[i],alpha = 1)
    #plt.plot(savgol_filter(PeakList2[i],51,3),alpha = 0.75)

#%%
'Fourier Analysis'
plt.figure()
n = len(AverageWaveform1) # total number of samples
ww = n/2                         # width of the window for the plots        
samplingrate = 1e9

FFT = np.fft.fft(AverageWaveform2) # FFT
FFT = np.fft.fft(PeakList2[0])
freq = np.fft.fftfreq(n)*samplingrate # Frequency Bins


#freq = freq/1e6;

label = ['Commercial','Custom','Hamamatsu']

plt.plot(freq[range(int(ww))]/1e6, abs(FFT[range(int(ww))])/n, label = label[2])
plt.xlabel("Frequency (MHz)",weight = 'bold', fontsize = 13) #xlabel
plt.ylabel("Weight",weight = 'bold', fontsize = 13)          #yabel   
plt.title("FFT",weight = 'bold', fontsize = 13)
axes = plt.gca()
axes.set_xlim([0,100])  
    
   


  