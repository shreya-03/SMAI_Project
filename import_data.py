#!/usr/bin/python
import csv
import numpy
import scipy.ndimage
import sys
import scipy.io

if __name__ == "__main__":
	f=open('12months_test.csv','rU')
	T1=csv.reader(f)
	print T1
	print ' '
	print 'Okay.............'
	print ' '
	temp=[]
	for rows in T1:
		temp.append(rows)
	
	out = [int(k) for k in temp[0][0:2]]
	
	#print enumerate(temp[0])
	global count_8,count_10,count_16,count_17,dictionary_8,dictionary_10,dictionary_16,dictionary_17
	count_8=0
	count_10=0
	count_16=0
	count_17=0
	count=0
	dictionary_8=dict()
	dictionary_10=dict()
	dictionary_16=dict()
	dictionary_17=dict()
	
	for row in temp:
		count=0
		for index,item in enumerate(row):
			if index>=24 and index<=28:
				if item=='NA':
					count+=1
			if count==5:		# flight is not delayed
				row[0]=1
			if count<5:			# flight is delayed
				row[0]=2
	
			if index==8:
				if item in dictionary_8.keys():
					row[index]=dictionary_8[item]
				else:
					dictionary_8[item]=count_8
					row[index]=count_8
					count_8+=1
			elif index==10:
				if item in dictionary_10.keys():
					row[index]=dictionary_10[item]
				else:
					dictionary_10[item]=count_10
					row[index]=count_10
					count_10+=1
			elif index==16:
				if item in dictionary_16.keys():
					row[index]=dictionary_16[item]
				else:
					dictionary_16[item]=count_16
					row[index]=count_16
					count_16+=1
			elif index==17:
				if item in dictionary_17.keys():
					row[index]=dictionary_17[item]
				else:
					dictionary_17[item]=count_17
					row[index]=count_17
					count_17+=1
			elif item=='NA':
				row[index]=-10000
			elif index==22:
				if item=='A':
					row[index]=1
				else:
					row[index]=-100001
			else:
				row[index]=int(item)
	csv_file = open("revised40.csv", "wb")
	writer = csv.writer(csv_file)
	writer.writerows(temp)

	print temp
	scipy.io.savemat('12months_test.mat', mdict={'temp': temp})
