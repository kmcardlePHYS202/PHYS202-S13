experiment = importdata('radioactivedecay.dat');
t = experiment.data(:,1);
N = experiment.data(:,2);
figure(42)
plot(t,N,'.b')

%%

hold on
% fit the data
fittedmodel = fit(t,N,'poly4')
% plot the result
plot(fittedmodel,'r-');
legend('data','fitted line')
hold off