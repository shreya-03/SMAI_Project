import math
def Entropy(data,target_index):
 
	val_freq = {}
	data_entropy = 0.0
 
	# Calculate the frequency of each of the values in the target attr
	for record in data:
		if (val_freq.has_key(record[target_index])):
			val_freq[record[target_index]] += 1.0
		else:
			val_freq[record[target_index]]  = 1.0
 
	# Calculate the entropy of the data for the target attribute
	for freq in val_freq.values():
		data_entropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
 
	return data_entropy