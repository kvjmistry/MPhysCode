# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:33 2016

@author: User
"""

'File that reads in 5 data sets and plots them on the same graph'


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
'function to read in all the data'
def xmlread(filename):
    PeakMax =[]
    VoltsOLD = []
    AverageWaveform = []
    PeakList = []
    Baseline = []
    Baseline2 = []
    tempmax = [];
    u = 0;
    
    p3       = 2000
    p4       = 2400
    Rows     = 50
     #number of data points
    BaselineLength = 1000

    xmldoc   = minidom.parse("%s" %filename)
    
    # Loop over and add all the arrays to variable Volts
    for j in range(0,Rows):   
        if (j == 1970 or j== 4479): 
            Baseline.append(0); 
            continue;
        
        VoltsOLD = xmldoc.getElementsByTagName("trace")[j].firstChild.data # grabs the data in the trace domain
        VoltsOLD = VoltsOLD.split()
               
        for i in range(len(VoltsOLD)):
            VoltsOLD[i] = float(VoltsOLD[i])
        
            
           
        " Subtract The Baseline"    
        Baseline.append(sum(VoltsOLD[0:BaselineLength])/BaselineLength)  
        VoltsOLD    = np.array(VoltsOLD) - Baseline[j]
        
        Baseline2 = sum(VoltsOLD[0:BaselineLength])/BaselineLength  
        VoltsOLD    = VoltsOLD - Baseline2
        

        VoltsNew = VoltsOLD
        VoltsNew = savgol_filter(VoltsOLD,55,2)
        
               
        "Store the peak into a list"
        PeakList.append(VoltsNew)
       
        'Take local average before the peak to subtract from the max peak'
        for r in range (5,6): 
            tempmax.append(VoltsNew[np.argmax(VoltsNew[p3:p4])-r]); # take max in range p3:p4 and take a mean of the 10 values before that       
        u = np.mean(tempmax);
        
        u = np.mean(VoltsNew[1970:1980])
 
        'find the max peak of the array via mean method' 
        PeakMax.append(np.max(VoltsNew[p3:p4]) - 0 )
        
        print (j)
        
    AverageWaveform = [sum(x) for x in zip(*PeakList)]                  
    AverageWaveform = np.array(AverageWaveform)/Rows   # average waveform
    
    temp.append(PeakMax)
    temp.append(Baseline)
    temp.append(PeakList)
    temp.append(AverageWaveform)
    return temp
 
temp = []
PeakList = []
BaselineList = []    
PeakMaxList = []    
AverageWaveformList = []

for i in range(1,2): 
    print(i)
    filename = "SIPMoneW%i.xml" %i
    temp = xmlread(filename)
    PeakList.append(temp[2])
    BaselineList.append(temp[1])
    PeakMaxList.append(temp[0])
    AverageWaveformList.append(temp[3])   
    temp = []

plt.figure()
cmap = plt.get_cmap('brg')
colors = [cmap(i) for i in np.linspace(0, 1, len(AverageWaveformList))]
        
          
label = ['CAEN Power Supply','Tenma Power Supply','29V','30V','50 v','60v']          
          
for i, color in enumerate(colors, start=0):
    plt.plot(AverageWaveformList[i], color=color, label=label[i])
plt.legend(loc='best')
plt.show()

#%%
for i in range(200,250): 
    plt.figure('%i' %(i+1))
    #plt.plot(PeakList[0][i],alpha = 0.25)
    #plt.plot(savgol_filter(PeakList[0][i],11,2))
    
    for j in range(0,5,4000):
      plt.plot(PeakList[0][i],alpha = 0.5)
    
    
    plt.plot(savgol_filter(PeakList[0][i],37,2))
    plt.axis([1950, 2300, -3, 5])
    plt.savefig('Desktop.png', format='png', dpi=1200)


   
#%% 
histSplitting =150
t=0

'histogram ranges'
HistMin  = min(PeakMaxList[t])
HistMAX  = max(PeakMaxList[t])
BinWidth = (HistMAX - HistMin)/histSplitting
plt.figure()

'histogram'
(CountsData, bins2, bars ) = plt.hist(PeakMaxList[t], bins = np.arange( HistMin, HistMAX,BinWidth),
    alpha = 1.0,label='Data',color = 'k', histtype = 'step')

plt.xlabel("ADC",weight = 'bold',fontsize = 13) #xlabel
plt.ylabel("Counts",weight = 'bold',fontsize = 13) #yabel   
plt.title("Commercial 29 V",weight = 'bold',fontsize = 13)        
axes = plt.gca()
axes.set_xlim([-1,8])  

'find the centroid of each bin '
bincentroid = []
midpoint = (bins2[15]- bins2[14])/2 #gives first midpoint
histSplitting = len(CountsData)
            
            
for k in range (0,histSplitting):
         bincentroid.append(midpoint +k*BinWidth)
        
bincentroid = np.array(bincentroid) 
bincentroid = bincentroid  + HistMin  

        
  
#%% 

'Fourier Analysis'
plt.figure("FFT")
p = 0
n = len(AverageWaveformList[p]) # total number of samples
ww = n/2 # width of the window for the plots        
samplingrate = 1e9

FFT = np.fft.fft(AverageWaveformList[p]) # FFT
FFT = np.fft.fft(PeakList[0][0])
freq = np.fft.fftfreq(n)*samplingrate # Frequency Bins


label = ['M10 LED 3.2V','M11 LED 3.3V','M12 LED 3.4V','M13 LED 3.5V',]

plt.plot(freq[range(int(ww))], abs(FFT[range(int(ww))])/n,label = label[p])
plt.rcParams.update({'font.size': 15,'font.weight':'bold'})


