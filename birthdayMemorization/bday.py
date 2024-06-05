b = {}
n = int(input())
for i in range(n):
	f = input().split()
	if b.get(f[2]) != None:
		if int(f[1]) > b.get(f[2])[1]:
			b[f[2]] = (f[0], int(f[1]))
	else:
		b[f[2]] = (f[0], int(f[1]))
bList = []
for key in b:
	bList.append(b[key][0])
print(len(bList))
bList.sort()
for i in bList:
	print(i)
