#!/usr/bin/python
import csv,sys
#from treeinterpreter import treeinterpreter as ti
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor,RandomForestClassifier
import numpy as np
from sklearn.metrics import make_scorer, mean_squared_error,accuracy_score,precision_score,recall_score,f1_score
import math
f = open(sys.argv[1],'rU')
T1 = csv.reader(f)
traindata = []
trainlabel = []
class_tlabels=[]
class_vlabels=[]
for data in T1:
	traindata.append(data[1:23])
	trainlabel.append(data[23])
	class_tlabels.append(data[0])
rf = RandomForestRegressor(n_estimators=1000,criterion='mse')
#print "befor fit"
rf.fit(traindata,trainlabel)
#print "after fit"
valid_f = open(sys.argv[2],'rU')
T2 = csv.reader(valid_f)
valid_data = []
valid_labels = []
for data in T2:
	valid_data.append(data[1:23])
	valid_labels.append(float(data[23]))
	class_vlabels.append(data[0])
predictions = []
for instances in valid_data:
#	print instances
	predictions.append(float(rf.predict(instances)))
#print predictions
s = 0.0
for i in range(len(valid_labels)):
	s += (predictions[i]-valid_labels[i])**2
#accuracy = math.sqrt(s/len(valid_labels))
rmse = np.sqrt(mean_squared_error(valid_labels, predictions))
print 'rmse:',rmse
class_rf = RandomForestClassifier(n_estimators=1000,criterion='gini')
class_rf.fit(traindata,class_tlabels)
class_predictions=[]
for instances in valid_data:
	class_predictions.append(class_rf.predict(instances))
#for label in class_predictions:
#	print label
class_predictions=[np.float64(elements) for elements in class_predictions]
class_vlabels=[np.float64(elements) for elements in class_vlabels]
print 'Accuracy:', accuracy_score(class_vlabels,class_predictions,normalize=True)
print 'Precision:', precision_score(class_vlabels,class_predictions,average='weighted')
print 'Recall:', recall_score(class_vlabels,class_predictions,average='weighted')
print 'F1 score:', f1_score(class_vlabels,class_predictions,average='weighted')	