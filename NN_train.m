clear ; close all; clc


input_layer_size  =  28; 
hidden_layer_size = 10;  
num_labels = 2;             
                          
load('12months.mat');
temp=double(temp);
X=temp;
y=X(:,1);
X=X(:,2:size(X,2));
%--------------------------------------------
m = size(X, 1);

sel = randperm(size(X, 1));
sel = sel(1:20);

%---------------------------------------------------------------------

epsilon_init=0.12;   % tweak
%epsilon_init=1/L_in^0.5;
%epsilon_init=(6^0.5)/(L_in+L_out)^0.5;
Theta1=rand(hidden_layer_size,1+input_layer_size)*2*epsilon_init - epsilon_init;
Theta2=rand(num_labels,1+hidden_layer_size)*2*epsilon_init - epsilon_init;
%---------------------------------------------------------------------
nn_params = [Theta1(:) ; Theta2(:)];

fprintf('\nfeedforward neural network\n')
lambda = 0;
J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, ...
                   num_labels, X, y, lambda);
fprintf(['\nCost at parameters %f '...
         '\n'], J);

fprintf('\nInitializing Neural Network Parameters ...\n')
initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);
initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];

lambda = 3; %tweak
checkNNGradients(lambda);

% % Also output the costFunction debugging values
% debug_J  = nnCostFunction(nn_params, input_layer_size, ...
%                           hidden_layer_size, num_labels, X, y, lambda);
% 
% fprintf(['\n\nCost at (fixed) debugging parameters (w/ lambda = 10): %f ' ...
%          '\n\n\n'], debug_J);

%  advanced optimizers
fprintf('\nTraining Neural Network... \n')
% MaxIter to a larger value to see how more training helps.
options = optimset('MaxIter', 50);
% try different values of lambda
lambda = 3;
costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, X, y, lambda);
                               
[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);
%fmincg batch gradient descent

%for which the feed forward and back prop gradients have been obtained in

%nnCostFunction
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));
Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

%  displaying the hidden units to see what features they are capturing in 
fprintf('\nVisualizing Neural Network... \n')

%displayData(Theta1(:, 2:end));

pred = predict(Theta1, Theta2, X);
fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);

rp = randperm(m);


