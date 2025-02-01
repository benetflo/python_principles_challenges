def capital_indexes(string):
	counter = 0
	index_list = []
	for letter in string:
		if letter.isupper():
			index_list.append(counter)
		counter += 1
	return index_list

print(capital_indexes("HeLlO"))	
