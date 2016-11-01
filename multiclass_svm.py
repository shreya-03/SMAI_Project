''' To execute this file inputs given as command line argument are the filename.csv which has all intgers values 
	and the number of instances used to construct classifier and the remaining is considered for testing to calculate
	accuracy and other performance metrics
	Second format of giving input is give the filename which is to be trained and other filename which will be used as 
	test samples and then accuracy is calculated 
'''
#!/usr/bin/python
import csv,re
import sys
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix	
if __name__ == "__main__":
	features=[]
	classes=[]
	count=0
	test_feature=[]
	testl_classes=[]
	testu_classes=[]
	f=open(sys.argv[1],'rU')
	T1=csv.reader(f)
	if '.csv' not in sys.argv[2]:
		for rows in T1:
			count+=1
			if count<int(sys.argv[2]):
				features.append([int(elements) for elements in rows[1:23]])
				classes.append(int(rows[0]))
			else:
				test_feature.append([int(elements) for elements in rows[1:23]])
				testl_classes.append(int(rows[0]))
		lin_clf = svm.SVC(C=0.01,kernel='linear')
		lin_clf.fit(features,classes)
		for rows in test_feature:
			testu_classes.append(int(lin_clf.predict([rows])))
#		print (lin_clf.predict([3,2,7,2225,2225,642,645,2,804,171,317,320,297,-3,0,42,5,2534,8,12,0,-100001,0,-10000,-10000,-10000,-10000,-10000]))
		testu_classes=[int(elements) for elements in testu_classes]
		testl_classes=[int(elements) for elements in testl_classes]
		print 'Accuracy:', accuracy_score(testl_classes,testu_classes,normalize=True)
		print 'Precision:', precision_score(testl_classes,testu_classes,average='weighted')
		print 'Recall:', recall_score(testl_classes,testu_classes,average='weighted')
		print 'F1 score:', f1_score(testl_classes,testu_classes,average='weighted')	
	else:
		for rows in T1:
			features.append([int(elements) for elements in rows[1:23]])
			classes.append(int(rows[0]))
		lin_clf=svm.SVC(C=0.01,kernel='rbf')
		lin_clf.fit(features,classes)
		test_f=open(sys.argv[2],'rU')
		T2=csv.reader(test_f)
		for rows in T2:
			testu_classes.append(int(lin_clf.predict([int(elements) for elements in rows[1:23]])))
			testl_classes.append(int(rows[0]))
		print 'Accuracy :',accuracy_score(testl_classes,testu_classes,normalize=True)
		print 'Precision:', precision_score(testl_classes,testu_classes,average='weighted')
		print 'Recall:', recall_score(testl_classes,testu_classes,average='weighted')
		print 'F1 score:', f1_score(testl_classes,testu_classes,average='weighted')
	print confusion_matrix(testl_classes,testu_classes)