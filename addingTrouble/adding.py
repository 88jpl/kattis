n = input()
splitInput = n.split()
if int(splitInput[0]) + int(splitInput[1]) == int(splitInput[2]):
	print("correct!")
else:
	print("wrong!")
