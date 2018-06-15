# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:33 2016

@author: User
"""

'Run this for the histograms'


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
    AverageWaveformDS = [] #downsampled average waveform
    PeakList = []
    Baseline = []
    Downsample = [];
    DownsampleList = []; 
    temp2 = 0;   
    global s; s = 4; # downsample length and make it global to the code
    x= 0;
    global p3; p3       = 2010
    global p4; p4       = 2040
    Rows     = 10 #number of data points
    BaselineLength = 1900

    xmldoc   = minidom.parse("%s" %filename)
    
    # Loop over and add all the arrays to variable Volts
    for j in range(0,Rows):   
        if (j == 1970 or j == 4479 or j == 3486): 
            Baseline.append(0); 
            continue;
        
        VoltsOLD = xmldoc.getElementsByTagName("trace")[j].firstChild.data # grabs the data in the trace domain
        VoltsOLD = VoltsOLD.split()
        
        for i in range(len(VoltsOLD)):
            VoltsOLD[i] = float(VoltsOLD[i])
                 
        " Subtract The Baseline"    
        Baseline.append(sum(VoltsOLD[0:BaselineLength])/BaselineLength)  
        VoltsOLD    = np.array(VoltsOLD) - Baseline[j]
        
        'Choose to savgol filter the data'
        VoltsNew = VoltsOLD
        #VoltsNew = savgol_filter(VoltsOLD,37,2)
        
        "Store the peak into a list"
        PeakList.append(VoltsNew)
        
        'Downsample the data' 
        for i in range(0,len(VoltsNew),s):
            for k in range(0,s):
                if (s+i > len(VoltsNew)): # want to discard the last bin
                    print("")
                    break;
                temp2 += VoltsNew[i+k]
                   
            if x != 0: print("") # dont add to the array     
            Downsample.append(temp2/s); #averages samples in the bin
            temp2 = 0;
        
        'subtract the local baseline'  
        b = sum(Downsample[1970:1980])/(1980-1970)
        Downsample = np.array(Downsample) - b; 
        
        'Choose to savgol filter the downsampled data or not'
        #DownsampleList.append(savgol_filter(Downsample,37,2));
        DownsampleList.append(Downsample);
        PeakMax.append(np.max(Downsample[(p3/s):(p4/s)]))
        Downsample = []
         
        'find the max peak of the array via mean method' 
        #PeakMax.append(np.max(VoltsNew[p3:p4]))
        
        print (j)
        
    AverageWaveform = [sum(x) for x in zip(*PeakList)]                  
    AverageWaveform = np.array(AverageWaveform)/Rows   # average waveform
    
    AverageWaveformDS = [sum(x) for x in zip(*DownsampleList)]                  
    AverageWaveformDS = np.array(AverageWaveformDS)/Rows   # average waveform
    
    temp.append(PeakMax)
    temp.append(Baseline)
    temp.append(PeakList)
    temp.append(AverageWaveform)
    temp.append(DownsampleList)
    temp.append(AverageWaveformDS)
    return temp
 
temp = [];
PeakList = [];
BaselineList = [];    
PeakMaxList = [];    
AverageWaveformList = [];
DownsampleList = [];
AverageWaveformListDS = [];

for i in range(1,2): 
    print(i)
    filename = "SIPMoneW%i.xml" %i
    temp = xmlread(filename)
    PeakList.append(temp[2])
    BaselineList.append(temp[1])
    PeakMaxList.append(temp[0])
    AverageWaveformList.append(temp[3])   
    DownsampleList.append(temp[4])
    AverageWaveformListDS.append(temp[5]);
    temp = []

plt.figure()
cmap = plt.get_cmap('brg')
colors = [cmap(i) for i in np.linspace(0, 1, len(AverageWaveformList))]
        
          
label = ['Commercial Board','Commercial Board','29V','30V','50 v','60v']          
          
for i, color in enumerate(colors, start=0):
    plt.plot(AverageWaveformList[i], color=color, label=label[i])
#plt.legend(loc='best')
plt.xlabel("Time (ns)",weight = 'bold',fontsize = 13) #xlabel
plt.ylabel("ADC",weight = 'bold',fontsize = 13) #yabel   
plt.title("Commercial",weight = 'bold',fontsize = 13)   
plt.show()
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
plt.title("28 V (high intensity)",weight = 'bold',fontsize = 13)        
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
for i in range(6,7): 
    plt.figure('%i' %(i+1))
    plt.plot(PeakList[0][i],alpha = 1)
    plt.xlabel("Time (ns)",weight = 'bold',fontsize = 13) #xlabel
    plt.ylabel("ADC",weight = 'bold',fontsize = 13) #yabel   
    plt.title("Commercial",weight = 'bold',fontsize = 13)    
    #plt.plot(savgol_filter(PeakList[0][i],11,2))
  
    
    #plt.plot(savgol_filter(PeakList[0][i],55,2))
    plt.plot((AverageWaveformList[0]*0.8)/max(AverageWaveformList[0]),alpha = 0.5)
    plt.plot((AverageWaveformList[0]*0.8*2)/max(AverageWaveformList[0]),alpha = 0.5)
    plt.plot((AverageWaveformList[0]*0.8*3)/max(AverageWaveformList[0]),alpha = 0.5)
    plt.plot((AverageWaveformList[0]*0.8*4)/max(AverageWaveformList[0]),alpha = 0.5)
    plt.plot((AverageWaveformList[0]*0.8*5)/max(AverageWaveformList[0]),alpha = 0.5)
    plt.plot((AverageWaveformList[0]*0.8*6)/max(AverageWaveformList[0]),alpha = 0.5)
    #plt.axis([1950, 2300, -3, 5])
    plt.axis([1700, 2500, -3, 11])


#%% 
'Down Sample'
x = 0;
s = 5;  'Downsample length'
Downsample = [];
DownsampleList = []; 

for k in range(0,len(PeakList[0])):
    for i in range(0,len(PeakList[0][k]),s):
        for j in range(0,s):
            if (s+i > len(PeakList[0][k])): # want to discard the last bin
                break;
            temp += PeakList[0][k][i+j]
                
        if x != 0: print(" ") # dont add to the array     
        Downsample.append(temp/s); #averages samples in the bin
        temp = 0;
    
    'subtract the local baseline'  
    b = sum(Downsample[1970:1980])/(19800-1970)
    Downsample = np.array(Downsample) - b;      
    DownsampleList.append(Downsample);
    Downsample = [];
        

AverageWaveform = [sum(x) for x in zip(*DownsampleList)]                  
AverageWaveform = np.array(AverageWaveform)/1000   # average waveform

#%%

ax = np.arange(0,len(PeakList[0][0]),s)

for i in range(150,191): 
    plt.figure('%i' %(i+1))
    #plt.plot(PeakList[0][i],alpha = 0.25)
    #plt.plot(savgol_filter(PeakList[0][i],11,2))
    
    for j in range(0,5,4000):
      plt.plot(ax, DownsampleList[0][i],alpha =1)
      #plt.plot(savgol_filter(DownsampleList[i],11,2))
      #plt.plot(savgol_filter(DownsampleList[i],9,7))
    
    #plt.plot(savgol_filter(PeakList[0][i],37,2))
    #plt.plot(ax, AverageWaveformListDS[0]*0.68, alpha = 0.75)
    #plt.plot(ax, AverageWaveformListDS[0]*0.68*2, alpha = 0.75)
    #plt.plot(ax, AverageWaveformListDS[0]*0.68*3, alpha = 0.75)
    #plt.plot(2*AverageWaveformList[0])
    
    
    plt.plot(ax, (AverageWaveformListDS[0]*0.8)/max(AverageWaveformListDS[0]),alpha = 0.5)
    plt.plot(ax, (AverageWaveformListDS[0]*0.8*2)/max(AverageWaveformListDS[0]),alpha = 0.5)
    plt.plot(ax, (AverageWaveformListDS[0]*0.8*3)/max(AverageWaveformListDS[0]),alpha = 0.5)
    plt.plot(ax, (AverageWaveformListDS[0]*0.8*4)/max(AverageWaveformListDS[0]),alpha = 0.5)
    plt.plot(ax, (AverageWaveformListDS[0]*0.8*5)/max(AverageWaveformListDS[0]),alpha = 0.5)
    plt.plot(ax, (AverageWaveformListDS[0]*0.8*6)/max(AverageWaveformListDS[0]),alpha = 0.5)
    
    plt.axis([1700, 2500, -3, 11])


plt.figure('Average Waveform')
plt.plot(AverageWaveformListDS[0])




#%%

fig, ax = plt.subplots()
ax.plot(range(10))

font = {'family' : 'CMU Serif',
        'weight' : 'bold',
        'size'   : 10}
plt.rc('font', **font)

ax.set_title("Hello World")

#prop = fm.FontProperties(fname='/usr/share/fonts/truetype/groovygh.ttf')
#ax.set_title('This is some random font')

plt.show()

#
import matplotlib as mpl
mpl.rcParams.update(mpl.rcParamsDefault)



