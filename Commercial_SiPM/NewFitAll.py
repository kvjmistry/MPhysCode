#!/usr/bin/env python
#<examples/doc_nistgauss.py>
from lmfit.models import GaussianModel
from lmfit import Parameters
import matplotlib.pyplot as plt


'Input Example'
#mu1= 0
#sig1 = 1.0
#A1 = 275 * np.sqrt(2*np.pi)*sig1
#
#mu2 = 5.5
#sig2 = 2.0
#A2 = 1010* np.sqrt(2*np.pi)*sig2

def NewFit(amp1,mu1,sig1,x,y):

    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1, vary = True)
    
    '==========================================='
    
    'Make the model as the sum of gaussians'
    mod = gauss1

    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-',linewidth = 1.50)
    plt.show()
    return pars


def NewFit2(amp1,amp2,mu1,mu2,sig1,sig2,x,y):

    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1, vary = True)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2, vary = True)
    pars['g2_sigma'].set(sig2, vary = True)
    pars['g2_amplitude'].set(amp2, vary = True)
    
    '==========================================='
    
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 

    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-',linewidth=1.5)
    plt.show()
    return pars

def NewFit3(amp1,amp2,amp3,mu1,mu2,mu3,sig1,sig2,sig3,x,y):
    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = False)
    pars['g1_sigma'].set(sig1, vary = False)
    pars['g1_amplitude'].set(amp1,min = 0, vary = False,)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2,min=2, vary = False)
    pars['g2_sigma'].set(sig2, max = 0.26,vary = False)
    pars['g2_amplitude'].set(amp2, min = 0,vary = False)
    
    '==========================================='
    
    'Define the third Gaussian'
    gauss3 = GaussianModel(prefix='g3_')     
    pars.update(gauss3.make_params()) #update the parameter list with another gaussian
    
    pars['g3_center'].set(mu3, vary = True)
    pars['g3_sigma'].set(sig3,max = 0.3, vary = True)
    pars['g3_amplitude'].set(amp3,min = 0, vary = True)
    
    '==========================================='
    
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 + gauss3

    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-',linewidth = 1.50)
    plt.show()
    return pars

def NewFit4(amp1,amp2,amp3,amp4, mu1,mu2,mu3,mu4, sig1,sig2,sig3,sig4,x,y):

    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1,min =  0, vary = True)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2, vary = True)
    pars['g2_sigma'].set(sig2, vary = True)
    pars['g2_amplitude'].set(amp2,min =  0, vary = True)
    
    '==========================================='
    
    'Define the third Gaussian'
    gauss3 = GaussianModel(prefix='g3_')     
    pars.update(gauss3.make_params()) #update the parameter list with another gaussian
    
    pars['g3_center'].set(mu3, vary = True)
    pars['g3_sigma'].set(sig3, vary = True)
    pars['g3_amplitude'].set(amp3,min =  0, vary = True)
    
    '==========================================='
         
    'Define the four Gaussian'
    gauss4 = GaussianModel(prefix='g4_')     
    pars.update(gauss4.make_params()) #update the parameter list with another gaussian
    
    pars['g4_center'].set(mu4, vary = True)
    pars['g4_sigma'].set(sig4,max = 0.25, vary = True)
    pars['g4_amplitude'].set(amp4,min =  0, vary = True)
    
    '==========================================='
       
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 + gauss3 + gauss4;
    
    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-',linewidth = 1.5)
    plt.show()
    return pars

def NewFit5(amp1,amp2,amp3,amp4,amp5, 
            mu1,mu2,mu3,mu4,mu5,
            sig1,sig2,sig3,sig4,sig5,
            x,y):

    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1, vary = True)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2, vary = True)
    pars['g2_sigma'].set(sig2, vary = True)
    pars['g2_amplitude'].set(amp2,min =  0, vary = True)
    
    '==========================================='
    
    'Define the third Gaussian'
    gauss3 = GaussianModel(prefix='g3_')     
    pars.update(gauss3.make_params()) #update the parameter list with another gaussian
    
    pars['g3_center'].set(mu3, min=0.2,vary = True)
    pars['g3_sigma'].set(sig3, vary = True)
    pars['g3_amplitude'].set(amp3,min =  0, vary = True)
    
    '==========================================='
         
    'Define the four Gaussian'
    gauss4 = GaussianModel(prefix='g4_')     
    pars.update(gauss4.make_params()) #update the parameter list with another gaussian
    
    pars['g4_center'].set(mu4,min=0.3, vary = True)
    pars['g4_sigma'].set(sig4,max = 0.4,  vary = True)
    pars['g4_amplitude'].set(amp4,min =  0, vary = True)
    
    '==========================================='
       
    'Define the fith Gaussian'
    gauss5 = GaussianModel(prefix='g5_')     
    pars.update(gauss5.make_params()) #update the parameter list with another gaussian
    
    pars['g5_center'].set(mu5,max = 3.7, vary = True)
    pars['g5_sigma'].set(sig5,min= 0, max = 0.35,  vary = True)
    pars['g5_amplitude'].set(amp5,min =  0, vary = True)
    
    '==========================================='
    
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 + gauss3 + gauss4 + gauss5;
    
    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-', linewidth=1.50)
    plt.show()
    return pars


