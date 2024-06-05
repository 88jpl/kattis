n = input().split()
row = int(n[0])
col = int(n[1])
result = ""
for i in range(row):
	line = input()
	for j in line:
		if j == ".":
			pass
		else:
			result += j
print(result)
