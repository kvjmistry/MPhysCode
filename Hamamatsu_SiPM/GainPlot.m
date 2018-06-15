% Gain Run Plots W1-4 Hamamatsu
% 30-04-2017
clear all;
close all;
set(0,'DefaultTextFontname', 'CMU Serif')
set(0, 'DefaultAxesFontName', 'CMU Serif')
set(0,'DefaultAxesFontWeight','bold');

SER1 = [2.74 5.17 7.68 10.06]; % Single Photoelectron
Sig1 = [0.15 0.15 0.15 0.15];
Gain = [52: 1 : 55];

SER1 = [2.40 5.03 7.63 10.26 ]; % data with shift of pedestal
Sig1 = [0.25 0.25 0.25 0.25];



x = Gain;
y = SER1;
e = Sig1;

[b, err_b, a, err_a, rchi2, yfit ] = LinearFit( x, y, e );
ax = [50:1:58]; % Change the axis scale Hamamatsu 

% Plots Graph with errorbars and best fit line
figure('name','Data with LOBF')
errorbar(x,y,e,'k.','MarkerSize',15);  % plots the graph for data points
hold on
plot(ax,yfit,'-k','LineWidth',1.5); % plots the LOBF over the top
hold off
xlabel('Bias Voltage (V)','FontSize',13','FontWeight','bold');
ylabel('SER (ADC)','FontSize',13,'FontWeight','bold');
title('Hamamatsu','FontSize',13);
set(gca, 'FontSize',13);
%set(gca, 'FontWeight','bold'); 
set(gca,'FontWeight','Bold'); 
xlim([51 56]) %Ham
ylim([0 11]) %Ham




 