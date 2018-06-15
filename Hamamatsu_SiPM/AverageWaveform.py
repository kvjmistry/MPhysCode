# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:33 2016

@author: User
"""

'Run this for the Histograms'


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
    global Positions; Positions = [];
    u = 0;
    p3       = 2015
    p4       = 2035
    Rows     = 1000
     #number of data points
    BaselineLength = 1900

    xmldoc   = minidom.parse("%s" %filename)
    
    # Loop over and add all the arrays to variable Volts
    for j in range(0,Rows):   
        VoltsOLD = xmldoc.getElementsByTagName("trace")[j].firstChild.data # grabs the data in the trace domain
        VoltsOLD = VoltsOLD.split()
        
        for i in range(len(VoltsOLD)):
            VoltsOLD[i] = float(VoltsOLD[i])
        
        if (j==9427):
            Baseline.append(0);
            continue;
            
        Baseline.append(sum(VoltsOLD[0:BaselineLength])/BaselineLength)  
        VoltsOLD    = np.array(VoltsOLD) - Baseline[j]
        
        Baseline2 = sum(VoltsOLD[0:BaselineLength])/BaselineLength  
        VoltsOLD    = VoltsOLD - Baseline2
      
        VoltsNew = VoltsOLD
        VoltsNew = savgol_filter(VoltsOLD,31,3)
        
        "Store the peak into a list"
        PeakList.append(VoltsNew)
       
        'find the max peak of the array via mean method' 
        PeakMax.append(np.max(VoltsNew[p3:p4]) )
        Positions.append(np.argmax(VoltsNew[p3:p4]))
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

for i in range(4,5): 
    print('%i =' %i) 
    filename = "SIPMthreeW%i.xml" %i
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
#plt.legend(loc='best')
plt.xlabel("Time (ns)",weight = 'bold', fontsize = 13) #xlabel
plt.ylabel("ADC",weight = 'bold', fontsize = 13) #yabel   
plt.title("Hamamatsu",weight = 'bold', fontsize = 13)
plt.show()

#%%
for i in range(0,50): 
    plt.figure('%i' %(i+1))
    plt.plot(PeakList[0][i],alpha = 1)
    #plt.plot(savgol_filter(PeakList[0][i],11,2))
    
   
#%% 
# old histsplit = 500
histSplitting = 100
t=0

'histogram ranges'
HistMin  = min(PeakMaxList[t])
HistMAX  = max(PeakMaxList[t])
BinWidth = (HistMAX - HistMin)/histSplitting
plt.figure()

'histogram'
(CountsData, bins2, bars ) = plt.hist(PeakMaxList[t], bins = np.arange( HistMin, HistMAX,BinWidth),
    alpha = 1.0,label='Data',color = 'k',histtype = 'step')

plt.xlabel("ADC",weight = 'bold', fontsize = 13) #xlabel
plt.ylabel("Counts",weight = 'bold', fontsize = 13) #yabel   
plt.title("53 V (high intensity)",weight = 'bold', fontsize = 13)        

'find the centroid of each bin '
bincentroid = []
midpoint = (bins2[15]- bins2[14])/2 #gives first midpoint
histSplitting = len(CountsData)
            
            
for k in range (0,histSplitting):
         bincentroid.append(midpoint +k*BinWidth)
        
bincentroid = np.array(bincentroid) 
bincentroid = bincentroid  + HistMin  


  