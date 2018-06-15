#%%


'Curve fitting input code'
'Uses the Lmfit module to fit the data'


from NewFitAll import NewFit  # 1 Gaussian
from NewFitAll import NewFit2 # 2 Gaussians
from NewFitAll import NewFit3 # 3 Gaussians
from NewFitAll import NewFit4 # 4 Gaussians
from NewFitAll import NewFit5 # 5 Gaussians
from NewFitAll import NewFit7 # 7 Gaussians

#%%
'W4 Data'
mu1= 0.3
sig1 = 1.0
amp1 = 450 * np.sqrt(2*np.pi)*sig1

mu2 = 10
sig2 = 2.0
amp2 = 650* np.sqrt(2*np.pi)*sig2

mu3 = 20
sig3 = 2.0
amp3 = 550* np.sqrt(2*np.pi)*sig2

mu4 = 30.0
sig4 = 2.0
amp4 = 400* np.sqrt(2*np.pi)*sig2

mu5 = 40.0
sig5 = 2.0
amp5 = 190* np.sqrt(2*np.pi)*sig2

mu6 = 50.0
sig6 = 2.0
amp6 = 100* np.sqrt(2*np.pi)*sig2

mu7 = 60.0
sig7 = 2.0
amp7 = 50* np.sqrt(2*np.pi)*sig2

#%%
'W3 Data'
mu1= 7
sig1 = 1.0
amp1 = 450 * np.sqrt(2*np.pi)*sig1

mu2 = 14
sig2 = 2.0
amp2 = 650* np.sqrt(2*np.pi)*sig2

mu3 = 21
sig3 = 2.0
amp3 = 550* np.sqrt(2*np.pi)*sig2

mu4 = 28
sig4 = 2.0
amp4 = 400* np.sqrt(2*np.pi)*sig2

mu5 = 35
sig5 = 2.0
amp5 = 190* np.sqrt(2*np.pi)*sig2

mu6 = 41
sig6 = 2.0
amp6 = 100* np.sqrt(2*np.pi)*sig2

mu7 = 49
sig7 = 2.0
amp7 = 50* np.sqrt(2*np.pi)*sig2
#%%
'W2 Data'
mu1= 0
sig1 = 1.0
amp1 = 450 * np.sqrt(2*np.pi)*sig1

mu2 = 5
sig2 = 2.0
amp2 = 650* np.sqrt(2*np.pi)*sig2

mu3 = 10
sig3 = 2.0
amp3 = 550* np.sqrt(2*np.pi)*sig2

mu4 = 15
sig4 = 2.0
amp4 = 400* np.sqrt(2*np.pi)*sig2

mu5 = 20
sig5 = 2.0
amp5 = 190* np.sqrt(2*np.pi)*sig2

mu6 = 25
sig6 = 2.0
amp6 = 100* np.sqrt(2*np.pi)*sig2

mu7 = 30
sig7 = 2.0
amp7 = 50* np.sqrt(2*np.pi)*sig2
#%%
'W1 Data'
mu1= 0
sig1 = 1.0
amp1 = 250 * np.sqrt(2*np.pi)*sig1

mu2 = 3
sig2 = 2.0
amp2 = 200* np.sqrt(2*np.pi)*sig2

mu3 = 5
sig3 = 2.0
amp3 = 55* np.sqrt(2*np.pi)*sig2

mu4 = 8
sig4 = 2.0
amp4 = 25* np.sqrt(2*np.pi)*sig2

#%%
'W6 W7 Data'
mu1= 0
sig1 = 1.0
amp1 = 250 * np.sqrt(2*np.pi)*sig1

mu2= 0
sig2 = 1.0
amp2 = 250 * np.sqrt(2*np.pi)*sig1

#%%
'W6 dark count data'
mu1= 7
sig1 = 1.0
amp1 = 3500 * np.sqrt(2*np.pi)*sig1

mu2= 7
sig2 = 2
amp2 = 500 * np.sqrt(2*np.pi)*sig1


mu3= 15
sig3 = 2.0
amp3 = 500 * np.sqrt(2*np.pi)*sig1


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
#temporary = NewFit2(amp1,amp2, mu1,mu2, sig1,sig2,x,y);
temporary = NewFit3(amp1,amp2,amp3, mu1,mu2,mu3, sig1,sig2,sig3,x,y);
#temporary = NewFit4(amp1,amp2,amp3,amp4, mu1,mu2,mu3,mu4, sig1,sig2,sig3,sig4,x,y);
#temporary = NewFit5(amp1,amp2,amp3,amp4,amp5,mu1,mu2,mu3,mu4,mu5,sig1,sig2,sig3,sig4,sig5,x,y);
#temorary = NewFit7(amp1,amp2,amp3,amp4,amp5, amp6,amp7, mu1,mu2,mu3,mu4,mu5,mu6,mu7, sig1,sig2,sig3,sig4,sig5,sig6,sig7, x,y)









