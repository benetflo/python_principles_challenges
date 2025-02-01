def mid(string):

	length = len(string)
	if length % 2 != 0:
		middle_index = length / 2
		return string[int(middle_index)] 
	else:
		return " "

print(mid("abc"))
print(mid("aaaa"))
