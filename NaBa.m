% clear all;
% close all;
% clc;

%XX = csvread('train1000.csv');
XX = train;
L = XX(:,1);
X = XX(:,2:23);

tr = fitcnb(X, L, 'DistributionNames', 'mvmn');

% XV = csvread('valid1000.csv');
XV = valid;
Ly = XV(:,1);
Y = XV(:,2:23);

[a b c] = predict(tr, Y);

accuracy = mean(Ly==a);

A=0; B=0; C=0; D=0;
for g=1:size(Ly,1)
    if Ly(g)==1 && a(g)==1
        A = A+1;
    end
    if Ly(g)==1 && a(g)==-1
        C = C+1;
    end
    if Ly(g)==-1 && a(g)==1
        B = B+1;
    end
    if Ly(g)==-1 && a(g)==-1
        D = D+1;
    end
end

recall = A/(A+C);
precision = A/(A+B);
F1 = 2*(recall * precision)/(recall + precision);