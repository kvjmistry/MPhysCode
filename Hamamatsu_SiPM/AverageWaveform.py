# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 16:18:33 2016
Last Updated: 23/06/18

@author: kmistry
This script will be used to analyse the Hammamatsu SiPM Waveforms
and produce a plot of the single photoelectron response. 

"""
#*****************************************************************************************************
# Import Library
from xml.dom import minidom     # For parsing an xml file input
import matplotlib.pyplot as plt # Plottting Software
import numpy as np              # For data analysis
from scipy.optimize import curve_fit # For curve fitting
from scipy.signal import savgol_filter
import matplotlib.patches as mpatches

# Set some default plot parameters. 
plt.rcParams['axes.linewidth'] = 3                # Sets the boarder width 
plt.rcParams.update({'errorbar.capsize': 1.2})    # Gives a cap to the errorbars
plt.rcParams["font.size"] = 20                    # Sets all font sizes to bold
plt.rcParams["lines.markersize"] = 4              
plt.rcParams["grid.linestyle"] = "--"             # Adds a grid to the plots
plt.rcParams['figure.figsize'] = 8, 8             # Sets the figure size


#%%
#*****************************************************************************************************
'Function that reads the xml file and appends its data to a list'
def xmlread(filename):
    # Define arrays
    PeakMax = [] # Array containing the peak maximum values in the region of interest
    Data = []    
    AverageWaveform = [] 
    EventList = [] # Array containing the events
    Baseline = []  # Array containing the initial baseline
    Baseline2 = [] # Array containing the second baseline
    PeakTime = []  # Array containing the time of the max peak
    
    ROI_Start       = 2015 # Start time of Region of Interest (ROI) [ns]
    ROI_End         = 2035
    NumEvents       = 1000 # The total number of events 
     
    # Define the length of the baseline before trigger
    BaselineLength = 1900

    xmldoc   = minidom.parse("%s" %filename) # Load the file
    
    # Loop over all events and add all the arrays to variable Data
    for j in range(0,NumEvents):   
        Data = xmldoc.getElementsByTagName("trace")[j].firstChild.data # Grabs the data in the trace domain of the xml
        Data = Data.split() # Splits the list into individual elements in a list
        
        # Loop over the data and convert its members to a float
        for i in range(len(Data)):
            Data[i] = float(Data[i])
        
        # Insert condition to ignore corrupt data files. 
        'HARDCODED and file dependent'
        if (j==9427):
            Baseline.append(0) # Keeps the baseline list the same size. 
            continue
            
        Baseline.append(sum(Data[0:BaselineLength])/BaselineLength) # Average the baseline and append
        Data    = np.array(Data) - Baseline[j]                      # Subtract the baseline from the data
        
        Baseline2 = sum(Data[0:BaselineLength])/BaselineLength      # Repeat baseline subtraction
        Data    = Data - Baseline2
      
        SGFilteredData = Data                       # Copy the data
        SGFilteredData = savgol_filter(Data,31,3)   # Filter the data with the SG Filter
        
        # Store the SG Filtered event into a list
        EventList.append(SGFilteredData)
       
        # Find the maximum of the peak in the specified region of interest
        PeakMax.append(np.max(SGFilteredData[ ROI_Start : ROI_End]) )
        PeakTime.append(np.argmax(SGFilteredData[ ROI_Start : ROI_End] )) # Time stamp of Max Peak
        print (j) # Display the event number

    # Average every event to get an average SiPM Signal    
    AverageWaveform = [sum(x) for x in zip(*EventList)]                  
    AverageWaveform = np.array(AverageWaveform)/NumEvents   
    
    # Push back each array to a temporary list to be returned by the function
    temp.append(PeakMax)
    temp.append(Baseline)
    temp.append(EventList)
    temp.append(AverageWaveform)
    temp.append(PeakTime)
    return temp
 #*****************************************************************************************************
'Begining of Main Function'
# Create arrays 
temp = []
EventList = []
BaselineList = []    
PeakMaxList = []    
AverageWaveformList = []
PeakTimeList = []

# Loop over file lists in directory.
for i in range(4,5): 
    print('%i =' %i) 
    filename = "SIPMthreeW%i.xml" %i
    
    # Call xmlread function to read the data in.
    temp = xmlread(filename)

    # Fill the lists with the data
    PeakMaxList.append(temp[0])
    BaselineList.append(temp[1])
    EventList.append(temp[2])
    AverageWaveformList.append(temp[3]) 
    PeakTimeList.append(temp[4])  
    temp = []

#*****************************************************************************************************
'Make a plot of the average waveform for each file loaded.'
'Colour each average waveform with a colour map'
plt.figure()
cmap = plt.get_cmap('brg')
colors = [cmap(i) for i in np.linspace(0, 1, len(AverageWaveformList))]
           
label = ['50 V','55 V'] # Add labels to waveforms for legend       

# Make the Plot          
for i, color in enumerate(colors, start=0):
    plt.plot(AverageWaveformList[i], color=color, label=label[i])

# Plot customisation
#plt.legend(loc='best')
plt.xlabel("Time [ns]") # xlabel
plt.ylabel("ADC")       # yabel   
plt.title("Hamamatsu")
plt.show()

#*****************************************************************************************************
# Plot N Events on the same plot with option to include another SG Filter on the data.
for i in range(0,50): 
    plt.figure('%i' %(i+1))
    plt.plot(EventList[0][i],alpha = 1)
    #plt.plot(savgol_filter(EventList[0][i],11,2))
    
#*****************************************************************************************************   
#%% 
# Create a histogram of the Peak Maximum List
histSplitting = 100 # Varibae to determine the bin sizes
t=0                 

# Get the histogram ranges
HistMin  = min(PeakMaxList[t])
HistMAX  = max(PeakMaxList[t])
BinWidth = (HistMAX - HistMin)/histSplitting # Define the bin width 

plt.figure() # Create a new figure

# Make the Histogram
(BinValue, BinEdge, Patches ) = plt.hist(PeakMaxList[t], bins = np.arange( HistMin, HistMAX, BinWidth),
    alpha = 1.0, label='Data', color = 'k', histtype = 'step')

# Histogram Customisation
plt.xlabel("ADC")       # x Label
plt.ylabel("Counts")    # y Label   
plt.title("53 V (high intensity)",weight = 'bold', fontsize = 13)        

# Get the centroid of each bin rather than the edges
bincentroid = []
midpoint = (BinEdge[15]- BinEdge[14])/2 # Gives the midpoint displacement
histSplitting = len(BinValue)
                
for k in range (0,histSplitting):
    bincentroid.append(midpoint + k * BinWidth)
        
bincentroid = np.array(bincentroid)  # Covert list to a np array 
bincentroid = bincentroid  + HistMin # Shift array to beggining of histogram

#******************************************* **END SCRIPT** ************************************************