from entropy import Entropy
def Gain(entropy,data,attr_index,target_index):
 
	val_freq = {}
	subset_entropy = 0.0
 	data_subset=[]
	# Calculate the frequency of each of the values in the target attribute
	for record in data:
		if (val_freq.has_key(record[attr_index])):
			val_freq[record[attr_index]] += 1.0
		else:
			val_freq[record[attr_index]]  = 1.0
 
	# Calculate the sum of the entropy for each subset of records weighted by their probability of occuring in the training set.
	for val in val_freq.keys():
		val_prob = val_freq[val] / sum(val_freq.values())
		for record in data:
			if record[attr_index]==val:
				data_subset.append(record)
		subset_entropy += val_prob * (Entropy(data_subset,0))
# 	print data_subset
	# Subtract the entropy of the chosen attribute from the entropy of the whole data set with respect to the target attribute (and return it)
#	print subset_entropy
	return (entropy- subset_entropy)