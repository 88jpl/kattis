(n, k, d) = input().split()
n = int(n)
k = int(k)
d = int(d)
total = 0
start = k + d - 14
for i in range(n):
	q = int(input())
	if q <= start:
		total += 1
print(total)
