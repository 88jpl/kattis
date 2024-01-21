n = int(input())
for i in range(n):
	g = int(input())
	txt = input().split()
	for j in txt:
		if txt.count(j) != 2:
			print("Case #{}: {}".format(i + 1, j))
			break
