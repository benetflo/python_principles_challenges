def double_letters(string):
	index = 0
	while index < len(string) - 1:
		if string[index] == string[index + 1]:
			return True
		else:
			index += 1
	return False


print(double_letters("heloo"))
print(double_letters("nono"))
