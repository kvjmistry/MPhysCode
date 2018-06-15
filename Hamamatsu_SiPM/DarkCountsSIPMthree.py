# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:33 2016

@author: User
"""

'File that reads in 5 data sets and plots them on the same graph'


'Note run this one to gert the histogram out!'


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
    DarkCount = []
    PeakList = []
    Baseline = []
    Baseline2 = []
    tempmax = [];
    u = 0;
    p3       = 0
    p4       = 500

    Rows     = 10000
     #number of data points
    BaselineLength = 1950

    xmldoc   = minidom.parse("%s" %filename)
    
    # Loop over and add all the arrays to variable Volts
    for j in range(0,Rows):   
        VoltsOLD = xmldoc.getElementsByTagName("trace")[j].firstChild.data # grabs the data in the trace domain
        VoltsOLD = VoltsOLD.split()
        
        if (j == 2424 or j == 2425 or j == 7875 or j==9427 or j==896): 
            Baseline.append(0); 
            continue;

        for i in range(len(VoltsOLD)):
            VoltsOLD[i] = float(VoltsOLD[i])
   
        " Subtract The Baseline"    
        Baseline.append(sum(VoltsOLD[0:BaselineLength])/BaselineLength)  
        VoltsOLD    = np.array(VoltsOLD) - Baseline[j]
        
        Baseline2 = sum(VoltsOLD[0:BaselineLength])/BaselineLength  
        VoltsOLD    = VoltsOLD - Baseline2
        
        VoltsNew = VoltsOLD
        VoltsNew = savgol_filter(VoltsOLD,17,1)
        
        "Store the peak into a list"
        PeakList.append(VoltsNew)
     
        
        
        '''
        PeakMax.append(np.max(VoltsNew[0:300]))
        PeakMax.append(np.max(VoltsNew[300:600]))
        PeakMax.append(np.max(VoltsNew[600:900]))
        PeakMax.append(np.max(VoltsNew[900:1200]))
        PeakMax.append(np.max(VoltsNew[1200:1500]))
        PeakMax.append(np.max(VoltsNew[1800:2100]))
        PeakMax.append(np.max(VoltsNew[2400:2700]))
        PeakMax.append(np.max(VoltsNew[2700:3000]))
        PeakMax.append(np.max(VoltsNew[3000:3300]))
        PeakMax.append(np.max(VoltsNew[3300:3600]))
        PeakMax.append(np.max(VoltsNew[3600:3900]))
        'find the max peak of the array via mean method' 
        
        '''
        h = 0 
        for h in range (60,3950,11):   
            if ((VoltsNew[h]-VoltsNew[h-13]) >3.0) and (VoltsNew[h+30]>1):
                #h=10 & >2 for SIPMthree
                u = sum(VoltsNew[h-60:h-30])/30
                'find the max peak of the array via mean method' 
                #PeakMax.append(np.max(VoltsNew[p3:p4]) - u )
                PeakMax.append(np.max(VoltsNew[h:h+20])- u )
                #DarkCount.append(VoltsNew[h-9:h+40])
                
                
          
            


        print (j)
        
    AverageWaveform = [sum(x) for x in zip(*PeakList)]                  
    AverageWaveform = np.array(AverageWaveform)/Rows   # average waveform
    
    temp.append(PeakMax)
    temp.append(Baseline)
    temp.append(PeakList)
    temp.append(AverageWaveform)
    temp.append(DarkCount)
    return temp
 
temp = []
PeakList = []
BaselineList = []    
PeakMaxList = []    
AverageWaveformList = []
DarkCountList = []

for i in range(6,7): 
    print('%i =' %i) 
    filename = "SIPMthreeW%i.xml"  %i  
    temp = xmlread(filename)
    PeakList.append(temp[2])
    BaselineList.append(temp[1])
    PeakMaxList.append(temp[0])
    AverageWaveformList.append(temp[3]) 
    DarkCountList.append(temp[4])
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
for i in range(0,10): 
    plt.figure('%i' %(i+1))
    #plt.plot(PeakList[0][i],alpha = 1,color = 'b', label = 'Data')
    plt.plot(savgol_filter(PeakList[0][i],123,1),color = 'g', label = 'S-G')
    #plt.plot(savgol_filter(PeakList[0][i],21,1),color = 'r')
    #plt.plot(savgol_filter(PeakList[0][i],11,1),color = 'y')
    
    for j in range(0,5,4000):
      plt.plot(PeakList[0][i],alpha = 1)
    
    
    #plt.plot(savgol_filter(PeakList[0][i],31,3))
    #plt.plot(AverageWaveformList[0])
    #plt.plot(2*AverageWaveformList[0])
    plt.axis([1000, 3000, -30, 100])
 
#%%

for i in range (0,len(DarkCountList)):
    if (1.10<DarkCountList[i]<1.16):
        plt.plot(DarkCountList[i])
        plt.show
       

   
#%% 
histSplitting = 300
t=0

'histogram ranges'
HistMin  = min(PeakMaxList[t])
HistMAX  = max(PeakMaxList[t])
BinWidth = (HistMAX - HistMin)/histSplitting
plt.figure()

'histogram'
(CountsData, bins2, bars ) = plt.hist(PeakMaxList[t], bins = np.arange( HistMin, HistMAX,BinWidth),
    alpha = 1.0,label='Data',color = 'k',histtype = 'step')

plt.xlabel("ADC",weight = 'bold') #xlabel
plt.ylabel("Counts",weight = 'bold') #yabel   
 
plt.title("54 V",weight = 'bold', fontsize = 13)


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
