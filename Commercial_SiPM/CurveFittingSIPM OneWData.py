#%%

'SIPM One'
'Curve fitting input code'
'Uses the Lmfit module to fit the data'

from NewFitAll import NewFit  # 1 Gaussian
from NewFitAll import NewFit2 # 2 Gaussian
from NewFitAll import NewFit3 # 3 Gaussians
from NewFitAll import NewFit4 # 4 Gaussians
from NewFitAll import NewFit5 # 5 Gaussians
from NewFitAll import NewFit6 # 6 Gaussians
from NewFitAll import NewFit7 # 7 Gaussians

#%%
'W4 Data'
mu1= 0.3
sig1 = 0.6
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 1.2
sig2 = 0.4
amp2 = 300* np.sqrt(2*np.pi)*sig2

mu3 = 2.4
sig3 = 0.3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 3.6
sig4 = 0.3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 5
sig5 = 0.3
amp5 = 50* np.sqrt(2*np.pi)*sig2

#%%
'W3 Data'
mu1= 0.3
sig1 = 0.6
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 1.2
sig2 = 0.4
amp2 = 300* np.sqrt(2*np.pi)*sig2

mu3 = 2.4
sig3 = 0.3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 3.6
sig4 = 0.3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 5
sig5 = 0.3
amp5 = 20* np.sqrt(2*np.pi)*sig2


#%%
'W2 and X2 Data'
mu1= 0.3
sig1 = 0.6
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 1.0
sig2 = 0.4
amp2 = 300* np.sqrt(2*np.pi)*sig2

mu3 = 2.0
sig3 = 0.3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 3.0
sig4 = 0.3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 4.0
sig5 = 0.3
amp5 = 80* np.sqrt(2*np.pi)*sig2

#%%
'X1 Data'
mu1= 0.15
sig1 = 0.2
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 1.1
sig2 = 0.4
amp2 = 300* np.sqrt(2*np.pi)*sig2

mu3 = 1.9
sig3 = 0.3
amp3 = 130* np.sqrt(2*np.pi)*sig2

mu4 = 2.9
sig4 = 0.3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 3.9
sig5 = 0.3
amp5 = 80* np.sqrt(2*np.pi)*sig2

mu6 = 4.9
sig6 = 0.3
amp6 = 40* np.sqrt(2*np.pi)*sig2
#%%
'X4 Data'
mu1= 0.15
sig1 = 0.2
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 1.25
sig2 = 0.4
amp2 = 300* np.sqrt(2*np.pi)*sig2

mu3 = 2.5
sig3 = 0.3
amp3 = 200* np.sqrt(2*np.pi)*sig2

mu4 = 3.5
sig4 = 0.3
amp4 = 150* np.sqrt(2*np.pi)*sig2

mu5 = 4.5
sig5 = 0.3
amp5 = 80* np.sqrt(2*np.pi)*sig2

mu6 = 5.75
sig6 = 0.3
amp6 = 40* np.sqrt(2*np.pi)*sig2

mu7 = 6.7
sig7 = 0.3
amp7 = 40* np.sqrt(2*np.pi)*sig2
#%%
'W6 X6/7 Data'
mu1= 0.00
sig1 = 0.2
amp1 =80000 * np.sqrt(2*np.pi)*sig1

#%%
'X8 Data'
mu1= 0.15
sig1 = 0.2
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 0.825
sig2 = 0.4
amp2 = 120* np.sqrt(2*np.pi)*sig2

mu3 = 1.7
sig3 = 0.3
amp3 = 130* np.sqrt(2*np.pi)*sig2

#%%
'X9 Data'
mu1= 0.15
sig1 = 0.2
amp1 = 500 * np.sqrt(2*np.pi)*sig1

mu2 = 0.9
sig2 = 0.4
amp2 = 200* np.sqrt(2*np.pi)*sig2

mu3 = 1.8
sig3 = 0.3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 2.7
sig4 = 0.3
amp4 =50* np.sqrt(2*np.pi)*sig2

mu5 = 3.6
sig5 = 0.3
amp5 = 130* np.sqrt(2*np.pi)*sig2

#%%
'X6 noise Data'
mu1= 0.84
sig1 = 0.38
amp1 = 260 * np.sqrt(2*np.pi)*sig1

mu2 = 2.2
sig2 = 0.4
amp2 = 20* np.sqrt(2*np.pi)*sig2

mu3 = 3.3
sig3 = 0.3
amp3 = 50* np.sqrt(2*np.pi)*sig2


#%%

'Cut the Data'
x = [];
y = [];

#for i in range(0,120):
#    x.append(bincentroid[i]);
#    y.append(CountsData[i]);

x = bincentroid;
y = CountsData;

#plt.plot(x,y);

'Choose the fit type'
temporary = [];
#temporary = NewFit(amp1, mu1, sig1,x,y);
temporary = NewFit3(amp1,amp2,amp3, mu1,mu2,mu3, sig1,sig2,sig3,x,y);
#temporary = NewFit4(amp1,amp2,amp3,amp4, mu1,mu2,mu3,mu4, sig1,sig2,sig3,sig4,x,y);
#temporary = NewFit5(amp1,amp2,amp3,amp4,amp5,mu1,mu2,mu3,mu4,mu5,sig1,sig2,sig3,sig4,sig5,x,y);
#temporary = NewFit6(amp1,amp2,amp3,amp4,amp5, amp6, mu1,mu2,mu3,mu4,mu5,mu6,sig1,sig2,sig3,sig4,sig5,sig6, x,y)
#temporary = NewFit7(amp1,amp2,amp3,amp4,amp5, amp6,amp7, mu1,mu2,mu3,mu4,mu5,mu6,mu7,sig1,sig2,sig3,sig4,sig5,sig6,sig7, x,y)








