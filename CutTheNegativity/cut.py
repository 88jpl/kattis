totalRows = int(input())
results = []
for i in range(1, totalRows + 1):
	cols = input().split()
	for j in range(1, len(cols) + 1):
		#print(i,j)
		answer = []
		if int(cols[j - 1]) != -1:
			answer.append(i)
			answer.append(j)
			answer.append(int(cols[j -1]))
			results.append(answer)
print(len(results))
for result in results:
	print(str(result[0]) + " " + str(result[1]) + " " + str(result[2]))
#print(results)

