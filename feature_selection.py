#!/usr/bin/python
import csv
import sys
from entropy import Entropy
from IG import Gain
import matplotlib.pyplot as plt
if __name__ == "__main__":
	f=open(sys.argv[1],'rU')
	T1=csv.reader(f)
	data=[]
	attr=[]
	tgt_attr=[]
#	attr_index=int(sys.argv[2])
	for rows in T1:
		data.append(rows)
#		tgt_attr.append(rows[0])
#		for index,item in enumerate(rows):
#			if attr_index==index:
#				attr.append(item)
#	print tgt_attr
#	print attr
	gain=[]
	entr=Entropy(data,0)
#	print entr
	for i in range(1,29):
		gain.append(Gain(entr,data,i,0))
#	print gain
#	print range(29)
	x=list(range(1,29))
	plt.plot(x,gain,"ob")
	plt.ylabel('Gain')
	plt.axis([0,29,-1,1])
	plt.show()