def NewFit6(amp1,amp2,amp3,amp4,amp5, amp6,
            mu1,mu2,mu3,mu4,mu5,mu6,
            sig1,sig2,sig3,sig4,sig5,sig6,
            x,y):
    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1, vary = True)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2, vary = True)
    pars['g2_sigma'].set(sig2, vary = True)
    pars['g2_amplitude'].set(amp2,min =  0, vary = True)
    
    '==========================================='
    
    'Define the third Gaussian'
    gauss3 = GaussianModel(prefix='g3_')     
    pars.update(gauss3.make_params()) #update the parameter list with another gaussian
    
    pars['g3_center'].set(mu3, min=0.2,vary = True)
    pars['g3_sigma'].set(sig3, vary = True)
    pars['g3_amplitude'].set(amp3,min =  0, vary = True)
    
    '==========================================='
         
    'Define the four Gaussian'
    gauss4 = GaussianModel(prefix='g4_')     
    pars.update(gauss4.make_params()) #update the parameter list with another gaussian
    
    pars['g4_center'].set(mu4,min=0.3, vary = True)
    pars['g4_sigma'].set(sig4,max = 0.4,  vary = True)
    pars['g4_amplitude'].set(amp4,min =  0, vary = True)
    
    '==========================================='
       
    'Define the fith Gaussian'
    gauss5 = GaussianModel(prefix='g5_')     
    pars.update(gauss5.make_params()) #update the parameter list with another gaussian
    
    pars['g5_center'].set(mu5,max = 3.8, vary = True)
    pars['g5_sigma'].set(sig5,min= 0, max = 0.35,  vary = True)
    pars['g5_amplitude'].set(amp5,min =  0, vary = True)
    
    '==========================================='
    
    '==========================================='
    'Define the sixth Gaussian'
    gauss6 = GaussianModel(prefix='g6_')     
    pars.update(gauss6.make_params()) #update the parameter list with another gaussian
    
    pars['g6_center'].set(mu6, vary = True)
    pars['g6_sigma'].set(sig6,max = 0.35,  vary = True)
    pars['g6_amplitude'].set(amp6,min =  0, vary = True)
    
    '==========================================='
    
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 + gauss3 + gauss4 + gauss5 + gauss6;
    
    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-', linewidth=1.50)
    plt.show()
    return pars

def NewFit7(amp1,amp2,amp3,amp4,amp5, amp6,amp7,
            mu1,mu2,mu3,mu4,mu5,mu6,mu7,
            sig1,sig2,sig3,sig4,sig5,sig6,sig7,
            x,y):

    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1,min =  0, vary = True)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2, vary = True)
    pars['g2_sigma'].set(sig2, vary = True)
    pars['g2_amplitude'].set(amp2,min =  0, vary = True)
    
    '==========================================='
    
    'Define the third Gaussian'
    gauss3 = GaussianModel(prefix='g3_')     
    pars.update(gauss3.make_params()) #update the parameter list with another gaussian
    
    pars['g3_center'].set(mu3, vary = True)
    pars['g3_sigma'].set(sig3, vary = True)
    pars['g3_amplitude'].set(amp3,min =  0, vary = True)
    
    '==========================================='
         
    'Define the four Gaussian'
    gauss4 = GaussianModel(prefix='g4_')     
    pars.update(gauss4.make_params()) #update the parameter list with another gaussian
    
    pars['g4_center'].set(mu4, vary = True)
    pars['g4_sigma'].set(sig4,  vary = True)
    pars['g4_amplitude'].set(amp4,min =  0, vary = True)
    
    '==========================================='
       
    'Define the fith Gaussian'
    gauss5 = GaussianModel(prefix='g5_')     
    pars.update(gauss5.make_params()) #update the parameter list with another gaussian
    
    pars['g5_center'].set(mu5, vary = True)
    pars['g5_sigma'].set(sig5,  vary = True)
    pars['g5_amplitude'].set(amp5,min =  0, vary = True)
    
    '==========================================='
    'Define the sixth Gaussian'
    gauss6 = GaussianModel(prefix='g6_')     
    pars.update(gauss6.make_params()) #update the parameter list with another gaussian
    
    pars['g6_center'].set(mu6, vary = True)
    pars['g6_sigma'].set(sig6,  vary = True)
    pars['g6_amplitude'].set(amp6,min =  0, vary = True)
    
    '==========================================='
    'Define the seventh Gaussian'
    gauss7 = GaussianModel(prefix='g7_')     
    pars.update(gauss7.make_params()) #update the parameter list with another gaussian
    
    pars['g7_center'].set(mu7,max = 6.8, vary = True)
    pars['g7_sigma'].set(sig7,max = 0.4,  vary = True)
    pars['g7_amplitude'].set(amp7,min =  0, vary = True)
    
    '==========================================='
    
    
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 + gauss3 + gauss4 + gauss5 + gauss6 + gauss7;
    
    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-', linewidth=1.50)
    plt.show()
    return pars

