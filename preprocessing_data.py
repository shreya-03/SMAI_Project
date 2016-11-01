''' To execute this file input given as command line argument is the filename.csv which has the original data
	and it will create revisedfilename.csv file which has all integer elements
'''
#!/usr/bin/python
import csv,sys
if __name__ == "__main__":
	f=open(sys.argv[1],'rU')
	T1=csv.reader(f)
	temp=[]
	count_8=0
	count_10=0
	count_16=0
	count_17=0
	dictionary_8=dict()
	dictionary_10=dict()
	dictionary_16=dict()
	dictionary_17=dict()
	for row in T1:
#		print type(row)
		time=0
		for index,item in enumerate(row):	
			if index>=24 and index<=28 and row[index]!='NA':
				time+=int(row[index])
				row[index]=int(row[index])
			if index==14 or index==15:
				if row[index]!='NA':
#					time+=int(row[index])
					row[index]=int(row[index])
			if index==8:
				if item in dictionary_8.keys():
					row[index]=dictionary_8[item]
				else:
					dictionary_8[item]=count_8
					row[index]=count_8
					count_8+=1
			if index==10:
				if item in dictionary_10.keys():
					row[index]=dictionary_10[item]
				else:
					dictionary_10[item]=count_10
					row[index]=count_10
					count_10+=1
			if index==16:
				if item in dictionary_16.keys():
					row[index]=dictionary_16[item]
				else:
					dictionary_16[item]=count_16
					row[index]=count_16
					count_16+=1
			if index==17:
				if item in dictionary_17.keys():
					row[index]=dictionary_17[item]
				else:
					dictionary_17[item]=count_17
					row[index]=count_17
					count_17+=1
			if index==23:
				row[index]=int(row[index])
			if index==22:
				row[index]=-100001
			if index<23:
#				print row[index]
#				print item
				if row[index]=='NA':
					row[index]=-100001
				row[index]=int(row[index])
		if row[24]!='NA' and row[14]!='NA' and row[15]!='NA':
			if time>15:
				row[0]=1
			else:
				row[0]=0
			del row[22]
			del row[24:29]
			row[23]=time
			temp.append(row)
	filename='revised'+sys.argv[1]
	csv_file = open(filename, "wb")
	writer = csv.writer(csv_file)
	writer.writerows(temp)