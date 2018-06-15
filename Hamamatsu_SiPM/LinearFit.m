function [b, err_b, a, err_a, rchi2, yfit ] = LinearFit( x, y, e )
% Performs a best fit on some data
%--------------------------------------------------------------------------
%% Sample input:

% 
% 
% % Sample plots:
% % Residual Plot (By itself)
%  figure('name','Residual Plot')
%  errorbar(x, yfit-y,e,'k*','MarkerSize',3); 
%  xlabel('X','FontSize',13);
%  ylabel('Y','FontSize',13);
%  title('title','FontSize',13);
%  set(gca, 'FontSize',13);
%  
% % Plots Graph with errorbars and best fit line
%  figure('name','Data with LOBF')
%  errorbar(x,y,e,'k*','MarkerSize',3);  % plots the graph for data points
%  hold on
%  plot(x,yfit,'-b','LineWidth',2); % plots the LOBF over the top
%  hold off
% 
% % Plots combination of best fit and residuals
%  figure('name','Data with LOBF and Residuals') 
% % if desired combine residuals with graphs
%  subplot(7,1,1:4), errorbar(x,y,e,'k*','MarkerSize',3);  % plots the graph for data points
%  hold on
%  subplot(7,1,1:4), plot(x,yfit,'-b','LineWidth',2); % plots the LOBF over the top
%  hold off
%  xlabel('X','FontSize',13);
%  ylabel('Y','FontSize',13);
%  title('title','FontSize',13);
%  set(gca, 'FontSize',13);
%  
%  subplot(7,1,6:7), errorbar(x, yfit-y,e,'k*','MarkerSize',3); % plots the residuals below main plot
%  xlabel('X','FontSize',13);
%  ylabel('y-yfit','FontSize',13);
%  title('residuals','FontSize',13);
%  set(gca, 'FontSize',13);
%--------------------------------------------------------------------------

%% Calculations
sig = sum(1./(e.^2)); %[1]
xbar = sum( x./ (e.^2)  ); % [x] 
ybar = sum( y./ (e.^2)  ); % [y]
xybar = sum( (x.*y)./ (e.^2)  ); % [xy]
xbar2 = sum( (x./e).^2) ; % [x^2]
ax = xbar/ sig; % <x> 
ay = ybar/sig; % <y>

b = (sig * xybar - xbar * ybar)/(sig * xbar2  - xbar * xbar); % Gradient
a = ay - b * ax ; % Intercept

% Errors
x_prime = x - ax; % x'
x_primebar2 = sum( ( x_prime./e ).^2 ); % [x'^2]

err_b = 1/ sqrt(x_primebar2); % Error on gradient

err_a_prime = 1/ sqrt(sig);
err_a = sqrt(   err_a_prime^2 + (ax * err_b)^2 ); % Error on intercept

% Chi-squared
[P,S] = polyfit(x,y,1);
yfit = polyval(P,x); 
rchi2 = sum(((y - yfit)./e).^2)/S.df;

% ax = [50:1:58]; % Change the axis scale Hamamatsu
ax = [27:1:32]; % Change the axis scale Commercial
yfit = polyval(P,ax); 

%% Display Results (if wanted uncomment this section)
 fprintf('gradient = %4.4f +/- %4.4f\n',b,err_b);
 fprintf('intercept = %4.4f +/- %4.4f\n',a,err_a);
 fprintf('Reduced chi-squared = %4.4f\n',rchi2);

end