def NewFit8(amp1,amp2,amp3,amp4,amp5, amp6,amp7,amp8,
            mu1,mu2,mu3,mu4,mu5,mu6,mu7,mu8,
            sig1,sig2,sig3,sig4,sig5,sig6,sig7,sig8,
            x,y):

    '=========================================='
    'Define the first gaussian'
    gauss1 = GaussianModel(prefix='g1_') # Model first as a gaussian
    pars = gauss1.guess(y, x=x)          # Make a gautomatic guess of the parameters
    
    'Set the Parameters values'
    pars['g1_center'].set(mu1, vary = True)
    pars['g1_sigma'].set(sig1, vary = True)
    pars['g1_amplitude'].set(amp1,min =  0, vary = True)
    
    '==========================================='
    'Define the second Gaussian'
    gauss2 = GaussianModel(prefix='g2_')     
    pars.update(gauss2.make_params()) #update the parameter list with another gaussian
    
    pars['g2_center'].set(mu2, vary = True)
    pars['g2_sigma'].set(sig2, vary = True)
    pars['g2_amplitude'].set(amp2,min =  0, vary = True)
    
    '==========================================='
    
    'Define the third Gaussian'
    gauss3 = GaussianModel(prefix='g3_')     
    pars.update(gauss3.make_params()) #update the parameter list with another gaussian
    
    pars['g3_center'].set(mu3, vary = True)
    pars['g3_sigma'].set(sig3, vary = True)
    pars['g3_amplitude'].set(amp3,min =  0, vary = True)
    
    '==========================================='
         
    'Define the four Gaussian'
    gauss4 = GaussianModel(prefix='g4_')     
    pars.update(gauss4.make_params()) #update the parameter list with another gaussian
    
    pars['g4_center'].set(mu4, vary = True)
    pars['g4_sigma'].set(sig4,  vary = True)
    pars['g4_amplitude'].set(amp4,min =  0, vary = True)
    
    '==========================================='
       
    'Define the fith Gaussian'
    gauss5 = GaussianModel(prefix='g5_')     
    pars.update(gauss5.make_params()) #update the parameter list with another gaussian
    
    pars['g5_center'].set(mu5, vary = True)
    pars['g5_sigma'].set(sig5,  vary = True)
    pars['g5_amplitude'].set(amp5,min =  0, vary = True)
    
    '==========================================='
    'Define the sixth Gaussian'
    gauss6 = GaussianModel(prefix='g6_')     
    pars.update(gauss6.make_params()) #update the parameter list with another gaussian
    
    pars['g6_center'].set(mu6, vary = True)
    pars['g6_sigma'].set(sig6,  vary = True)
    pars['g6_amplitude'].set(amp6,min =  0, vary = True)
    
    '==========================================='
    'Define the seventh Gaussian'
    gauss7 = GaussianModel(prefix='g7_')     
    pars.update(gauss7.make_params()) #update the parameter list with another gaussian
    
    pars['g7_center'].set(mu7, vary = True)
    pars['g7_sigma'].set(sig7,  vary = True)
    pars['g7_amplitude'].set(amp7,min =  0, vary = True)
    
    '==========================================='
    
    'Define the eigth Gaussian'
    gauss8 = GaussianModel(prefix='g8_')     
    pars.update(gauss8.make_params()) #update the parameter list with another gaussian
    
    pars['g8_center'].set(mu8, vary = True)
    pars['g8_sigma'].set(sig8,  vary = True)
    pars['g8_amplitude'].set(amp8,min =  0, vary = True)
    
    '==========================================='
    'Make the model as the sum of gaussians'
    mod = gauss1 + gauss2 + gauss3 + gauss4 + gauss5 + gauss6 + gauss7 + gauss8;
    
    'Fit and print the data'
    out = mod.fit(y, pars, x=x)
    print(out.fit_report(min_correl=0.5))
    plt.plot(x, out.best_fit, 'r-', linewidth=1.50)
    plt.show()
    return pars








