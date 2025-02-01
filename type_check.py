def only_ints(num1, num2):

	if (type(num1) == float or type(num1) == str) or (type(num2) == float or type(num2) == str):
		return False
	else:
		return True

print(only_ints("a", 2))
print(only_ints(1,2))
