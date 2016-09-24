function W = randInitializeWeights(L_in, L_out)

% root6/root(lin+lout)

W = zeros(L_out, 1 + L_in);
epsilon_init=0.12;
%epsilon_init=1/L_in^0.5;
%epsilon_init=(6^0.5)/(L_in+L_out)^0.5;
W=rand(L_out,1+L_in)*2*epsilon_init - epsilon_init;
% negative of epsilon to positive of epsilon
end
