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
'X1 Data'
mu1= 0.3
sig1 = 2
amp1 = 350 * np.sqrt(2*np.pi)*sig1

mu2 = 9
sig2 = 2
amp2 = 150* np.sqrt(2*np.pi)*sig2

mu3 = 18
sig3 = 2
amp3 = 80* np.sqrt(2*np.pi)*sig2

mu4 = 27
sig4 = 2
amp4 = 40* np.sqrt(2*np.pi)*sig2

#%%
'X2 Data'
mu1= 0.3
sig1 = 0.6
amp1 = 350 * np.sqrt(2*np.pi)*sig1

mu2 = 11.23
sig2 = 0.4
amp2 = 150* np.sqrt(2*np.pi)*sig2

mu3 = 22
sig3 = 0.3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 33
sig4 = 0.3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 41
sig5 = 0.3
amp5 = 50* np.sqrt(2*np.pi)*sig2

#%%
'X3 Data'
mu1= 2.5
sig1 = 2
amp1 = 350 * np.sqrt(2*np.pi)*sig1

mu2 = 11.23
sig2 = 2
amp2 = 150* np.sqrt(2*np.pi)*sig2

mu3 = 22
sig3 = 2
amp3 = 80* np.sqrt(2*np.pi)*sig2

mu4 = 31
sig4 = 3
amp4 = 40* np.sqrt(2*np.pi)*sig2

mu5 = 40 # set vary = False
sig5 = 3
amp5 = 30* np.sqrt(2*np.pi)*sig2
#%%
'X4 Data'
mu1= 2.5
sig1 = 3
amp1 = 600 * np.sqrt(2*np.pi)*sig1

mu2 = 11.5
sig2 = 3
amp2 = 270* np.sqrt(2*np.pi)*sig2

mu3 = 21.5
sig3 = 3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 32
sig4 = 3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 41
sig5 = 3
amp5 = 50* np.sqrt(2*np.pi)*sig2

#%%
'X5 Data'
mu1= 2.5
sig1 = 3
amp1 = 600 * np.sqrt(2*np.pi)*sig1

mu2 = 12
sig2 = 3
amp2 = 270* np.sqrt(2*np.pi)*sig2

mu3 = 21.5
sig3 = 3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 33
sig4 = 3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 42
sig5 = 3
amp5 = 50* np.sqrt(2*np.pi)*sig2

mu6 = 53
sig6 = 3
amp6 = 40* np.sqrt(2*np.pi)*sig2
#%%
'X6 Data'
mu1= 2.5
sig1 = 3
amp1 = 600 * np.sqrt(2*np.pi)*sig1

mu2 = 13
sig2 = 3
amp2 = 270* np.sqrt(2*np.pi)*sig2

mu3 = 24
sig3 = 3
amp3 = 150* np.sqrt(2*np.pi)*sig2

mu4 = 35.5
sig4 = 3
amp4 = 80* np.sqrt(2*np.pi)*sig2

mu5 = 47
sig5 = 3
amp5 = 50* np.sqrt(2*np.pi)*sig2

mu6 = 58
sig6 = 3
amp6 = 40* np.sqrt(2*np.pi)*sig2
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
temporary = NewFit(amp1, mu1, sig1,x,y);
#temporary = NewFit3(amp1,amp2,amp3, mu1,mu2,mu3, sig1,sig2,sig3,x,y);
#temporary = NewFit4(amp1,amp2,amp3,amp4, mu1,mu2,mu3,mu4, sig1,sig2,sig3,sig4,x,y);
#temporary = NewFit5(amp1,amp2,amp3,amp4,amp5,mu1,mu2,mu3,mu4,mu5,sig1,sig2,sig3,sig4,sig5,x,y);
#temporary = NewFit6(amp1,amp2,amp3,amp4,amp5, amp6, mu1,mu2,mu3,mu4,mu5,mu6,sig1,sig2,sig3,sig4,sig5,sig6, x,y)
#temporary = NewFit7(amp1,amp2,amp3,amp4,amp5, amp6,amp7, mu1,mu2,mu3,mu4,mu5,mu6,mu7,sig1,sig2,sig3,sig4,sig5,sig6,sig7, x,y)








