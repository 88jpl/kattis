n = int(input())
while True:
	temp = 0
	for i in str(n):
		temp += int(i)
	if n % temp == 0:
		print(n)
		break
	else:
		n += 1
