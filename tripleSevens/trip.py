n = int(input())
result = 0
for i in range(3):
	txt = input().split()
	if txt.count("7") >= 1:
		result += 1
if result == 3:
	print(777)
else:
	print(0)
