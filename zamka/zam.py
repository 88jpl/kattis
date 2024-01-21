mi = int(input())
ma = int(input())
total = int(input())
answerMin = -1
answerMax = -1
for i in range(mi, ma + 1):
	#print(i)
	test = 0
	for j in str(i):
		#print("i: {}, j: {}".format(i, j))
		test += int(j)
	#print("test: {}".format(test))
	if test == total:
		answerMin = i
		break
for i in range(ma, mi - 1, -1):
	#print(i)
	test = 0
	for j in str(i):
		#print("i: {}, j: {}".format(i, j))
		test += int(j)
	#print("test: {}".format(test))
	if test == total:
		answerMax = i
		break
print(str(answerMin) +"\n" + str(answerMax))
