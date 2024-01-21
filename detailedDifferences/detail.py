times = int(input())
for i in range(times):
	lineOne = input()
	lineTwo = input()
	result = ""
	for i in range(len(lineOne)):
		if lineOne[i] == lineTwo[i]:
			result = result + "."
		else:
			result = result + "*"
	print(lineOne)
	print(lineTwo)
	print(result)
