% Gain Run Plots W1-4 Commercial
% 30-04-2017
clear all;
close all;
set(0,'DefaultTextFontname', 'CMU Serif')
set(0, 'DefaultAxesFontName', 'CMU Serif')
set(0,'DefaultAxesFontWeight','bold');

SER1 = [1 1.09 1.16 1.25]; % Single Photoelectron Room Temp
Sig1 = [0.02 0.02 0.02 0.02];


SER2 = [0.9 0.99 1.08 1.13 1.22 1.28]; % Single Photoelectron Ln2 Temp
Sig2 = [0.02 0.02 0.02 0.02 0.02 0.02];


Ratio = SER2(3:6)./SER1;
SIGRat = Ratio .* sqrt((Sig1./SER1).^2 + (Sig2(3:6)./SER2(3:6)).^2);


% SER1 = [0.83 0.94 1.04 1.08]; % Subtracted Room Temp
% Sig1 = [0.05 0.023 0.033 0.026];
% 
% 
% SER2 = [0.76 0.84 0.89 0.94 1.03 1.09]; % Subtracted Photoelectron Ln2 Temp
% Sig2 = [0.014 0.008 0.008 0.021 0.032 0.013];


Gain = [29: 0.5 : 30.5];

x = Gain;
y1 = SER1; % Room
e1 = Sig1;
y2 = SER2; % Ln2
e2 = Sig2;
x2 = [28: 0.5 : 30.5];

[b, err_b, a, err_a, rchi2, yfit1 ] = LinearFit( x, y1, e1 );
[b, err_b, a, err_a, rchi2, yfit2 ] = LinearFit( x2, y2, e2 ); 

ax = [27:1:32]; % Change the axis scale Commercial

% Plots Graph with errorbars and best fit line
figure('name','Data with LOBF')
p1 = errorbar(x,y1,e1,'k.','MarkerSize',15);  % plots the graph for data points
hold on
plot(ax,yfit1,'-k','LineWidth',1.5); % plots the LOBF over the top
hold on

p3 = errorbar(x2,y2,e2,'kx','MarkerSize',8);  % plots the graph for data points
hold on
plot(ax,yfit2,'-k','LineWidth',1.5); % plots the LOBF over the top
hold off

xlabel('Bias Voltage (V)','FontSize',13','FontWeight','bold');
ylabel('SER (ADC)','FontSize',13,'FontWeight','bold');
title('Commercial','FontSize',13);
set(gca, 'FontSize',13);
set(gca,'FontWeight','Bold'); 
xlim([27.5 31]) %Com
ylim([0.8 1.35]) %Com
legend([p1 p3],'Room','LN_2','Location','northwest')



%Plot the ratio
yfitrat  = mean(Ratio);
yfitrat = ones(6) * yfitrat;

figure('name','Test')
errorbar(x,Ratio,SIGRat,'k.','MarkerSize',15);  % plots the graph for data points
hold on
plot(ax,yfitrat,'-k','LineWidth',1.5); % plots the LOBF over the top
hold off
xlabel('Bias Voltage (V)','FontSize',13','FontWeight','bold');
ylabel('Ratio','FontSize',13,'FontWeight','bold');
title('Commercial','FontSize',13);
set(gca, 'FontSize',13);
set(gca,'FontWeight','Bold'); 
xlim([28.9 30.6]) %Com
ylim([1 1.12]) %Com
 