# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:28:54 2017


find the rms noise in the signal
@author: User
"""


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
    VoltsOLD = []
    global AverageWaveform; AverageWaveform = []
    global PeakList; PeakList = []
    global Baseline; Baseline = []
    global Rows; Rows     = 5000
    global BaselineRMS; BaselineRMS = []
    global p3; p3 = 2500;
    global p4; p4 = 3500;
     #number of data points
    BaselineLength = 1800

    xmldoc   = minidom.parse("%s" %filename)
    
    # Loop over and add all the arrays to variable Volts
    for j in range(0,Rows):   
        VoltsOLD = xmldoc.getElementsByTagName("trace")[j].firstChild.data # grabs the data in the trace domain
        VoltsOLD = VoltsOLD.split()
        
        if (j==1671):
            Baseline.append(0);
            continue;
        
        
        for i in range(len(VoltsOLD)):
            VoltsOLD[i] = float(VoltsOLD[i]) #Convert to a float
        
        " Subtract The Baseline"    
        Baseline.append(sum(VoltsOLD[0:BaselineLength])/BaselineLength)  
        VoltsOLD    = np.array(VoltsOLD) - Baseline[j]
        
        VoltsOLD = savgol_filter(VoltsOLD,11,1)
        
        "Store the peak into a list"
        PeakList.append(VoltsOLD);
        
        "Make an array for the baseline RMS"
        for k in range(p3,p4):
            BaselineRMS.append(VoltsOLD[k]);
                                       
        print (j);
        
    AverageWaveform = [sum(x) for x in zip(*PeakList)]                  
    AverageWaveform = np.array(AverageWaveform)/Rows   # average waveform
    
    return 0;

"Take input for the file name"
for i in range(8,9): 
    print(i)
    filename = "SIPMtwoX%i.xml" %i
    xmlread(filename)
#%%
for i in range(200,250): 
    plt.figure('%i' %(i+1))
    #plt.plot(PeakList[0][i],alpha = 0.25)
    #plt.plot(savgol_filter(PeakList[0][i],11,2))
    plt.plot(PeakList[i],alpha = 1)
    
    #plt.axis([1950, 2300, -3, 5])


#%%
histSplitting =200

'histogram ranges'
HistMin  = -15
HistMAX  = 15
BinWidth = (HistMAX - HistMin)/histSplitting
plt.figure()

'histogram'
(CountsData, bins2, bars ) = plt.hist(BaselineRMS, bins = np.arange( HistMin, HistMAX,BinWidth),
    alpha = 1.0,label='Data',color = 'k',histtype = 'step',linewidth=2.0)

plt.xlabel("ADC",weight = 'bold',fontsize=13) #xlabel
plt.ylabel("Counts",weight = 'bold',fontsize=13) #yabel   
plt.title("Custom Board 25 V LN2",weight = 'bold',fontsize=13)
axes = plt.gca()
axes.set_xlim([-11.5,11.5])  

'find the centroid of each bin '
bincentroid = []
midpoint = (bins2[15]- bins2[14])/2 #gives first midpoint
histSplitting = len(CountsData)
            
            
for k in range (0,histSplitting):
         bincentroid.append(midpoint +k*BinWidth)
        
bincentroid = np.array(bincentroid) 
bincentroid = bincentroid  + HistMin    

