load('smai40.mat')
temp=double(temp);
x=temp(:,[5 6 7 8 10 12 13 14 15 16 19 21]);
[coeff,score,latent] = pca(x);

I=eye(12);
d=latent'*I;
for i=1:12
I(i,:)=I(i,:).*latent(i);
end
cov=coeff*I*(coeff');

[coeff2,score2,latent2] = pca(score);
I2=eye(12);
d2=latent2'*I2;
for i=1:12
I2(i,:)=I2(i,:).*latent2(i);
end
cov2=coeff2*I2*(coeff2');
