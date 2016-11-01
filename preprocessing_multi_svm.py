#!/usr/bin/python
import sys,csv
if __name__ == "__main__":
	f=open(sys.argv[1],'rU')
	T1=csv.reader(f)
	temp=[]
	for data in T1:
		temp.append(data)
	for instances in temp:	
		if int(instances[-1])>45:
			instances[0]=2
	filename='svm'+sys.argv[1]
	csv_file = open(filename, "wb")
	writer = csv.writer(csv_file)
	writer.writerows(temp)