import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.nonparametric.kde import KDEUnivariate
from statsmodels.nonparametric import smoothers_lowess
from pandas import Series, DataFrame
from patsy import dmatrices
from sklearn import datasets, svm
from KaggleAux import predict as ka

df = pd.read_csv("data2/modtrain5000.csv")
dftest =  pd.read_csv("data2/modvalid5000.csv")
df = df.dropna()
dftest = dftest.dropna()
#print df
print "dataset imported"

#fig = plt.figure(figsize=(18,6), dpi=1600) 
alpha=alpha_scatterplot = 0.2 
alpha_bar_chart = 0.55
#
## a14 airtime
#
## lets us plot many diffrent shaped graphs together 
#ax1 = plt.subplot2grid((2,3),(0,0))
## plots a bar graph of those who surived vs those who did not.               
#df.logistlabel.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
## this nicely sets the margins in matplotlib to deal with a recent bug 1.3.1
#ax1.set_xlim(-1, 2)
## puts a title on our graph
#plt.title("Distribution of Flight time, (1 = Delayed)") 
#
#plt.subplot2grid((2,3),(0,1))
#plt.scatter(df.logistlabel, df.a4, alpha=alpha_scatterplot)
## sets the y axis lable
#plt.ylabel("Day of week")
## formats the grid line style of our graphs                          
#plt.grid(b=True, which='major', axis='y')  
#plt.title("delay by day of week,  (1 = Delayed)")
#plt.show()
#ax3 = plt.subplot2grid((2,3),(0,2))
#df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
#ax3.set_ylim(-1, len(df.Pclass.value_counts()))
#plt.title("Class Distribution")  

#plt.figure(figsize=(6,4))
#fig, ax = plt.subplots()
#df.logistlabel.value_counts().plot(kind='barh', color="blue", alpha=.65)
#ax.set_ylim(-1, len(df.logistlabel.value_counts())) 
#plt.title("Delay Breakdown (1 = Delayed, 0 = On time)")


#plt.figure(figsize=(6,4))
#fig, ax = plt.subplots()
#plt.scatter(df.logistlabel, df.a18, alpha=alpha_scatterplot)
## sets the y axis lable
#plt.ylabel("distance")
## formats the grid line style of our graphs                          
#plt.grid(b=True, which='major', axis='y')  
#plt.title("Delay by distance,  (1 = Delayed)")
#plt.show()

#formula = 'logistlabel ~ a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a15 + a16' 
# create a results dictionary to hold our regression results for easy analysis later
formula = 'logistlabel ~ a5 + a6 + a7 + a8 + a9 + a10 + a11 + a13 + a14' # works with accuracy 64% 
#formula = 'logistlabel ~ a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14' accuracy 62%
#formula = 'logistlabel ~ a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11 + a12 + a13 + a14 + a19'       
results = {} 
# create a regression friendly dataframe using patsy's dmatrices function
y,x = dmatrices(formula, data=df, return_type='dataframe')
ytest,xtest = dmatrices(formula, data=dftest, return_type='dataframe')
# instantiate our model
model = sm.Logit(y,x)

# fit our model to the training data
res = model.fit()

# save the result for outputing predictions later
results['Logit'] = [res, formula]
print res.summary()



# Plot Predictions Vs Actual
#plt.figure(figsize=(18,4));
#plt.subplot(111, axisbg="#DBDBDB")
## generate predictions from our fitted model
#ypred = res.predict(xtest)
#plt.plot(xtest.index, ypred, 'bo', xtest.index, ytest, 'go', alpha=.65);
#plt.grid(color='white', linestyle='dashed')
#plt.title('Logit predictions, Blue: \nFitted/predicted values: Red');
#
#plt.show()



