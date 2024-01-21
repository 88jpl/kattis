n = int(input())
txtList = input().split()
ab = ""
for i in txtList:
	if i[0].isupper():
		ab += i[0]
print(ab)
