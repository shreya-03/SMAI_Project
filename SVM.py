# To execute this file inputs given as command line argument are the filename.csv which has all intgers values and the number of instances used to construct classifier 
#!/usr/bin/python
import csv,re
import sys
import numpy as np
from sklearn import svm
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
if __name__ == "__main__":
	features=[]
	classes=[]
	count=0
	test_feature=[]
	testl_classes=[]
	testu_classes=[]
	f=open(sys.argv[1],'rU')
#	print sys.argv[2]
	T1=csv.reader(f)
	for rows in T1:
		count+=1
		if count<int(sys.argv[2]):
			features.append([int(elements) for elements in rows[1:]])
			classes.append(int(rows[0]))
		else:
			test_feature.append([int(elements) for elements in rows[1:]])
			testl_classes.append(int(rows[0]))
	lin_clf = svm.LinearSVC()
	lin_clf.fit(features,classes)
	count=0.0
	for rows in test_feature:
#		print lin_clf.predict([rows])
		testu_classes.append(int(lin_clf.predict([rows])))
#		print test_class
#	print testu_classes
#	for i in range(len(testu_classes)):
#		print testu_classes[i],testl_classes[i]
#		if int(testl_classes[i])==int(testu_classes[i]):
#			print "entered"
#			count+=1.0
#	print (count/len(testu_classes))*100
#	print (lin_clf.score(features,test_feature))
	print (lin_clf.predict([3,2,7,2225,2225,642,645,2,804,171,317,320,297,-3,0,42,5,2534,8,12,0,-100001,0,-10000,-10000,-10000,-10000,-10000]))
	testu_classes=[int(elements) for elements in testu_classes]
	testl_classes=[int(elements) for elements in testl_classes]
	print 'Accuracy:', accuracy_score(testl_classes,testu_classes,normalize=True)
	print 'Precision:', precision_score(testl_classes,testu_classes,average='weighted')
	print 'Recall:', recall_score(testl_classes,testu_classes,average='weighted')
	print 'F1 score:', f1_score(testl_classes,testu_classes,average='weighted')	
