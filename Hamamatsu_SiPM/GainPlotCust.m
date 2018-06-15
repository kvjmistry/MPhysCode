% Gain Run Plots W1-4 Custom
% 30-04-2017
clear all;
close all;
set(0,'DefaultTextFontname', 'CMU Serif')
set(0, 'DefaultAxesFontName', 'CMU Serif')
set(0,'DefaultAxesFontWeight','bold');

SER1 = [12.6 13.6 15.5 17 18.3 19.9]; % Single Photoelectron
Sig1 = [0.25 0.25 0.2 3 3 4];

Gain = [28: 0.5 : 30.5];


SER1 = [8.55 9.57 10.74 12.63 13.31 15.96]; % Correscted for noise
Sig1 = [1 1.4 1.5 1.5 2 4];

SER2 = [8.99 9.74 11.38 11.58 12.14 13.06]; % Single Photoelectron Ln2 Temp
Sig2 = [0.7 0.5 0.4 0.3 0.3 0.3 ];

Ratio = SER2./SER1;
SIGRat = Ratio .* sqrt((Sig1./SER1).^2 + (Sig2./SER2).^2);



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

p3 = errorbar(x2+0.02,y2,e2,'kx','MarkerSize',8);  % plots the graph for data points
hold on
plot(ax,yfit2,'-k','LineWidth',1.5); % plots the LOBF over the top
hold off

xlabel('Bias Voltage (V)','FontSize',13','FontWeight','bold');
ylabel('SER (ADC)','FontSize',13,'FontWeight','bold');
title('Custom','FontSize',13);
set(gca, 'FontSize',13);
set(gca,'FontWeight','Bold');
xlim([27.5 31.5]) %cust
ylim([6 21]) %cust
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
title('Custom','FontSize',13);
set(gca, 'FontSize',13);
set(gca,'FontWeight','Bold'); 
xlim([27.9 30.6]) %cust
ylim([0.59 1.25]) %cust
 