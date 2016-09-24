function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)

Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);         
X=[ones(m,1) X];
 
%p = zeros(size(X, 1), 1);

tempa=sigmoid(X*Theta1');
new=X*Theta1';
new1=[ones(size(new,1),1) new];
tempa1=[ones(size(tempa,1),1) tempa];
tempb=sigmoid(tempa1*Theta2');
%[a,p]=max(tempb,[],2);
 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));
ks=size(Theta2,1);
A=log(tempb);
%A
B=log(1-tempb);
%B
ok=1:ks;
for i=1:m
    okm=ok==y(i);
    
    d3=tempb(i,:)-okm;
    
    d2=((Theta2')*(d3')).*sigmoidGradient((new1(i,:))');
    d2=d2(2:end);
    
    Theta2_grad=Theta2_grad+d3'*tempa1(i,:); 
    Theta1_grad=Theta1_grad+d2*X(i,:); 
    
    
    J=J+sum(okm.*A(i,:))+sum((1-okm).*B(i,:));
end

Theta2_grad=Theta2_grad/m;
Theta1_grad=Theta1_grad/m;

Theta2_grad(:,2:end)=Theta2_grad(:,2:end)+lambda/m*(Theta2(:,2:end));
Theta1_grad(:,2:end)=Theta1_grad(:,2:end)+lambda/m*(Theta1(:,2:end));

J=-J/m;
pr=Theta1(:,2:end).^2;
si=Theta2(:,2:end).^2;

J=J+(lambda/(2*m))*(sum(pr(:))+sum(si(:)));

grad = [Theta1_grad(:) ; Theta2_grad(:)];
%grad

end
