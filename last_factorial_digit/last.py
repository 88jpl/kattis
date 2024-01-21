times = int(input())
for i in range(times):
	answer = 1
	n = int(input())
	for j in range(1, n):
		answer += j * answer
	print(answer % 10)
