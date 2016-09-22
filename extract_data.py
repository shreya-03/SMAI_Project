#!/usr/bin/python
import csv,re
import sys
from sklearn import svm
if __name__ == "__main__":
	features=[]
	classes=[]
	count=0
	temp=[]
	f=open(sys.argv[1],'rU')
	T1=csv.reader(f)
	for rows in T1:
		temp.append(rows)
	for rows in temp:
		count+=1
		if count<40:
			features.append(rows[1:])
			classes.append(rows[0])
		else:
			test_feature=[int(elements) for elements in rows[1:]]
	features=[[int(elements) for elements in rows] for rows in features]
	classes=[int(elements) for elements in classes]
#	print features
#	print classes
#	print test_feature
	lin_clf = svm.LinearSVC()
	lin_clf.fit(features,classes)
	test_class=lin_clf.predict([test_feature])
	print test_class