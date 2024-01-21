dict = {}
for i in range(10):
	num = int(input())
	dict[num % 42] = 0
print(len(dict))
