n = int(input())
for i in range(n):
	(a, b, x) = input().split()
	a = int(a)
	b = int(b)
	x = int(x)
	if a + b == x or a - b == x or b - a == x or a * b == x or a / b == x or b / a == x:
		print("Possible")
	else:
		print("Impossible")
