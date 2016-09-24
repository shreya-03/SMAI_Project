


% input_layer_size  =  28; 
% hidden_layer_size = 12;  
% num_labels = 2;             
                          
load('12months_test.mat');
temp=double(temp);
X_test=temp;
y_test=X_test(:,1);
X_test=X_test(:,2:size(X_test,2));
%--------------------------------------------
% m = size(X_test, 1);
% 
% 
% %displayData(Theta1(:, 2:end));
% 
% pred = predict(Theta1, Theta2, X_test);
% fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y_test)) * 100);
% 
% rp = randperm(m);
pred = predict(Theta1, Theta2, X_test);


%------recall, precision, F1--------
A=0, B=0, C=0, D=0;
for g=1:size(y_test,1)
    if y_test(g)==2 && pred(g)==2
        A = A+1;
    end
    if y_test(g)==2 && pred(g)==1
        C = C+1;
    end
    if y_test(g)==1 && pred(g)==2
        B = B+1;
    end
    if y_test(g)==1 && pred(g)==1
        D = D+1;
    end
end

recall = A/(A+C)
precision = A/(A+B)
F1 = 2*(recall * precision)/(recall + precision)

